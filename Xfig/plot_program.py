from Xfig.plot_object_name import plot_object_name
from Xfig.plot_use_name    import plot_use_name
from Xfig.plot_type_stat   import plot_type_stat

#===============================================================================
# Function to plot program box
#
# Parameters:
#   - file:               Xfig file's handle
#   - x0:                 object position on x axis in centimeters
#   - y0:                 object position on y axis in centimeters
#   - programe_name:      name of the program
#   - use_list:           list of subroutine use statements
#   - object:             object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function/program
#-------------------------------------------------------------------------------
def plot_program(file, x0, y0,         \
                 program_name,         \
                 use_list,             \
                 object):

  # Plot a header text box
  plot_object_name(file, x0, y0,         \
                   program_name,          \
                   object)

  # Plot a type statements box
  if object.N_Types() != 0:
    plot_type_stat(file, x0, y0, object)

  # Check if use box exist
  if use_list != "None":
    # Plot a use text box
    plot_use_name(file, x0, y0,       \
                  use_list,           \
                  object)
  else:
    use_list = 0

