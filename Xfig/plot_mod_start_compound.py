import Const
from Xfig.find_height import find_height
from Xfig.find_width  import find_width

#===============================================================================
# Function to start definition of a compound in xfig
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         module name)
#   - object:       object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - plot_module
#-------------------------------------------------------------------------------
def plot_mod_start_compound(file, x0, y0, text, object):

  box_width  = find_width(object)
  box_height = find_height(object)

  file.write("6 %9d %9d %9d %9d\n" % (                            \
     x0             * Const.XFIG_SCALE - Const.COMPOUND_MARGIN,   \
     y0             * Const.XFIG_SCALE - Const.COMPOUND_MARGIN,   \
    (x0+box_width)  * Const.XFIG_SCALE + Const.COMPOUND_MARGIN,   \
    (y0+box_height) * Const.XFIG_SCALE + Const.COMPOUND_MARGIN))

