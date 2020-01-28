#===============================================================================
# Function to end a compound in xfig
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
def plot_mod_end_compound(file, x0, y0, text, object):
  file.write("-6\n")

