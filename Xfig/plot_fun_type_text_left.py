#===============================================================================
# Function to plot function type (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting function type box
#-------------------------------------------------------------------------------
def plot_fun_type_text_left(file, x0, y0, object):

  fun_type      = object.fun_type
  box_width     = find_width(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = type_stat_len + 0.25                                    \
                + (y0 + const.FONT_SIZE + (const_UBH-const.FONT_SIZE)*0.5)

  plot_text_left(file, x0, y_pos, box_width,            \
                 const_UBH, fun_type, const.FONT_NORMAL)

