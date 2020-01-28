import attribute
from const import UNIT_BOX_HEIGHT as const_UBH
from Xfig.plot_spline_legend import plot_spline_legend
from Xfig.plot_text_center   import plot_text_center
from Xfig.find_width         import find_width
from Xfig.plot_fun_name      import plot_fun_name
from Xfig.plot_mod_name      import plot_mod_name
from Xfig.plot_sub_name      import plot_sub_name
from Xfig.plot_prog_name     import plot_prog_name

#===============================================================================
# Function to plot legend
#
# Parameters:
#   - file:         Xfig file's handle
#   - obj_list:     list of all objects
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def plot_legend(file, obj_list, x0, y0):

  object =  attribute.Program("Legend",                      \
                              "              Subroutine",    \
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
  text_height = const_UBH
  text_width  = find_width(object)

  # Boxes
  plot_mod_name(file,  x0,  y0,               "Module",     object)
  plot_sub_name(file,  x0,  y0+const_UBH,     "Subroutine", object)
  plot_fun_name(file,  x0,  y0+(const_UBH)*2, "Function",   object)
  plot_prog_name(file, x0,  y0+(const_UBH)*3, "Program",    object)

  # Splines
  plot_spline_legend(file, obj_list, x0, y0+const_UBH*5.5, text_width,  \
                     "Continuous")
  plot_spline_legend(file, obj_list, x0, y0+const_UBH*7.0, text_width,  \
                     "Dashed")
  plot_text_center(file, x0+1, y0+4.5*const_UBH,  \
                   text_width, text_height,       \
                   "Use statements")
  plot_text_center(file, x0+1, y0+6.0*const_UBH,  \
                   text_width,                    \
                   text_height,                   \
                   "Call statements")

