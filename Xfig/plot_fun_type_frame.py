import Const
from Xfig.check_if_function  import check_if_function
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.box_color          import box_color

#===============================================================================
# Function to plot an empty function type box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting function type box
#-------------------------------------------------------------------------------
def plot_fun_type_frame(file, x0, y0, box_width, box_height,  \
                        object):

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "     % Const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(Const.COLOR_BOX))
  file.write("11 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((x0+box_width) *Const.XFIG_SCALE,  \
                           (y0+box_height                     \
                           +fun_type_len                      \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height                     \
                           +fun_type_len                      \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d\n"% ( x0            *Const.XFIG_SCALE,  \
                           (y0+box_height)*Const.XFIG_SCALE))

