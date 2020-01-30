from Xfig.plot_object_name import plot_object_name
from Xfig.plot_type_stat   import plot_type_stat
from Xfig.plot_use_name    import plot_use_name
from Xfig.plot_var_name    import plot_var_name

#===============================================================================
# Function to plot subroutine box
#
# Parameters:
#   - file:               Xfig file's handle
#   - object:             object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_subroutine(file, object):

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
    # Plot a variable text box
    plot_var_name(file, object)

