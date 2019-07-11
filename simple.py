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
root  = "/home/simcic/Development/Synthetic-Eddies"

files = browse.source_files(root)      # list of all fortran files in root
file_path = browse.source_paths(root)  # list of all paths to fortran files

"""
from pprint import pprint
pprint(file_path)
"""


x0    = xfig.x_pos(file_path)               # upper left corner positions on x axis
y0    = 1                              # upper left corner positions on y axis

#===============================================================================
# Collecting classes into lists
#-------------------------------------------------------------------------------
"""
mod_list = attribute.mod_list_fun(files)
sub_list = attribute.sub_list_fun(files)

# Printing mods and subs and their levels
attribute.print_levels(mod_list,sub_list)
"""
#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.")

# Check directories for errors
# browse.check_directories(root)

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files in root
for i in range(len(file_path)):
  xfig.plot(xf, x0[i], y0, file_path[i])

# Print all unused files and subdirectories
#browse.source_unused(root)

#End
xf.close()
