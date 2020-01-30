import Const
from Xfig.check_if_function import check_if_function
from Xfig.find_width        import find_width
from Xfig.plot_text         import plot_text

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
def plot_use_text_list(file,         \
                       use_list,     \
                       object):

  use_list_num = list(range(len(use_list)))
  fun_type_len = check_if_function(object)

  for i in range(len(use_list)):
    plot_text(file, "Left",                                          \
              object.x0 + Const.UNIT_BOX_HEIGHT*0.333,               \
              object.y0 + Const.UNIT_BOX_HEIGHT*object.N_Types()     \
                        + Const.UNIT_BOX_HEIGHT*(use_list_num[i]+1)  \
                        + Const.UNIT_BOX_HEIGHT*0.75,                \
              use_list[i], Const.FONT_NORMAL, "Black", 10)

