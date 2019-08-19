#!/home/simcic/Programs/Anaconda3/bin/python3
#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import time
start = time.time()  # start time measuring

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

file_paths = []

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

    # Check if list of sources was specified
    if str(sys.argv[j]) == "-s" or str(sys.argv[j]) == "--sources":
      print("List of files is specified in:", str(sys.argv[j+1]),"\n")

      with open (str(sys.argv[j+1]), 'rt') as myfile:
        for line in myfile:
          if not line.startswith("#"):
            file_paths.append(line.rstrip("\n"))

      file_paths = list(filter(None, file_paths))

      for i in range(0,len(file_paths)):
        file_paths[i] = root + file_paths[i]

      obj_list = attribute.get_obj_list(file_paths)        # list of all objects
      obj_list = finder.get_new_calls(file_paths,obj_list) # updated objects

    if str(sys.argv[j]) == "-h" or str(sys.argv[j]) == "--help":
      print("\nProgram for extracting UML diagrams for modern Fortran programs")
      print("Author: Ivan Simcic\n")
      exit()

  # If user specifed object coordinates
  for j in range(1,len(sys.argv)):
    if str(sys.argv[j]) == "-g" or str(sys.argv[j]) == "--grid":
      print("\nObject coordinates are specified in:", str(sys.argv[j+1]),"\n")
      finder.find_coordinates(str(sys.argv[j+1]), obj_list)


#===============================================================================
# Obviously the main function
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
