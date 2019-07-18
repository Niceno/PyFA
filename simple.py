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

file_path  = browse.source_paths(root)         # list of paths to all .f90 files
file_list  = attribute.get_file_list(file_path)

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

attribute.plot_all_mod_spline(xf,file_list)
# Plot all fortran files starting from root
for i in range(len(file_list)):
  xfig.plot(xf, file_list[i].x0, file_list[i].y0, file_list[i])

# Plot spline between 2 boxes
#xfig.plot_spline(xf, file_list[1],file_list[2])
#attribute.plot_all_mod_spline(xf,file_path,file_list)
#End
xf.close()
