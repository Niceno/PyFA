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

  # Module definition has been found
  if object.Type() == "Module":

    plot_module(file, object)

  # Subroutine definition has been found
  elif object.Type() == "Subroutine":

    # If variables has not been found, do not plot subroutine
    if object.N_Vars() > 0:          # WHY THIS???
      plot_subroutine(file, object)

  # Function definition has been found
  elif object.Type() == "Function":

    # If variables has not been found, do not plot function
    if object.N_Vars() > 0:          # WHY THIS???
      plot_function(file, object)

  # Program definition has been found
  elif object.Type() == "Program":

    plot_program(file, object)

