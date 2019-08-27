#!/home/simcic/Programs/Anaconda3/bin/python3
#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import time
import const
start = time.time()  # start measuring time

import os            # needed for getcwd
import sys           # needed to get command line arguments
import xfig
import finder
import browse
import attribute

#===============================================================================
# Lists
#-------------------------------------------------------------------------------

# Set the current directory as the root
root = os.getcwd() + "/"
print("\nAnalyzing Fortan sources in: " + root)

# Initialize

file_paths = []
attribute.align_boxes             = "Diagonal"
attribute.object_hierarchy        = "Row-Based"
attribute.object_representation   = "Normal"

#-----------------------------------------
# Call without any command line arguments
#-----------------------------------------
if len(sys.argv) == 1:
  print("List of files not specified, branching through all sources from root.")

  # Get all sources
  file_paths = browse.source_paths(root)               # list- all paths to .f90
  obj_list = attribute.get_obj_list(file_paths)        # list of all objects
  obj_list = finder.get_new_calls(file_paths,obj_list) # list of updated objects

#-------------------------------------------
# Some command line arguments are specified
#-------------------------------------------
else:
  for j in range(1,len(sys.argv)):


    # Check if help was specified
    if str(sys.argv[j]) == "-h" or str(sys.argv[j]) == "--help":
      print("\nProgram for extracting UML diagrams for modern Fortran programs")
      print("\nUsage: simple.py [OPTION1]...[OPTION2]  or  simple.py [OPTION2]")
      print("Example1: simple.py -s source.list -a left")
      print("Example2: simple.py -a left")
      print("\nOPTION1 can be:")
      print("  -s, --sources [FILE] [OPTION2]        \
             Choose source list with paths for plotting")
      print("  -g, --grid [FILE]                     \
             Plot with user specifed objects coordinates")
      print("\nOPTION2 can be:")
      print("  -a, --align [ACTION]                  \
             Plot by specified object alignment: ")
      print("                                        \
              'left'     for left alignment")
      print("                                        \
              'diagonal' for diagonal alignment")
      print("  -oh, --object_hierarchy [ACTION]      \
             Plot by specified object hierarchy: ")
      print("                                        \
              'row'    for row based hierarchy")
      print("                                        \
              'column' for column based hierarchy")
      print("  -or, --object_representation [ACTION] \
             Plot by specified object hierarchy: ")
      print("                                        \
              'normal'  for normal representation")
      print("                                        \
              'compact' for compact representation")

      print("\nAuthor: Ivan Simcic\n")
      exit()


    # Check if alignment was specified
    if str(sys.argv[j]) == "-a" or str(sys.argv[j]) == "--align":
      try:
        if str(sys.argv[j+1]) == "left":
          attribute.align_boxes  = "Left"
        elif str(sys.argv[j+1]) == "diagonal":
          attribute.align_boxes  = "Diagonal"

      except:
        print("Input correct alignment! Can be 'left' or 'diagonal'")
        print("Plotting with 'diagonal' alignment\n")
        attribute.align_boxes = "Diagonal"

    # Check if object hierarchy was specified
    if str(sys.argv[j]) == "-oh" or            \
       str(sys.argv[j]) == "--object_hierarchy":
      try:
        if str(sys.argv[j+1]) == "column":
          attribute.object_hierarchy  = "Column-Based"
        elif str(sys.argv[j+1]) == "row":
          attribute.object_hierarchy  = "Row-Based"
      except:
        print("Input correct object hierarchy! Can be 'row' or 'column'")
        print("Plotting with 'row' hierarchy\n")
        attribute.object_hierarchy = "Row-Based"

    # Check if object representation was specified
    if str(sys.argv[j]) == "-or" or                 \
      str(sys.argv[j]) == "--object_representation":
      try:
        if str(sys.argv[j+1]) == "normal":
          attribute.object_representation  = "Normal"
        elif str(sys.argv[j+1]) == "compact":
          attribute.object_representation  = "Compresssed"
      except:
        print("Input correct object representation! Can be 'normal' or 'compact'")
        print("Plotting with 'normal' representation\n")
        attribute.object_representation = "Normal"

    file_paths = browse.source_paths(root)               # list- all paths to .f90
    obj_list = attribute.get_obj_list(file_paths)        # list of all objects
    obj_list = finder.get_new_calls(file_paths,obj_list) # list of updated objects


    # Check if list of sources was specified
    if str(sys.argv[j]) == "-s" or str(sys.argv[j]) == "--sources":
      try:
        second_input = str(sys.argv[j+1])
      except IndexError:
        second_input = "null"
        print("\nInsert correct argument! Missing source file name!\n")
        sys.exit()

      print("List of files is specified in:", str(sys.argv[j+1]),"\n")

      # Check if alignment was specified
      try:
        if str(sys.argv[j+2]) == "-a" or str(sys.argv[j+2]) == "--align":

          if str(sys.argv[j+3]) == "left":
            attribute.align_boxes  = "Left"
          elif str(sys.argv[j+3]) == "diagonal":
            attribute.align_boxes  = "Diagonal"

      except IndexError:
        print("Input correct alignment! Can be 'left' or 'diagonal'")
        print("Plotting with 'diagonal' alignment\n")
        attribute.align_boxes = "Diagonal"

      # Check if object hierarchy was specified
      try:
        if str(sys.argv[j+2]) == "-oh" or            \
           str(sys.argv[j+2]) == "--object_hierarchy":

          if str(sys.argv[j+3]) == "column":
            attribute.object_hierarchy  = "Column-Based"
          elif str(sys.argv[j+3]) == "row":
            attribute.object_hierarchy  = "Row-Based"

      except IndexError:
        print("Input correct object hierarchy! Can be 'row' or 'column'")
        print("Plotting with 'row' hierarchy\n")
        attribute.object_hierarchy = "Row-Based"

      # Check if object representation was specified
      try:
        if str(sys.argv[j+2]) == "-or" or                 \
           str(sys.argv[j+2]) == "--object_representation":

          if str(sys.argv[j+3]) == "normal":
            attribute.object_representation  = "Normal"
          elif str(sys.argv[j+3]) == "compact":
            attribute.object_representation  = "Compresssed"

      except IndexError:
        print("Input correct object representation! Can be 'normal' or 'compact'")
        print("Plotting with 'normal' representation\n")
        attribute.object_representation = "Normal"

      # Get list of objects from source.list
      with open (second_input, 'rt') as myfile:
        for line in myfile:
          if not line.startswith("#"):
            file_paths.append(line.rstrip("\n"))

      file_paths = list(filter(None, file_paths))

      for i in range(0,len(file_paths)):
        file_paths[i] = root + file_paths[i]

      obj_list = attribute.get_obj_list(file_paths)        # list of all objects
      obj_list = finder.get_new_calls(file_paths,obj_list) # updated objects


  # If user specifed object coordinates
  for j in range(1,len(sys.argv)):

    if str(sys.argv[j]) == "-g" or str(sys.argv[j]) == "--grid":

      file_paths = browse.source_paths(root)               # list- all paths to .f90
      obj_list = attribute.get_obj_list(file_paths)        # list of all objects
      obj_list = finder.get_new_calls(file_paths,obj_list) # list of updated objects

      try:
        second_input = str(sys.argv[j+1])
      except IndexError:
        second_input = "null"
        print("\nInsert correct argument! Missing object list file name!\n")
        sys.exit()

      print("\nObject coordinates are specified in:", str(sys.argv[j+1]),"\n")
      finder.find_coordinates(str(sys.argv[j+1]), obj_list)

     # Get all sources
      file_paths = browse.source_paths(root)                # list- all paths to .f90
      obj_list  = attribute.get_obj_list(file_paths)        # list of all objects
      obj_list  = finder.get_new_calls(file_paths,obj_list) # list of updated objects

  # Add options for:
  # -a | --align                  = diagonal or left
  # -oh | --object_hierarchy      = column or row
  # -or | --object_representation = normal or compact

#===============================================================================
# Obviously the main function for plotting
#-------------------------------------------------------------------------------

# Printing objects and their levels
#attribute.print_info(obj_list)
# Save names of all objects into .txt file
attribute.write_names(obj_list, "object_names.txt")

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files starting from root
xfig.plot_all(xf, obj_list)

#End
xf.close()

#Print out execution time
end = time.time()
print("Execution time:", end - start, "seconds")
