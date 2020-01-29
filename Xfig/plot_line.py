import Const

#===============================================================================
# Function to plot line
#
# Parameters:
#   - file:     Xfig file's handle
#   - x0:       first coordinate -> on x axis in centimeters
#   - y0:       first coordinate -> on y axis in centimeters
#   - x1:       second coordinate -> on x axis in centimeters
#   - y1:       second coordinate -> on y axis in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting grid
#-------------------------------------------------------------------------------
def plot_line(file, x0, y0, x1, y1, depth):

  file.write("2 1 0 1 2 7 %3d -1 -1 0.000 0 0 -1 0 0 2" % depth)

  file.write("\n%9d %9d" % ( (x0) * Const.XFIG_SCALE,  \
                             (y0) * Const.XFIG_SCALE))
  file.write("%9d %9d" %   ( (x1) * Const.XFIG_SCALE,  \
                             (y1) * Const.XFIG_SCALE))
  file.write("\n")

