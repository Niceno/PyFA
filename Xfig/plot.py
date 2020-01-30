from Xfig.plot_function   import plot_function
from Xfig.plot_module     import plot_module
from Xfig.plot_subroutine import plot_subroutine
from Xfig.plot_program    import plot_program

#===============================================================================
# Plot module, subroutine or function (choose which one to plot)
#
# Parameters:
#   - file:      Xfig file's handle
#   - object:    object to plot (can be subroutine or module)
# Returns:
#   - nothing
# Used by:
#   - function for plotting everything (the entire graph)
#-------------------------------------------------------------------------------
def plot(file, object):

  var_list    = object.var
  meth_list   = object.meth
  use_list    = object.use
  x0          = object.x0
  y0          = object.y0

  # Module definition has been found
  if object.Type() == "Module":

    # If variables has not been found, assign "No variables" and plot module
    if var_list == []:
      var_list = ["No variables"]

    plot_module(file, x0, y0,        \
                var_list,            \
                meth_list,           \
                use_list,            \
                object)

  # Subroutine definition has been found
  elif object.Type() == "Subroutine":

    # If variables has not been found, do not plot subroutine
    if var_list != []:
      plot_subroutine(file, x0, y0,    \
                    var_list,          \
                    use_list,          \
                    object)

  # Function definition has been found
  elif object.Type() == "Function":

    # If variables has not been found, do not plot function
    if var_list != []:
      plot_function(file, x0, y0,      \
                    var_list,          \
                    use_list,          \
                    object)

  # Program definition has been found
  elif object.Type() == "Program":

    plot_program(file, x0, y0,         \
                 use_list,             \
                 object)

