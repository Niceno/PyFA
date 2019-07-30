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
#file_paths = browse.remove_path(file_paths,"/home/simcic/Development/Synthetic-Eddies/Prof_Mod")

file_list = attribute.get_file_list(file_paths)    # list of all .f90 files

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.\n")

# Printing mods and subs and their levels
#attribute.print_levels(file_list)
# Check directories for errors
#browse.check_directories(root)
# Print all unused files and subdirectories
browse.source_unused(root)

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files starting from root
xfig.plot_all(xf,file_list)

#End
xf.close()
