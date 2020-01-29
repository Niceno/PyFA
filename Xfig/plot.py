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

  # Type of object is module, assign module name
  if object.Type() == "Module":
    mod_name  = object.name
    sub_name  = 0
    fun_name  = 0
    prog_name = 0

  # Type of object is subroutine, assign subroutine name
  elif object.Type() == "Subroutine":
    sub_name  = object.name
    mod_name  = 0
    fun_name  = 0
    prog_name = 0

  # Type of object is function, assign function name
  elif object.Type() == "Function":
    fun_name  = object.name
    mod_name  = 0
    sub_name  = 0
    prog_name = 0

  elif object.Type() == "Program":
    prog_name = object.name
    fun_name  = 0
    mod_name  = 0
    sub_name  = 0

  # Module definition has been found
  if mod_name !=0 :

  # If variables has not been found, assign "No variables" and plot module
    if var_list == []:
      var_list = ["No variables"]

    module_name = mod_name

    if (mod_name != []):

      plot_module(file, x0, y0,        \
                  module_name,         \
                  var_list,            \
                  meth_list,           \
                  use_list,            \
                  object)

  # Subroutine definition has been found
  elif sub_name != 0:
    subroutine_name = sub_name

  # If variables has not been found, do not plot subroutine
    if var_list != []:
      plot_subroutine(file, x0, y0,    \
                    subroutine_name,   \
                    var_list,          \
                    use_list,          \
                    object)

  # Function definition has been found
  elif fun_name != 0:
    function_name = fun_name

  # If variables has not been found, do not plot function
    if var_list != []:
      plot_function(file, x0, y0,      \
                    function_name,     \
                    var_list,          \
                    use_list,          \
                    object)

  # Program definition has been found
  elif prog_name != 0:
    program_name = prog_name

    plot_program(file, x0, y0,         \
                 program_name,         \
                 use_list,             \
                 object)

