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
root  = "/home/simcic/Development/PyFA"

file_path  = browse.source_paths(root)         # list of paths to all .f90 files

mod_list   = attribute.mod_list_fun(file_path) # list of all mod classes
sub_list   = attribute.sub_list_fun(file_path) # list of all sub classes
file_list  = [*mod_list,*sub_list]             # list of all classes(mod + sub)
file_list  = attribute.remove_empty(file_list) # remove empty files from list
x_position = xfig.x_pos(file_list)             # list of all x positions

# Printing mods and subs and their levels
attribute.print_levels(file_list)

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.")

# Check directories for errors
#browse.check_directories(root)

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files in root
for i in range(len(file_list)):
  file_list[i].x0 = x_position[i]     # update x0
  xfig.plot(xf, file_list[i].x0, (file_list[i].level*2)+1, file_list[i])

# Print all unused files and subdirectories
#browse.source_unused(root)

#End
xf.close()
