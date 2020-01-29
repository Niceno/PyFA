import Const
from Xfig.check_if_function  import check_if_function
from Xfig.check_if_type_stat import check_if_type_stat
from Xfig.box_color     import box_color
from Xfig.use_len            import use_len

#===============================================================================
# Function to plot an empty method box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - var_list:        list of variables
#   - meth_list:       list of methods
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_frame(file, x0, y0, box_width, box_height, \
                    var_list,                            \
                    meth_list,                           \
                    use_list,                            \
                    object):

  if object.var == 0:
    var_list = []

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "       % const.THICKNESS)
  file.write("0")
  file.write("%3d "       % box_color(const.COLOR_BOX))
  file.write("13 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFIG_SCALE, (y0+box_height  \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*XFIG_SCALE))
  file.write("%9d %9d"   % ((x0+box_width)*XFIG_SCALE, (y0+box_height  \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*XFIG_SCALE))
  file.write("%9d %9d"   % ((x0+box_width)*XFIG_SCALE, (y0+box_height  \
                           +len(var_list)         \
                           +len(meth_list)        \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*XFIG_SCALE))
  file.write("%9d %9d"   % ( x0           *XFIG_SCALE, (y0+box_height  \
                           +len(var_list)         \
                           +len(meth_list)        \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*XFIG_SCALE))
  file.write("%9d %9d\n" % ( x0           *XFIG_SCALE, (y0+box_height  \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*XFIG_SCALE))

