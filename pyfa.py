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

start = time.time()  # start measuring time

#===============================================================================
# Lists
#-------------------------------------------------------------------------------

# Set the current directory as the root
root = os.getcwd() + "/"
print("Analyzing Fortan sources in: " + root)

# Initialize
file_paths = []
obj_list   = []

attribute.align_boxes             = "Diagonal"
attribute.object_hierarchy        = "Row-Based"
attribute.object_representation   = "Normal"
attribute.grid                    = "None"
src_list                          = "None"
grid                              = "Grid-Off"

oh_specified = "None"
s_specified  = "None"
g_specified  = "None"

#-------------------------------------------
# Browse through command line arguments
#-------------------------------------------
for j in range(1,len(sys.argv),2):

  # Check if help was specified
  if str(sys.argv[j]) == "-h" or str(sys.argv[j]) == "--help":
    print("\nProgram for extracting UML diagrams for modern Fortran programs")
    print("\nAuthor: Ivan Simcic")
    print("\nUsage: simple.py [OPTIONS]")
    print("\nValid options are:\n")
    print("  -s,  --sources [FILE]                 \
           Choose source list with paths for plotting")
    print("\n  -a,  --align [SWITCH]                 \
           Plot by specified object alignment: ")
    print("                                        \
            'straight' for straight alignment")
    print("                                        \
            'diagonal' for diagonal alignment")
    print("  -oh, --object_hierarchy [SWITCH]      \
           Plot by specified object hierarchy: ")
    print("                                        \
            'row'    for row based hierarchy")
    print("                                        \
            'column' for column based hierarchy")
    print("  -or, --object_representation [SWITCH] \
           Plot by specified object hierarchy: ")
    print("                                        \
            'normal'  for normal representation")
    print("                                        \
            'compact' for compact representation")
    print("\nExample1: simple.py -s source.list -a straight")
    print("Example2: simple.py -a straight\n")

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
    elif str(sys.argv[j]) == "-oh" or            \
         str(sys.argv[j]) == "--object_hierarchy":
      if str(sys.argv[j+1]) == "column":
        oh_specified = "Column-Based"
        attribute.object_hierarchy  = "Column-Based"
      elif str(sys.argv[j+1]) == "row":
        oh_specified = "Row-Based"
        attribute.object_hierarchy  = "Row-Based"
      else:
        print("Incorrect switch:", sys.argv[j+1], "after", sys.argv[j])
        print("Allowed switches are 'row' or 'column'")
        print("Exiting the program")
        sys.exit()

    # Check if object representation was specified
    elif str(sys.argv[j]) == "-or" or                 \
         str(sys.argv[j]) == "--object_representation":
      if str(sys.argv[j+1]) == "normal":
        attribute.object_representation  = "Normal"
      elif str(sys.argv[j+1]) == "compact":
        attribute.object_representation  = "Compresssed"
      else:
        print("Incorrect switch:", sys.argv[j+1], "after", sys.argv[j])
        print("Allowed switches are: 'normal' or 'compact'")
        print("Exiting the program")
        sys.exit()

    elif str(sys.argv[j]) == "-s" or    \
         str(sys.argv[j]) == "--sources":

      s_specified = sys.argv[j+1]
      print("List of files is specified in:", str(sys.argv[j+1]),"\n")

    elif str(sys.argv[j]) == "-g" or    \
         str(sys.argv[j]) == "--grid":

      g_specified = sys.argv[j+1]
      print("\nObject coordinates are specified in:", str(sys.argv[j+1]),"\n")

    else:
      print("Unknow option:", sys.argv[j])
      print("Exiting the program")
      sys.exit()

# Tu, s obzirom na vrijednosti: g_specified, oh_specified ...

if s_specified != "None":

  # Get list of objects from source.list
  try: src_list = open (s_specified, 'rt')
  except:
    print("File", s_specified, "can't be found!  Exiting")
    sys.exit()

  with src_list:
    for line in src_list:
      if not line.startswith("#"):
        file_paths.append(line.rstrip("\n"))

  file_paths = list(filter(None, file_paths))

  for i in range(0,len(file_paths)):
    file_paths[i] = root + file_paths[i]

  obj_list = attribute.get_obj_list(file_paths)
  obj_list = finder.get_new_calls(file_paths,obj_list)


if g_specified != "None":
  file_paths = browse.source_paths(root)
  obj_list   = attribute.get_obj_list(file_paths)
  obj_list   = finder.get_new_calls(file_paths, obj_list)
  attribute.grid = "Default"

  if oh_specified == "Row-Based" or "None":
    obj_list   = finder.find_coordinates(g_specified, obj_list)
    grid       = "Grid-On"
  if oh_specified == "Column-Based":
    obj_list   = finder.find_coordinates(g_specified, obj_list)
    grid       = "Grid-On"

if src_list == "None" and grid == "Grid-Off":
  print("List of sources not specifed, browsing through all")
  file_paths = browse.source_paths(root)
  if not file_paths:
    print("No Fortran sources found!")
    print("Exiting the program")
    sys.exit()
  obj_list   = attribute.get_obj_list(file_paths)
  obj_list   = finder.get_new_calls(file_paths,obj_list)

#===============================================================================
# Obviously the main function for plotting
#-------------------------------------------------------------------------------

# Save names and coordinates of all objects into .txt file (hidden option)
# if g_specified == "None":
#   attribute.write_names(obj_list, const.OBJ_FILE_NAME)

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
