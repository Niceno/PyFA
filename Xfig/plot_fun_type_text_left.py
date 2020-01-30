import Const
from Xfig.find_width         import find_width
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.plot_text          import plot_text

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

  fun_type      = object.fun_type
  box_width     = find_width(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = type_stat_len + 0.25                                    \
                + (y0 + Const.FONT_SIZE  \
                + (Const.UNIT_BOX_HEIGHT-Const.FONT_SIZE)*0.5)

  plot_text(file, "Left",                                    \
            x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
            y0 + Const.UNIT_BOX_HEIGHT                       \
               + Const.UNIT_BOX_HEIGHT* type_stat_len        \
               + Const.UNIT_BOX_HEIGHT*0.75,                 \
            fun_type, Const.FONT_HEADER, "Black", 10)

