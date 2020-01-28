import const
from const import UNIT_BOX_HEIGHT as const_UBH
from const import XFIG_SCALE      as const_XFS
from Xfig.box_color import box_color

#===============================================================================
# Function to plot an empty module frame
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
#   - function for plotting module name box (header box)
#-------------------------------------------------------------------------------
def plot_mod_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(const.COLOR_HEADER_MODULE))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS,  y0            *const_XFS))

