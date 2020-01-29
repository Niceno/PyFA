#===============================================================================
# Function to plot function box
#
# Parameters:
#   - file:               Xfig file's handle
#   - x0:                 object position on x axis in centimeters
#   - y0:                 object position on y axis in centimeters
#   - function_name:      name of the function
#   - var_list:           list of function variables
#   - use_list:           list of function use statements
#   - object:             object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_function(file, x0, y0,       \
                  function_name,      \
                  var_list,           \
                  use_list,           \
                  object):

  # Plot a header text box
  plot_fun_name(file, x0, y0,         \
                function_name,        \
                object)

  # Plot a type statements box
  type_stat_len  = check_if_type_stat(object)
  if type_stat_len != 0:
    plot_type_stat(file, x0, y0, object)

  plot_fun_type_name(file, x0, y0,    \
                     object)

  # Check if use box exist
  if use_list != "None":
    # Plot a use text box
    plot_use_name(file, x0, y0,       \
                  use_list,           \
                  object)
  else:
    use_list = 0

  if object.var != 0:
   # Plot a variable text box
    plot_var_name(file, x0, y0,         \
                  var_list,             \
                  use_list,             \
                  object)
