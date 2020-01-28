import const
from const import XFIG_SCALE as const_XFS
from Xfig.font_code import font_code

#===============================================================================
# Function to print left aligned frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - text:            text to plot (variable,method or use statement)
# Returns:
#   - nothing
# Used by:
#   - functions for plotting variables, methods and use statements
#-------------------------------------------------------------------------------
def plot_text_left(file, x0, y0, box_width, box_height, text, font):

  file.write("4 0 0 10 -1 ")                     # 45 is depth
  file.write("%5d" % font_code(font))
  file.write("%3d" % (const.FONT_SIZE * 36))     # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                                # could be any value
  text_height = 3                                # could be any value
  file.write("%9d" % (text_height * const_XFS))  # text height in xfig units
  file.write("%9d" % (text_width  * const_XFS))  # text width in xfig units
  file.write("%9d %9d" % ( (x0+(box_height-const.FONT_SIZE)*0.5)*const_XFS,  \
                           (y0+const.FONT_SIZE                               \
                          +(box_height-const.FONT_SIZE)*0.5)*const_XFS))
  file.write("%s%s\\001\n" % (" ", text))

