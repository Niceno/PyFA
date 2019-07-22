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

file_path = browse.source_paths(root)             # list of paths to all .f90
file_list = attribute.get_file_list(file_path)    # list of all .f90 files
print(attribute.max_lvl_width(file_list))
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
xfig.plot_all(xf,file_list)

#End
xf.close()
