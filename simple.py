#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse

#===============================================================================
# Lists
#-------------------------------------------------------------------------------
root = "/home/simcic/Development/PyFA"

files = browse.source_files(root)      # list of all fortran files in root

x0        = xfig.x_pos(root)           # upper left corner positions on x axis
y0        = 1                          # upper left corner positions on y axis

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.")

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files in root
for i in range(len(files)):
  xfig.plot(xf, x0[i], y0, files[i])

# Print all unused files and subdirectories
unused = browse.source_unused(root)

#End
xf.close()
