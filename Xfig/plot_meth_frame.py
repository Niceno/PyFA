import Const
from Xfig.box_color import box_color

#===============================================================================
# Function to plot an empty method box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_frame(file, box_width, box_height, object):

  file.write("2 2 0 ")
  file.write("%3d "       % Const.THICKNESS)
  file.write("0")
  file.write("%3d "       % box_color(Const.COLOR_BOX))
  file.write("13 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( object.x0           *Const.XFIG_SCALE,  \
                            (object.y0+box_height                    \
                            +object.N_Vars()                         \
                            +object.N_Uses()                         \
                            +object.N_Types())   *Const.XFIG_SCALE))
  file.write("%9d %9d"   % ((object.x0+box_width)*Const.XFIG_SCALE,  \
                            (object.y0+box_height                    \
                            +object.N_Vars()                         \
                            +object.N_Uses()                         \
                            +object.N_Types())   *Const.XFIG_SCALE))
  file.write("%9d %9d"   % ((object.x0+box_width)*Const.XFIG_SCALE,  \
                            (object.y0+box_height                    \
                            +object.N_Vars()                         \
                            +object.N_Methods()                      \
                            +object.N_Uses()                         \
                            +object.N_Types())   *Const.XFIG_SCALE))
  file.write("%9d %9d"   % ( object.x0           *Const.XFIG_SCALE,  \
                            (object.y0+box_height                    \
                            +object.N_Vars()                         \
                            +object.N_Methods()                      \
                            +object.N_Uses()                         \
                            +object.N_Types())   *Const.XFIG_SCALE))
  file.write("%9d %9d\n" % ( object.x0           *Const.XFIG_SCALE,  \
                            (object.y0+box_height                    \
                            +object.N_Vars()                         \
                            +object.N_Uses()                         \
                            +object.N_Types())*Const.XFIG_SCALE))

