from const import XFIG_SCALE      as const_XFS
from const import COMPOUND_MARGIN as const_CMR
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

  file.write("6 %9d %9d %9d %9d\n" % (       \
     x0            *const_XFS - const_CMR,   \
     y0            *const_XFS - const_CMR,   \
    (x0+box_width) *const_XFS + const_CMR,   \
    (y0+box_height)*const_XFS + const_CMR))

