import Const
from Xfig.box_color import box_color

#===============================================================================
# Function to plot an empty function frame
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting function name box (header box)
#-------------------------------------------------------------------------------
def plot_fun_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % Const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(Const.COLOR_HEADER_FUNCTION))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,   \
                            y0            *Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,   \
                            y0            *Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,   \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,   \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d\n"% ( x0            *Const.XFIG_SCALE,   \
                            y0            *Const.XFIG_SCALE))

