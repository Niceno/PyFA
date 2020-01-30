import Const
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
#   - meth_list:    list of methods
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_meth_name(file,              \
                   meth_list,         \
                   object):

  box_width = find_width(object)

  # Plot methods framing box first
  plot_meth_frame(file, object.x0, object.y0,        \
                  box_width, Const.UNIT_BOX_HEIGHT,  \
                  meth_list, object)

  # Plot text
  plot_meth_text_left(file, object)

