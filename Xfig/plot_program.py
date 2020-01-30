from Xfig.plot_object_name import plot_object_name
from Xfig.plot_use_list    import plot_use_list
from Xfig.plot_type_list   import plot_type_list
from Xfig.plot_var_list    import plot_var_list

#===============================================================================
# Function to plot program box
#
# Parameters:
#   - file:               Xfig file's handle
#   - object:             object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function/program
#-------------------------------------------------------------------------------
def plot_program(file, object):

  # Plot a header text box
  plot_object_name(file, object)

  # Plot a type statements box
  if object.N_Types() > 0:
    plot_type_list(file, object)

  # If use statements have been found, plot use text box
  if object.N_Uses() > 0:
    plot_use_list(file, object)

  # If variables have been found, plot variables text box
  if object.N_Vars() > 0:
    plot_var_list(file, object)

