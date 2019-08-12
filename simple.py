#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
import attribute
#===============================================================================
# Lists
#-------------------------------------------------------------------------------
#root  = "/home/simcic/Development/T-Flows/Sources/IvanTest"
root  = "/home/simcic/Development/Synthetic-Eddies"

file_paths = browse.source_paths(root)             # list of paths to all .f90

#file_paths = browse.remove_path(file_paths,\
#            "/home/simcic/Development/Synthetic-Eddies/Prof_Mod")

obj_list = attribute.get_obj_list(file_paths)    # list of all .f90 files

 # Change object placement in grid (column,row)
#attribute.update_box_pos(obj_list,"Eddy_Mod",10,0)

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.\n")

# Printing objects and their levels
#attribute.print_levels(obj_list)

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
