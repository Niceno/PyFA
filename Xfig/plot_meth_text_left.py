import Const
from Xfig.check_if_function import check_if_function
from Xfig.find_width        import find_width
from Xfig.use_len           import use_len
from Xfig.plot_text         import plot_text

#===============================================================================
# Function to plot methods (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_text_left(file, object):

  fun_type_len  = check_if_function(object)

  for i in range(object.N_Methods()):
    plot_text(file, "Left",                                           \
              object.x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
              object.y0 + Const.UNIT_BOX_HEIGHT*object.N_Types()      \
                        + Const.UNIT_BOX_HEIGHT*fun_type_len          \
                        + Const.UNIT_BOX_HEIGHT*object.N_Vars()       \
                        + Const.UNIT_BOX_HEIGHT*object.N_Uses()       \
                        + Const.UNIT_BOX_HEIGHT*(i+1)                 \
                        + Const.UNIT_BOX_HEIGHT*0.75,                 \
                          object.methods[i], Const.FONT_NORMAL, "Black", 10)

