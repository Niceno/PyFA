import const
from const import XFIG_SCALE as const_XFS
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.box_color     import box_color

#===============================================================================
# Function to plot an empty type statement box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting type statement box
#-------------------------------------------------------------------------------
def plot_type_stat_frame(file, x0, y0, box_width, box_height,  \
                        object):

  type_stat_len = check_if_type_stat(object)

  if object.type == "Module":
    color = const.COLOR_HEADER_MODULE
  if object.type == "Subroutine":
    color = const.COLOR_HEADER_SUBROUTINE
  if object.type == "Function":
    color = const.COLOR_HEADER_FUNCTION
  if object.type == "Program":
    color = const.COLOR_HEADER_PROGRAM

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(color))
  file.write("11 -1 30 0.000 0 0 -1 0 0 5\n")         # 30*5 = 150% intensity
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height           \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height           \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

