import Const
from Xfig.check_if_function  import check_if_function
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.find_width         import find_width
from Xfig.plot_text_left     import plot_text_left

#===============================================================================
# Function to plot use statements (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting use statements box
#-------------------------------------------------------------------------------
def plot_use_text_left(file, x0, y0, \
                       use_list,     \
                       object):

  use_list_num  = list(range(len(use_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  box_width     = find_width(object)
  y_pos         = fun_type_len + type_stat_len + 0.25 \
                + (   y0               \
                   +  Const.FONT_SIZE  \
                   + (Const.UNIT_BOX_HEIGHT-Const.FONT_SIZE)*0.5)

  for i in range(len(use_list)):
    plot_text_left(file, x0, y_pos + use_list_num[i],       \
                   box_width, Const.UNIT_BOX_HEIGHT,        \
                   use_list[i], Const.FONT_NORMAL)

