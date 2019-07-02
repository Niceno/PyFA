#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
X0        = 1  # upper left corner position on x axis
Y0        = 1  # upper left corner position on y axis

#===============================================================================
# Lists
#-------------------------------------------------------------------------------

filename = "Eddy_Mod.f90"
#filename = "Save_Vtk.f90"

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("Great program for extracting UML from Fortran.")

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot module box
xfig.plot(xf, X0, Y0,        \
          filename)

#End
xf.close()
