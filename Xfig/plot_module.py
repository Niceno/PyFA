from Xfig.plot_object_end_compound   import plot_object_end_compound
from Xfig.plot_object_start_compound import plot_object_start_compound
from Xfig.plot_object_name           import plot_object_name
from Xfig.plot_type_stat             import plot_type_stat
from Xfig.plot_use_name              import plot_use_name
from Xfig.plot_meth_name             import plot_meth_name
from Xfig.plot_var_name              import plot_var_name

#===============================================================================
# Function to plot module box
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - object:          object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_module(file, object):

  # Start a compound around the module
  plot_object_start_compound(file, object)

  # Plot a header text box
  plot_object_name(file, object)

  # Plot a type statements box
  if object.N_Types() > 0:
    plot_type_stat(file, object)

  # If use statements have been found, plot use text box
  if object.N_Uses() > 0:
    plot_use_name(file, object)

  # If variables have been found, plot variables text box
  if object.N_Vars() > 0:
    plot_var_name(file, object)

  # If methods have been found, plot methods text box
  if object.N_Methods() > 0:
    plot_meth_name(file,            \
                   object.methods,  \
                   object)

  # End the compound around the module
  plot_object_end_compound(file, object)

