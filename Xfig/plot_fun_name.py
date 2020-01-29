import Const
from Xfig.find_width       import find_width
from Xfig.plot_fun_frame   import plot_fun_frame
from Xfig.plot_text        import plot_text

#===============================================================================
# Function to plot function name box (function header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (function name)
#   - object:       object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting function box
#-------------------------------------------------------------------------------
def plot_fun_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_fun_frame(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT)

  # Plot text
  plot_text(file, "Center",                   \
            x0 + box_width*0.5,               \
            y0 + Const.UNIT_BOX_HEIGHT*0.75,  \
            text, Const.FONT_HEADER, "Black", 10)
