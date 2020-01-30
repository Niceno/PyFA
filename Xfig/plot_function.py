from Xfig.plot_object_name           import plot_object_name
from Xfig.plot_fun_type_name         import plot_fun_type_name
from Xfig.plot_var_name              import plot_var_name
from Xfig.plot_use_name              import plot_use_name
from Xfig.plot_object_end_compound   import plot_object_end_compound
from Xfig.plot_object_start_compound import plot_object_start_compound

def difference (list1, list2):
  list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
  return list_dif

#===============================================================================
# Function to plot function box
#
# Parameters:
#   - file:               Xfig file's handle
#   - object:             object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_function(file, object):

  # Start a compound around the module
  plot_object_start_compound(file, object)

  # Plot a header text box
  plot_object_name(file, object)

  # Plot a type statements box
  if object.N_Types() != 0:
    plot_type_stat(file, object)

  plot_fun_type_name(file, object.x0, object.y0, object)

  # If use statements have been found, plot use text box
  if object.N_Uses() > 0:
    plot_use_name(file, object)

  # If variables have been found, plot variables text box
  if object.N_Vars() > 0:
    plot_var_name(file, object)

  # End the compound around the module
  plot_object_end_compound(file, object)
