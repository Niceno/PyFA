import Const
from Xfig.box_color import box_color

#===============================================================================
# Function to plot an empty type statement box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - object.x0:              object position on x axis in centimeters
#   - object.y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting type statement box
#-------------------------------------------------------------------------------
def plot_type_frame(file, box_width, box_height, object):

  type_stat_len = object.N_Types()

  if object.Type() == "Module":
    color = Const.COLOR_HEADER_MODULE
  if object.Type() == "Subroutine":
    color = Const.COLOR_HEADER_SUBROUTINE
  if object.Type() == "Function":
    color = Const.COLOR_HEADER_FUNCTION
  if object.Type() == "Program":
    color = Const.COLOR_HEADER_PROGRAM

  file.write("2 2 0 ")
  file.write("%3d "     % Const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(color))
  file.write("11 -1 30 0.000 0 0 -1 0 0 5\n")         # 30*5 = 150% intensity
  file.write("%9d %9d"  % ( object.x0            *Const.XFIG_SCALE,  \
                           (object.y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((object.x0+box_width) *Const.XFIG_SCALE,  \
                           (object.y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((object.x0+box_width) *Const.XFIG_SCALE,  \
                           (object.y0+box_height               \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ( object.x0            *Const.XFIG_SCALE,  \
                           (object.y0+box_height               \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d\n"% ( object.x0            *Const.XFIG_SCALE,  \
                           (object.y0+box_height)*Const.XFIG_SCALE))

