from const import UNIT_BOX_HEIGHT as const_UBH
from Xfig.find_width          import find_width
from Xfig.plot_meth_frame     import plot_meth_frame
from Xfig.plot_meth_text_left import plot_meth_text_left

#===============================================================================
# Function to plot methods box with text
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
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_meth_name(file, x0, y0,      \
                   var_list,          \
                   meth_list,         \
                   use_list,          \
                   object):

  box_width = find_width(object)

  # Plot methods framing box first
  plot_meth_frame(file, x0, y0, box_width, const_UBH,           \
                  var_list, meth_list, use_list, object)

  # Plot text
  plot_meth_text_left(x0, y0, file, var_list, meth_list, use_list, object)

