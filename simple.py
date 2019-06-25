#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig_module_box

#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
X0        = 1  # upper left corner position on x axis
Y0        = 1  # upper left corner position on y axis

#===============================================================================
# Lists and its "constants"
#-------------------------------------------------------------------------------
var_list = ["real :: xy","character :: name","integer :: r","integer:: xy"]
meth_list = ["Allocate_Cells","Calculate","Decompose"]
module_name = "Const_Mod"


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
