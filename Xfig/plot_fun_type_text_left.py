import Const
from Xfig.find_width import find_width
from Xfig.plot_text  import plot_text

#===============================================================================
# Function to plot function type (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting function type box
#-------------------------------------------------------------------------------
def plot_fun_type_text_left(file, x0, y0, object):

  fun_type  = object.fun_type

  plot_text(file, "Left",                                    \
            x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
            y0 + Const.UNIT_BOX_HEIGHT                       \
               + Const.UNIT_BOX_HEIGHT* object.N_Types()     \
               + Const.UNIT_BOX_HEIGHT*0.75,                 \
            fun_type, Const.FONT_HEADER, "Black", 10)

