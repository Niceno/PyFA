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

file_path = browse.source_paths(root)  # list of all paths to fortran files

mod_list = attribute.mod_list_fun(file_path)   # list of all mod classes
sub_list = attribute.sub_list_fun(file_path)   # list of all sub classes
file_list = [*mod_list,*sub_list]              # list of all classes(mod + sub)

x0    = xfig.x_pos(file_list)          # upper left corner positions on x axis
y0    = 1                              # upper left corner positions on y axis

for i in range(len(file_list)):
  file_list[i].x0 = i*14





# Printing mods and subs and their levels
attribute.print_levels(mod_list,sub_list)

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
  xfig.plot(xf, file_list[i].x0, file_list[i].level*10, file_list[i])

# Print all unused files and subdirectories
#browse.source_unused(root)

#End
xf.close()
