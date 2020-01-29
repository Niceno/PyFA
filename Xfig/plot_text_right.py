import Const
from Xfig.font_code import font_code

#===============================================================================
# Function to print right aligned frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - text:            text to plot (coordinates)
# Returns:
#   - nothing
# Used by:
#   - function for plotting grid
#-------------------------------------------------------------------------------
def plot_text_right(file, x0, y0, text):

  file.write("4 2 2 500 -1 ")                     # 500 is depth
  file.write("%5d" % font_code(Const.FONT_NORMAL))
  file.write("%3d" % (Const.FONT_SIZE * 36))      # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                                 # could be any value
  text_height = 3                                 # could be any value
  file.write("%9d" % (text_height * Const.XFIG_SCALE))  # text height xfig units
  file.write("%9d" % (text_width  * Const.XFIG_SCALE))  # text width xfig units
  file.write("%9d %9d" % ( (x0) * Const.XFIG_SCALE,  \
                           (y0) * Const.XFIG_SCALE))
  file.write("%s%s\\001\n" % (" ", text))

