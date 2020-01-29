import Const
from Xfig.find_width       import find_width
from Xfig.plot_sub_frame   import plot_sub_frame
from Xfig.plot_text        import plot_text

#===============================================================================
# Function to plot subroutine name box (subroutine header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (subroutine name)
#   - object:       object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting subroutine box
#-------------------------------------------------------------------------------
def plot_sub_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_sub_frame(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT)

  # Plot text
  plot_text(file, "Center",                   \
            x0 + box_width*0.5,               \
            y0 + Const.UNIT_BOX_HEIGHT*0.75,  \
            text, Const.FONT_HEADER, "Black", 10)

