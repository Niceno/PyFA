from const import XFIG_SCALE as const_XFS

#===============================================================================
# Function to plot spline (with 2 coordinates)
#
# Parameters:
#   - file:       Xfig file's handle
#   - obj_list:
#   - x0:         first coordinate on x axis
#   - y0:         first coordinate on y axis
# Returns:
#   - nothing
# Used by:
#   - function for plotting spline connections for legend
#-------------------------------------------------------------------------------
def plot_spline_legend(file, obj_list, x0, y0, width, line_type):

  x1 = x0 + width

  if line_type == "Continuous":
    file.write("3 0 0 1 0 7 ")
    file.write("%5d" % (50))
    file.write(" -1 -1 0.000 0 1 1 2")             # 2 --> number of points
  else:
    file.write("3 0 1 1 0 7 ")
    file.write("%5d" % (50))
    file.write(" -1 -1 4.000 0 1 1 2")             # 2 --> number of points

  if line_type == "Continuous":
    file.write("\n 1 1 2.00 120.00 120.00")        # arrow settings
    file.write("\n 6 1 2.00 120.00 120.00")        # arrow settings
  else:
    file.write("\n 1 0 2.00 120.00 120.00")        # arrow settings
    file.write("\n 6 0 2.00 120.00 120.00")        # arrow settings

  file.write("\n%9d %9d" % ( (x0) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("%9d %9d" %   ( (x1) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("\n 0.000 0.000\n")

