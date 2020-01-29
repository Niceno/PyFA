import Const
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.find_width         import find_width
from Xfig.plot_text        import plot_text

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

  type_stat_num  = list(range(type_stat_len))

  if type_stat_len != 0:
    for i in range(type_stat_len):
      plot_text(file, "Left",                                    \
                x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
                y0 + Const.UNIT_BOX_HEIGHT*(type_stat_num[i]+1)  \
                   + Const.UNIT_BOX_HEIGHT*0.75,                 \
                type_stat[i], Const.FONT_HEADER, "Black", 10)

