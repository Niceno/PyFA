from Xfig.plot_mod_end_compound   import plot_mod_end_compound
from Xfig.plot_mod_start_compound import plot_mod_start_compound
from Xfig.plot_mod_name           import plot_mod_name
from Xfig.plot_type_stat          import plot_type_stat
from Xfig.plot_use_name           import plot_use_name
from Xfig.plot_meth_name          import plot_meth_name
from Xfig.plot_var_name           import plot_var_name
from Xfig.check_if_type_stat      import check_if_type_stat

#===============================================================================
# Function to plot module box
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - module_name:     name of the module
#   - var_list:        list of module variables
#   - meth_list:       list of module methods
#   - use_list:        list of module use statements
#   - object:          object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_module(file, x0, y0,     \
                module_name,      \
                var_list,         \
                meth_list,        \
                use_list,         \
                object):

  # Start a compound around the module
  plot_mod_start_compound(file, x0, y0,   \
                          module_name,    \
                          object)

  # Plot a header text box
  plot_mod_name(file, x0, y0,     \
                module_name,      \
                object)

  # Plot a type statements box
  type_stat_len  = check_if_type_stat(object)
  if type_stat_len != 0:
    plot_type_stat(file, x0, y0, object)

  if use_list != "None":
    # If use statement has been found, plot use text box
    plot_use_name(file, x0, y0,   \
                  use_list,       \
                  object)
    # If use statement has not been found, do not plot use text box
  else:
    use_list = 0

  if object.var != 0:
    # Plot a variable text box
    plot_var_name(file, x0, y0,     \
                  var_list,         \
                  use_list,         \
                  object)

  if object.meth != 0:
    # Plot a method text box
    plot_meth_name(file, x0, y0,    \
                   var_list,        \
                   meth_list,       \
                   use_list,        \
                   object)

  # End the compound around the module
  plot_mod_end_compound(file, x0, y0,   \
                        module_name,    \
                        object)

