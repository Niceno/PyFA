#===============================================================================
# Function to plot an empty variable box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - var_list:        list of variables
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting variables box
#-------------------------------------------------------------------------------
def plot_var_frame(file, x0, y0, box_width, box_height, \
                   var_list,                            \
                   use_list,                            \
                   object):

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % box_color(const.COLOR_BOX))
  file.write("14 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height            \
                          +len(var_list)         \
                          +use_len(use_list)     \
                          +fun_type_len          \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height            \
                          +len(var_list)         \
                          +use_len(use_list)     \
                          +fun_type_len          \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

