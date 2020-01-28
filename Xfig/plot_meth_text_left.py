import const
from const import UNIT_BOX_HEIGHT as const_UBH
from Xfig.check_if_function  import check_if_function
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.find_width         import find_width
from Xfig.use_len            import use_len
from Xfig.plot_text_left     import plot_text_left

#===============================================================================
# Function to plot methods (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - meth_list:    list of methods
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_text_left(x0, y0, xf, \
                        var_list,   \
                        meth_list,  \
                        use_list,   \
                        object):

  if object.var == 0:
    var_list = []

  box_width     = find_width(object)
  meth_list_num = list(range(len(meth_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = fun_type_len + type_stat_len                         \
                + len(var_list) + use_len(use_list)                    \
                + (0.25 + (y0 + const.FONT_SIZE                        \
                + (const_UBH-const.FONT_SIZE)*0.5))

  for i in range(len(meth_list)):
    plot_text_left(xf, x0, y_pos + meth_list_num[i],                   \
                   box_width, const_UBH, meth_list[i], const.FONT_NORMAL)

