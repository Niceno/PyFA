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
#root  = "/home/simcic/Development/PyFA"

file_path  = browse.source_paths(root)         # list of paths to all .f90 files

mod_list   = attribute.mod_list_fun(file_path) # list of all mod classes
sub_list   = attribute.sub_list_fun(file_path) # list of all sub classes
file_list  = [*mod_list,*sub_list]             # list of all classes(mod + sub)
file_list  = attribute.remove_empty(file_list) # remove empty files from list
file_list  = attribute.update(file_list)       # updating coordinates
attribute.arrange_by_level(file_list)          # arranging by level
file_list = attribute.lvl_file_list(file_list) # put it together

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.\n")

# Printing mods and subs and their levels
#attribute.print_levels(file_list)

# Check directories for errors
#browse.check_directories(root)

# Print all unused files and subdirectories
#browse.source_unused(root)

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files starting from root
for i in range(len(file_list)):
  xfig.plot(xf, file_list[i].x0, file_list[i].y0, file_list[i])

"""
# Plot spline between boxes

for i in range(len(file_list)-1):

  xfig.plot_spline(xf, file_list[i].x0+ file_list[i].x1,           \
                       (file_list[i].y0+file_list[i].y1)/2,        \
                       file_list[i+1].x0,                          \
                       (file_list[i+1].y1+file_list[i+1].y0)/2)
"""

#End
xf.close()
