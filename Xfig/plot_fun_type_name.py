import Const
from Xfig.find_width              import find_width
from Xfig.plot_fun_type_frame     import plot_fun_type_frame
from Xfig.plot_fun_type_text_left import plot_fun_type_text_left

#===============================================================================
# Function to plot function type box with text
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
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_fun_type_name(file, x0, y0,   \
                       object):

  box_width = find_width(object)

  # Plot function type framing box first
  plot_fun_type_frame(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT, object)

  # Plot text
  plot_fun_type_text_left(file, x0, y0, object)

