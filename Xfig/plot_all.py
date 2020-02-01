import Const
from Xfig.plot_object     import plot_object
from Xfig.create_splines  import create_splines
from Xfig.plot_grid       import plot_grid
from Xfig.plot_legend     import plot_legend
from Xfig.plot_spline     import plot_spline

#===============================================================================
# Plot everything (the entire graph) from object list
#
# Parameters:
#   - file:       Xfig file's handle
#   - obj_list:   list of all objects representing modules or subroutines
#   - box_margins box margins which can be changed by command line option
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def plot_all(file, obj_list, box_margins):

  # Plot boxes
  for i in range(len(obj_list)):
    plot_object(file, obj_list[i])

  # Create splines                            offset          stride
  splines = create_splines(file, obj_list, box_margins, box_margins * 0.5)

  # Plot them all
  for s in range(len(splines)):
    plot_spline(file, splines[s])

  # Plot grid
  plot_grid(file, obj_list)

  # Plot legend
  plot_legend(file, obj_list, 0, -8 * Const.UNIT_BOX_HEIGHT)

