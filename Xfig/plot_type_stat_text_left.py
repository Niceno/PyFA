import Const
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.find_width         import find_width
from Xfig.plot_text_left     import plot_text_left

#===============================================================================
# Function to plot type statements (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting type statements box
#-------------------------------------------------------------------------------
def plot_type_stat_text_left(file, x0, y0, object):

  type_stat      = object.type_stat
  type_stat_len  = check_if_type_stat(object)
  box_width      = find_width(object)
  y_pos          = 0.25 + (y0 + Const.FONT_SIZE    \
                 + (Const.UNIT_BOX_HEIGHT - Const.FONT_SIZE) * 0.5)

  type_stat_num  = list(range(type_stat_len))

  if type_stat_len != 0:
    for i in range(type_stat_len):
      plot_text_left(file, x0, y_pos + type_stat_num[i], box_width,     \
                     Const.UNIT_BOX_HEIGHT, type_stat[i], Const.FONT_HEADER)

