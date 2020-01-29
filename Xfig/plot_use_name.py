import Const
from Xfig.find_width         import find_width
from Xfig.plot_use_frame     import plot_use_frame
from Xfig.plot_use_text_left import plot_use_text_left

#===============================================================================
# Function to plot use statements box with text
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
def plot_use_name(file, x0, y0, \
                  use_list,     \
                  object):

  box_width = find_width(object)

  # Plot use statements framing box first
  plot_use_frame(file, x0, y0,   \
                 box_width, Const.UNIT_BOX_HEIGHT, use_list, object)

  # Plot text
  plot_use_text_left(file, x0, y0, use_list, object)

