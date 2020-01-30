import Const
from Xfig.check_if_function import check_if_function
from Xfig.box_color         import box_color
from Xfig.use_len           import use_len

#===============================================================================
# Function to plot an empty use statements box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - object.x0:              object position on x axis in centimeters
#   - object.y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting use statements box
#-------------------------------------------------------------------------------
def plot_use_frame(file, box_width, box_height, object):

  fun_type_len  = check_if_function(object)
  type_stat_len = object.N_Types()

  file.write("2 2 0 ")
  file.write("%3d "     % Const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(Const.COLOR_BOX))
  file.write("12 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( object.x0            *Const.XFIG_SCALE,   \
                           (object.y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((object.x0+box_width) *Const.XFIG_SCALE,   \
                           (object.y0+box_height)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ((object.x0+box_width) *Const.XFIG_SCALE,   \
                           (object.y0+box_height                      \
                           +object.N_Uses()                           \
                           +fun_type_len                              \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d"  % ( object.x0            *Const.XFIG_SCALE,   \
                           (object.y0+box_height                      \
                           +object.N_Uses()                           \
                           +fun_type_len                              \
                           +type_stat_len)*Const.XFIG_SCALE))
  file.write("%9d %9d\n"% ( object.x0            *Const.XFIG_SCALE,   \
                           (object.y0+box_height)*Const.XFIG_SCALE))

