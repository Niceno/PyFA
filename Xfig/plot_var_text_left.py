import Const
from Xfig.check_if_function import check_if_function
from Xfig.find_width        import find_width
from Xfig.use_len           import use_len
from Xfig.plot_text         import plot_text

#===============================================================================
# Function to plot variables (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting variable box
#-------------------------------------------------------------------------------
def plot_var_text_left(file, x0, y0, \
                       var_list,     \
                       use_list,     \
                       object):

  box_width    = find_width(object)
  var_list_num = list(range(len(var_list)))
  fun_type_len = check_if_function(object)

  for i in range(len(var_list)):
    plot_text(file, "Left",                                    \
              x0 + Const.UNIT_BOX_HEIGHT*0.333,                \
              y0 + Const.UNIT_BOX_HEIGHT*object.N_Types()      \
                 + Const.UNIT_BOX_HEIGHT*fun_type_len          \
#                + Const.UNIT_BOX_HEIGHT*len(var_list)         \
                 + Const.UNIT_BOX_HEIGHT*use_len(use_list)     \
                 + Const.UNIT_BOX_HEIGHT*(var_list_num[i]+1)   \
                 + Const.UNIT_BOX_HEIGHT*0.75,                 \
                   var_list[i], Const.FONT_NORMAL, "Black", 10)

