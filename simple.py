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

filename = "Save_Vtk.f90"

var_list = finder.get_var(filename)
meth_list = finder.get_meth(filename)
header_name = finder.get_header(filename)

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
          header_name,       \
          var_list,          \
          meth_list,         \
          filename)

#End
xf.close()
