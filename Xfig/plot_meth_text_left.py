import Const
from Xfig.check_if_function  import check_if_function
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.find_width         import find_width
from Xfig.use_len            import use_len
from Xfig.plot_text          import plot_text

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

  for i in range(len(meth_list)):
    plot_text(xf, "Left",                                      \
              x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
              y0 + Const.UNIT_BOX_HEIGHT*type_stat_len         \
                 + Const.UNIT_BOX_HEIGHT*fun_type_len          \
                 + Const.UNIT_BOX_HEIGHT*len(var_list)         \
                 + Const.UNIT_BOX_HEIGHT*use_len(use_list)     \
                 + Const.UNIT_BOX_HEIGHT*(meth_list_num[i]+1)  \
                 + Const.UNIT_BOX_HEIGHT*0.75,                 \
                   meth_list[i], Const.FONT_NORMAL, "Black", 10)

