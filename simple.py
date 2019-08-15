#!/home/simcic/Programs/Anaconda3/bin/python3

#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import os          # needed for getcwd
import sys         # needed to get command line arguments
import xfig
import finder
import browse
import attribute

#===============================================================================
# Lists
#-------------------------------------------------------------------------------

# Set the current directory as the root
root = os.getcwd() + "/"
print("Analyzing Fortan sources in: " + root)

file_paths = []


#-----------------------------------------
# Call without any command line arguments
#-----------------------------------------
if len(sys.argv) == 1:
  print("List of files not specified, branching through all sources from root.")

  # Get all sources
  file_paths = browse.source_paths(root)             # list of paths to all .f90
  # print(file_paths)

#-------------------------------------------
# Some command line arguments are specified
#-------------------------------------------
else:
  if str(sys.argv[1]) == "-s" or str(sys.argv[1]) == "--sources":
    print("List of files is specified in:", str(sys.argv[2]))

    with open (str(sys.argv[2]), 'rt') as myfile:    # open file
      for line in myfile:                            # read line by line
        if not line.startswith("#"):                 # search for pattern
          file_paths.append(line.rstrip("\n"))

    file_paths = list(filter(None, file_paths))

    for i in range(0,len(file_paths)):
      file_paths[i] = root + file_paths[i]


obj_list = attribute.get_obj_list(file_paths)         # list of all objects
obj_list = finder.get_new_calls(file_paths,obj_list)  # list of updated objects

 # Change object placement in grid (row,column)

#attribute.update_box_pos(obj_list,"Point_Mod",0,1)



#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

# Printing objects and their levels
#attribute.print_info(obj_list)

# Check directories for errors
#browse.check_all(root)

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
