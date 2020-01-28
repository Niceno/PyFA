from const import XFIG_SCALE as const_XFS

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
def plot_line(file, x0, y0, x1, y1):

  file.write("2 1 0 1 2 7 500 -1 -1 0.000 0 0 -1 0 0 2")

  file.write("\n%9d %9d" % ( (x0) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("%9d %9d" %   ( (x1) * const_XFS,  \
                             (y1) * const_XFS))
  file.write("\n")

