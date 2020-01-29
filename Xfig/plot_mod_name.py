import Const
from Xfig.find_width       import find_width
from Xfig.plot_mod_frame   import plot_mod_frame
from Xfig.plot_text_center import plot_text_center

#===============================================================================
# Function to plot module name box (module header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (module name)
#   - object:       object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module box
#-------------------------------------------------------------------------------
def plot_mod_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_mod_frame(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT)

  # Plot text
  plot_text_center(file, x0, y0, box_width, Const.UNIT_BOX_HEIGHT, text)

