import Const
from Xfig.font_code import font_code

#===============================================================================
# Function to print centered frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - text:            text to plot (header name)
# Returns:
#   - nothing
# Used by:
#   - function for plotting header box
#-------------------------------------------------------------------------------
def plot_text_center(file, x0, y0, box_width, box_height, text):

  file.write("4 1 0 10 -1 ")                      # 45 is depth
  file.write("%5d" % font_code(Const.FONT_HEADER))
  file.write("%3d" % (Const.FONT_SIZE * 36))      # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                                 # could be any value
  text_height = 3                                 # could be any value
  file.write("%9d" % (text_height * Const.XFIG_SCALE))  # text height xfig units
  file.write("%9d" % (text_width  * Const.XFIG_SCALE))  # text width xfig units
  file.write("%9d %9d" % ( (x0+(box_width*0.5))*Const.XFIG_SCALE,     \
                           (y0+Const.FONT_SIZE                        \
                          +(box_height-Const.FONT_SIZE)*0.5)*Const.XFIG_SCALE))
  file.write("%s%s\\001\n" % (" ", text))

