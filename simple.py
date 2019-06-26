#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re
import xfig_module_box
import finder

#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
X0        = 1  # upper left corner position on x axis
Y0        = 1  # upper left corner position on y axis

#===============================================================================
# Lists
#-------------------------------------------------------------------------------

filename = "Mesh_Mod.f90"

var_list = finder.get_var(filename)
meth_list = finder.get_meth(filename)
module_name = finder.get_mod(filename)

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("Great program for extracting UML from Fortran.")

# Open Xfig file

xf = open("flow.fig", "w")

# Write header out
xfig_module_box.write_header(xf)

# Plot module box
xfig_module_box.plot(xf, X0, Y0,        \
                     module_name,       \
                     var_list,          \
                     meth_list)

#End
xf.close()
