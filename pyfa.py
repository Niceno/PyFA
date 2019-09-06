#!/usr/bin/python3

#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import time
import const
import os            # needed for getcwd
import sys           # needed to get command line arguments
import xfig
import finder
import browse
import attribute

# Start measuring time
start = time.time()

# Set the current directory as the root
root = os.getcwd() + "/"
print("Analyzing Fortan sources in: " + root)

# Initialize
file_paths = []
obj_list   = []

attribute.align_boxes           = "Diagonal"
attribute.object_hierarchy      = "Row-Based"
attribute.object_representation = "Reduced"
attribute.box_margins           = const.BOX_MARGINS

src_file    = "None"
s_specified = "None"
c_specified = "None"

#---------------------------------------
#
# Browse through command line arguments
#
#---------------------------------------
for j in range(1,len(sys.argv),2):

  # Check if help was specified
  if str(sys.argv[j]) == "-h" or str(sys.argv[j]) == "--help":
    print("\nProgram for extracting UML diagrams for modern Fortran programs")
    print("\nAuthor: Ivan Simcic")
    print("\nUsage: pyfa.py [OPTIONS]")
    print("\nValid options are:\n")
    print("  -a, --align [SWITCH]            \
    Plot by specified object alignment: ")
    print("                                  \
     'straight' for straight alignment")
    print("                                  \
     'diagonal' for diagonal alignment")
    print("  -c, --coordinates [FILE]        \
    Read object coordinates from the file")
    print("  -d, --detail_level [SWITCH]     \
    Plot by specified object detail: ")
    print("                                  \
     'normal'  for normal representation")
    print("                                  \
     'reduced' for reduced representation")
    print("                                  \
     'minimal' for minimal representation")
    print("  -h, --help                      \
    Displays this help screen")
    print("  -m, --margins [MARGIN]          \
    Set margin in cm for individual boxes")
    print("  -o, --object_hierarchy [SWITCH] \
    Plot by specified object hierarchy: ")
    print("                                  \
     'row'    for row based hierarchy")
    print("                                  \
     'column' for column based hierarchy")
    print("  -s, --sources [FILE]            \
    Choose source list with paths for plotting")
    print("\nExample1: pyfa.py -s source.list -a straight")
    print("Example2: pyfa.py -a straight\n")

    exit()

  if(len(sys.argv) > j+1):

    # Check if alignment was specified
    if str(sys.argv[j]) == "-a" or \
       str(sys.argv[j]) == "--align":
      if str(sys.argv[j+1]) == "diagonal":
        attribute.align_boxes  = "Diagonal"
      elif str(sys.argv[j+1]) == "straight":
        attribute.align_boxes  = "Left"
      else:
        print("Incorrect switch:", sys.argv[j+1], "after", sys.argv[j])
        print("Allowed switches are 'straight' or 'diagonal'")
        print("Exiting the program")
        sys.exit()

    # Check if object hierarchy was specified
    elif str(sys.argv[j]) == "-o" or            \
         str(sys.argv[j]) == "--object_hierarchy":
      if str(sys.argv[j+1]) == "column":
        attribute.object_hierarchy  = "Column-Based"
      elif str(sys.argv[j+1]) == "row":
        attribute.object_hierarchy  = "Row-Based"
      else:
        print("Incorrect switch:", sys.argv[j+1], "after", sys.argv[j])
        print("Allowed switches are 'row' or 'column'")
        print("Exiting the program")
        sys.exit()

    # Check if object representation was specified
    elif str(sys.argv[j]) == "-d" or                 \
         str(sys.argv[j]) == "--detail_level":
      if str(sys.argv[j+1]) == "normal":
        attribute.object_representation  = "Normal"
      elif str(sys.argv[j+1]) == "reduced":
        attribute.object_representation  = "Reduced"
      elif str(sys.argv[j+1]) == "minimal":
        attribute.object_representation  = "Minimal"
      else:
        print("Incorrect switch:", sys.argv[j+1], "after", sys.argv[j])
        print("Allowed switches are: 'normal', 'reduced' or 'minimal'")
        print("Exiting the program")
        sys.exit()

    # Check if margins were specified
    elif str(sys.argv[j]) == "-m" or    \
         str(sys.argv[j]) == "--margins":

      attribute.box_margins = float(sys.argv[j+1])
      print("Box margins are set to:", str(sys.argv[j+1]))

    # Check if list of sources were specified
    elif str(sys.argv[j]) == "-s" or    \
         str(sys.argv[j]) == "--sources":

      s_specified = sys.argv[j+1]
      print("List of files is specified in:", str(sys.argv[j+1]))

    # Check if file with object coordinates was specified
    elif str(sys.argv[j]) == "-c" or    \
         str(sys.argv[j]) == "--coordinates":

      c_specified = sys.argv[j+1]
      print("Object coordinates are specified in:", str(sys.argv[j+1]))

    else:
      print("Unknow option:", sys.argv[j])
      print("Exiting the program")
      sys.exit()

#----------------
#
# Main algorithm
#
#----------------

#---------------------------------------------------------------
# List of sources was not specified, browse the whole directory
#---------------------------------------------------------------
if s_specified == "None":

  print("List of sources not specifed, browsing through all")
  file_paths = browse.source_paths(root)

#---------------------------------------------
# List of sources was specified, read from it
#---------------------------------------------
else:

  # Get list of objects from source.list
  try: src_file = open (s_specified, 'rt')
  except:
    print("File", s_specified, "can't be found!  Exiting")
    sys.exit()

  with src_file:
    for line in src_file:
      if not line.startswith("#"):
        file_paths.append(line.rstrip("\n"))

  file_paths = list(filter(None, file_paths))

  for i in range(len(file_paths)):
    file_paths[i] = root + file_paths[i]

#--------------------------------------------------------------------
# For all cases, take object list from file paths and work out calls
#--------------------------------------------------------------------
obj_list, obj_memb = attribute.get_obj_lists(file_paths)
obj_list = finder.get_new_calls(file_paths, obj_list, obj_memb)

#-------------------------------------------------
# If logical coordinates specified, load them now
# (These should over-write those specified above)
#-------------------------------------------------
if c_specified != "None":
  obj_list = attribute.load_logical_coordinates(c_specified, obj_list)

if src_file == "None" and c_specified == "None":
  file_paths = browse.source_paths(root)
  if not file_paths:
    print("No Fortran sources found!")
    print("Exiting the program")
    sys.exit()

#----------------------------------------------------------
# If logical coordinates were not specified, save them now
#----------------------------------------------------------
if c_specified == "None":
  attribute.save_logical_coordinates(obj_list, const.OBJ_FILE_NAME)

#------------------------------------------
#
# Obviously the main function for plotting
#
#------------------------------------------

# Find object coordinates in Xfig units
xfig.find_coordinates(obj_list)

# Open Xfig file
xf = open(const.FIG_FILE_NAME, "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files starting from root
xfig.plot_all(xf, obj_list)

#End
xf.close()

#Print out execution time
end = time.time()
print("File", const.FIG_FILE_NAME, "has been created!")
print("Execution time:", end - start, "seconds")
