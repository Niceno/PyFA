#===============================================================================
# Function to plot variable box with text
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
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_var_name(file, x0, y0,       \
                  var_list,           \
                  use_list,           \
                  object):

  box_width = find_width(object)

  # Plot variable framing box first
  plot_var_frame(file, x0, y0, box_width, const_UBH, var_list, use_list, object)

  # Plot text
  plot_var_text_left(file, x0, y0, var_list, use_list, object)

