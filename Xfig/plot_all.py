from Xfig.plot_object     import plot_object
from Xfig.plot_all_spline import plot_all_spline
from Xfig.plot_grid       import plot_grid
from Xfig.plot_legend     import plot_legend

#===============================================================================
# Plot everything (the entire graph) from object list
#
# Parameters:
#   - file:      Xfig file's handle
#   - obj_list:  list of all objects representing modules or subroutines
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def plot_all(file, obj_list, box_margins):

  # Plot boxes
  for i in range(len(obj_list)):
    plot_object(file, obj_list[i])

  # Plot splines
  plot_all_spline(file, obj_list, box_margins)

  # Plot grid
  plot_grid(file, obj_list)

  # Plot legend
  plot_legend(file, obj_list, 0, -8)

