import Const
from Xfig.find_width               import find_width
from Xfig.plot_type_stat_frame     import plot_type_stat_frame
from Xfig.plot_type_stat_text_left import plot_type_stat_text_left

#===============================================================================
# Function to plot type statements box with text
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
def plot_type_stat(file, x0, y0,   \
                   object):

  box_width = find_width(object)

  # Plot type statement framing box first
  plot_type_stat_frame(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT, object)

  # Plot text
  plot_type_stat_text_left(file, x0, y0, object)

