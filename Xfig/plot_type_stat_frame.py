import Const
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
    color = Const.COLOR_HEADER_MODULE
  if object.type == "Subroutine":
    color = Const.COLOR_HEADER_SUBROUTINE
  if object.type == "Function":
    color = Const.COLOR_HEADER_FUNCTION
  if object.type == "Program":
    color = Const.COLOR_HEADER_PROGRAM

  file.write("2 2 0 ")
  file.write("%3d "     % Const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(color))
  file.write("11 -1 30 0.000 0 0 -1 0 0 5\n")         # 30*5 = 150% intensity
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,  \
                           (y0+box_height               \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height               \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d\n"% ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))

