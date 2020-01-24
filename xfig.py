#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import math
import finder
import browse
import attribute
import const
import grid
from const import XFIG_SCALE          as const_XFS
from const import UNIT_BOX_HEIGHT     as const_UBH
from const import STARTING_LAYER_USE  as const_SLU
from const import STARTING_LAYER_CALL as const_SLC
from const import UNIT_BOX_HEIGHT     as const_UBH
from const import COMPOUND_MARGIN     as const_CMR

#===============================================================================
# Function to choose use statements list length
#
# Parameters:
#   - list:  list of use statements
# Returns:
#   - use_list_len:  number of use statements, zero if none
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def use_len(list):
  if list != 0:
    use_list_len = len(list)
  else:
    use_list_len = 0
  return use_list_len

#===============================================================================
# Function to check if object is function
#
# Parameters:
#   - object:  checked object
# Returns:
#   - fun_type_len:  1 if it is function, 0 if it is not function
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def check_if_function(object):
  if object.type == "Function":
    fun_type_len = 1
  else:
    fun_type_len = 0
  return fun_type_len

#===============================================================================
# Function to check if object has type statements
#
# Parameters:
#   - object:  checked object
# Returns:
#   - fun_type_len:  1 if it is has type stat, 0 if not
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def check_if_type_stat(object):
  if object.type_stat != 0:
    type_len = len(object.type_stat)
  else:
    type_len = 0
  return type_len

#===============================================================================
# Return the code value of a Xfig font
#
# Parameters:
#   - name:  font name, the same name as in Xfig
# Returns:
#   - number corresponding to font code, as defined in Xfig format
# Used by:
#   - functions which plot text
#-------------------------------------------------------------------------------
def xfig_font_code(name):

  if name   == "Courier":
    return 12
  elif name == "Courier-Bold":
    return 14
  elif name == "Helvetica":
    return 16
  elif name == "Helvetica-Bold":
    return 18

#===============================================================================
# Return the code value of a Xfig box color
#
# Parameters:
#   - name:  color name, the same name as in Xfig
# Returns:
#   - number corresponding to color code, as defined in Xfig format
# Used by:
#   - functions which plot frames
#-------------------------------------------------------------------------------
def xfig_box_color(name):

  if name   == "Yellow":
    return  6
  elif name == "White":
    return  7
  elif name == "LtBlue":
    return 11
  elif name == "Pink2":
    return 28
  elif name == "Green2":
    return 14

#===============================================================================
# Function for calculating height of a box
#
# Parameters:
#   - object:    object for calculating height
# Returns:
#   - height     height of the box
# Used by:
#   - Function for updating object attributes
#-------------------------------------------------------------------------------
def find_height(object):

  use_list     = object.use
  var_list     = object.var
  meth_list    = object.meth
  call_list    = object.call
  type_list    = object.type_stat
  len_fun_type = 0

  if use_list == "None":
    use_list = []
  if var_list == 0:
    var_list = []
  if meth_list == 0:
    meth_list = []
  if type_list == 0:
    type_list = []
  if object.type == "Function":
    fun_type = object.fun_type
    if fun_type != 0:
      len_fun_type = 1

  height = const_UBH + len(var_list) + len(meth_list) + len(use_list)    \
         + len(type_list) + len_fun_type

  return height

#===============================================================================
# Choose box width depending on longest string
#
# Parameters:
#   - filename:   name of the Fortran file being read (.f90)
# Returns:
#   - var_width:  box width in Xfig drawing units
# Used by:
#   - functions which plot boxes
# Warning:
#   - Uses ghost parameter 0.4 to convert width from characters to Xfig units
#-------------------------------------------------------------------------------
def find_width(filename):

  header_name = filename.name
  var_list    = filename.var
  meth_list   = filename.meth
  use_list    = filename.use
  type_list   = filename.type_stat

  if filename.type == "Function":
    fun_type = filename.fun_type
  else:
    fun_type = ["0"]
  if use_list == 0:
    use_list = ["0"]
  else:
    use_list = use_list
  if meth_list == 0:
    meth_list = ["0"]
  else:
    meth_list = meth_list
  if var_list == []:
    var_list = ["No variables"]
  if var_list == 0:
    var_list = ["No variables"]
  if type_list == 0:
    type_list = ["No new types"]

  var_length      = max(var_list,  key=len)
  meth_length     = max(meth_list, key=len)
  use_length      = max(use_list,  key=len)
  fun_type_length = max(fun_type,  key=len)
  type_length     = max(type_list, key=len)

  lengths = [len(var_length),      len(meth_length), \
             len(header_name),     len(use_length),  \
             len(fun_type_length), len(type_length)]

  box_width = max(lengths)
  box_width = box_width * const_UBH * 0.4  # gives the best ratio for width

  return box_width

#===============================================================================
# Function to write xfig header
#
# Parameters:
#   - file:  xfig file's handle
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def write_header(file):

  file.write("#FIG 3.2  Produced by xfig version 3.2.6a\n")
  file.write("Landscape\n")
  file.write("Center\n")
  file.write("Metric\n")
  file.write("B0\n")
  file.write("100.00\n")
  file.write("Single\n")
  file.write("-2\n")
  file.write("1200 2\n")

#===============================================================================
# Plot everything (the entire graph) from object list
#
# Parameters:
#   - file:      Xfig file's handle
#   - obj_list:  list of all objects representing modules or subroutines
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def plot_all(file, obj_list):

  # Plot boxes
  for i in range(len(obj_list)):
    plot(file, obj_list[i])

  # Plot splines
  plot_all_spline(file, obj_list)

  # Plot grid
  plot_grid(file, obj_list)

  # Plot legend
  plot_legend(file, obj_list, 0, -8)

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
  if object.type == "Module":
    mod_name  = object.name
    sub_name  = 0
    fun_name  = 0
    prog_name = 0

  # Type of object is subroutine, assign subroutine name
  elif object.type == "Subroutine":
    sub_name  = object.name
    mod_name  = 0
    fun_name  = 0
    prog_name = 0

  # Type of object is function, assign function name
  elif object.type == "Function":
    fun_name  = object.name
    mod_name  = 0
    sub_name  = 0
    prog_name = 0

  elif object.type == "Program":
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

#===============================================================================
# Function to plot subroutine box
#
# Parameters:
#   - file:               Xfig file's handle
#   - x0:                 object position on x axis in centimeters
#   - y0:                 object position on y axis in centimeters
#   - subroutine_name:    name of the subroutine
#   - var_list:           list of subroutine variables
#   - use_list:           list of subroutine use statements
#   - object:             object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module/subroutine/function (choosing what to plot)
#-------------------------------------------------------------------------------
def plot_subroutine(file, x0, y0,      \
                    subroutine_name,   \
                    var_list,          \
                    use_list,          \
                    object):

  # Plot a header text box
  plot_sub_name(file, x0, y0,          \
                subroutine_name,       \
                object)

  # Plot a type statements box
  type_stat_len  = check_if_type_stat(object)
  if type_stat_len != 0:
    plot_type_stat(file, x0, y0, object)

  # Check if use box exist
  if use_list != "None":
    # Plot a use text box
    plot_use_name(file, x0, y0,        \
                  use_list,            \
                  object)
  else:
    use_list = 0

  if object.var != 0:
    # Plot a variable text box
    plot_var_name(file, x0, y0,         \
                  var_list,             \
                  use_list,             \
                  object)

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
  plot_prog_name(file, x0, y0,         \
                program_name,          \
                object)

  # Plot a type statements box
  type_stat_len  = check_if_type_stat(object)
  if type_stat_len != 0:
    plot_type_stat(file, x0, y0, object)

  # Check if use box exist
  if use_list != "None":
    # Plot a use text box
    plot_use_name(file, x0, y0,       \
                  use_list,           \
                  object)
  else:
    use_list = 0

#===============================================================================
# Function to plot an empty module frame
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting module name box (header box)
#-------------------------------------------------------------------------------
def plot_mod_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_HEADER_MODULE))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS,  y0            *const_XFS))

#===============================================================================
# Function to plot an empty subroutine frame
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting subroutine name box (header box)
#-------------------------------------------------------------------------------
def plot_sub_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_HEADER_SUBROUTINE))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS,  y0            *const_XFS))

#===============================================================================
# Function to plot an empty function frame
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting function name box (header box)
#-------------------------------------------------------------------------------
def plot_fun_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_HEADER_FUNCTION))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS,  y0            *const_XFS))

#===============================================================================
# Function to plot an empty program frame
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting program name box (header box)
#-------------------------------------------------------------------------------
def plot_prog_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_HEADER_PROGRAM))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS,  y0            *const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS,  y0            *const_XFS))

#===============================================================================
# Function to plot an empty type statement box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting type statement box
#-------------------------------------------------------------------------------
def plot_type_stat_frame(file, x0, y0, box_width, box_height,  \
                        object):

  type_stat_len = check_if_type_stat(object)

  if object.type == "Module":
    color = const.COLOR_HEADER_MODULE
  if object.type == "Subroutine":
    color = const.COLOR_HEADER_SUBROUTINE
  if object.type == "Function":
    color = const.COLOR_HEADER_FUNCTION
  if object.type == "Program":
    color = const.COLOR_HEADER_PROGRAM

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(color))
  file.write("11 -1 30 0.000 0 0 -1 0 0 5\n")         # 30*5 = 150% intensity
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height           \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height           \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

#===============================================================================
# Function to plot an empty function type box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - object:          object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting function type box
#-------------------------------------------------------------------------------
def plot_fun_type_frame(file, x0, y0, box_width, box_height,  \
                        object):

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_BOX))
  file.write("11 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height            \
                          +fun_type_len                                   \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height            \
                          +fun_type_len                                   \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

#===============================================================================
# Function to plot an empty use statements box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting use statements box
#-------------------------------------------------------------------------------
def plot_use_frame(file, x0, y0, box_width, box_height, \
                   use_list,                            \
                   object):

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_BOX))
  file.write("12 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height            \
                          +use_len(use_list)           \
                          +fun_type_len                \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height            \
                          +use_len(use_list)           \
                          +fun_type_len                \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

#===============================================================================
# Function to plot an empty variable box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - var_list:        list of variables
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting variables box
#-------------------------------------------------------------------------------
def plot_var_frame(file, x0, y0, box_width, box_height, \
                   var_list,                            \
                   use_list,                            \
                   object):

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "     % const.THICKNESS)
  file.write("0")
  file.write("%3d "     % xfig_box_color(const.COLOR_BOX))
  file.write("14 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height)*const_XFS))
  file.write("%9d %9d"  % ((x0+box_width)*const_XFS, (y0+box_height            \
                          +len(var_list)         \
                          +use_len(use_list)     \
                          +fun_type_len          \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d"  % ( x0           *const_XFS, (y0+box_height            \
                          +len(var_list)         \
                          +use_len(use_list)     \
                          +fun_type_len          \
                          +type_stat_len)*const_XFS))
  file.write("%9d %9d\n"% ( x0           *const_XFS, (y0+box_height)*const_XFS))

#===============================================================================
# Function to plot an empty method box (frame without text)
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - var_list:        list of variables
#   - meth_list:       list of methods
#   - use_list:        list of use statements
#   - object:          object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_frame(file, x0, y0, box_width, box_height, \
                    var_list,                            \
                    meth_list,                           \
                    use_list,                            \
                    object):

  if object.var == 0:
    var_list = []

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "       % const.THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(const.COLOR_BOX))
  file.write("13 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *const_XFS, (y0+box_height            \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*const_XFS))
  file.write("%9d %9d"   % ((x0+box_width)*const_XFS, (y0+box_height            \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*const_XFS))
  file.write("%9d %9d"   % ((x0+box_width)*const_XFS, (y0+box_height            \
                           +len(var_list)         \
                           +len(meth_list)        \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*const_XFS))
  file.write("%9d %9d"   % ( x0           *const_XFS, (y0+box_height            \
                           +len(var_list)         \
                           +len(meth_list)        \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*const_XFS))
  file.write("%9d %9d\n" % ( x0           *const_XFS, (y0+box_height            \
                           +len(var_list)         \
                           +use_len(use_list)     \
                           +fun_type_len          \
                           +type_stat_len)*const_XFS))

#===============================================================================
# Function to print centered frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - text:            text to plot (header name)
# Returns:
#   - nothing
# Used by:
#   - function for plotting header box
#-------------------------------------------------------------------------------
def plot_text_center(file, x0, y0, box_width, box_height, text):

  file.write("4 1 0 10 -1 ")                    # 45 is depth
  file.write("%5d" % xfig_font_code(const.FONT_HEADER))
  file.write("%3d" % (const.FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                               # could be any value
  text_height = 3                               # could be any value
  file.write("%9d" % (text_height * const_XFS))       # text height in xfig units
  file.write("%9d" % (text_width  * const_XFS))       # text width in xfig units
  file.write("%9d %9d" % ( (x0+(box_width*0.5))*const_XFS,            \
                           (y0+const.FONT_SIZE                        \
                          +(box_height-const.FONT_SIZE)*0.5)*const_XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print left aligned frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - box_width:       box width in centimeters
#   - box_height:      box height in centimeters
#   - text:            text to plot (variable,method or use statement)
# Returns:
#   - nothing
# Used by:
#   - functions for plotting variables, methods and use statements
#-------------------------------------------------------------------------------
def plot_text_left(file, x0, y0, box_width, box_height, text, font):

  file.write("4 0 0 10 -1 ")                     # 45 is depth
  file.write("%5d" % xfig_font_code(font))
  file.write("%3d" % (const.FONT_SIZE * 36))     # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                                # could be any value
  text_height = 3                                # could be any value
  file.write("%9d" % (text_height * const_XFS))  # text height in xfig units
  file.write("%9d" % (text_width  * const_XFS))  # text width in xfig units
  file.write("%9d %9d" % ( (x0+(box_height-const.FONT_SIZE)*0.5)*const_XFS,  \
                           (y0+const.FONT_SIZE                               \
                          +(box_height-const.FONT_SIZE)*0.5)*const_XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print right aligned frameless text
#
# Parameters:
#   - file:            Xfig file's handle
#   - x0:              object position on x axis in centimeters
#   - y0:              object position on y axis in centimeters
#   - text:            text to plot (coordinates)
# Returns:
#   - nothing
# Used by:
#   - function for plotting grid
#-------------------------------------------------------------------------------
def plot_text_right(file, x0, y0, text):

  file.write("4 2 2 500 -1 ")                    # 45 is depth
  file.write("%5d" % xfig_font_code(const.FONT_NORMAL))
  file.write("%3d" % (const.FONT_SIZE * 36))     # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                                # could be any value
  text_height = 3                                # could be any value
  file.write("%9d" % (text_height * const_XFS))  # text height in xfig units
  file.write("%9d" % (text_width  * const_XFS))  # text width in xfig units
  file.write("%9d %9d" % ( (x0) * const_XFS,  \
                           (y0) * const_XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to plot spline (with 6 coordinates)
#
# Parameters:
#   - file:     Xfig file's handle
#   - object1:  starting object (spline starts at the rigth side of this object)
#   - object2:  ending object   (spline ends at the left side of this object)
#   - depth:    depth of plotted spline
# Returns:
#   - nothing
# Used by:
#   - function for plotting spline connections
#-------------------------------------------------------------------------------
def plot_spline(file, obj_list, object1, object2, line_type, depth):

  # print("Connecting ", object1.name, "and", object2.name)

  offset = attribute.box_margins * 1.00

  xc1 = object1.x0 + object1.w * 0.5
  xc2 = object2.x0 + object2.w * 0.5

  # 0.7 in lines below is to avoid coinciding lines
  if abs(xc1 - xc2) <= offset:
    x1 = object1.x0              # start at the lhs of object1
    x2 = x1 - offset * 0.7       # continue to the left
    x6 = object2.x0              # end on the lhs of object1
    x5 = x6 - offset * 0.7       # come from left side

  elif xc1 < xc2 - offset:
    x1 = object1.x0 + object1.w  # start at the rhs of object1
    x2 = x1 + offset * 0.7       # continue to the right
    x6 = object2.x0              # end on the lhs of object1
    x5 = x6 - offset * 0.7       # come from left side

  else:
    x1 = object1.x0              # start at the lhs of the object1
    x2 = x1 - offset * 0.7       # continue to the left
    x6 = object2.x0 + object2.w  # end on the rhs of object2
    x5 = x6 + offset * 0.7       # come from right side

  # First height depends on line_type
  if line_type == "Continuous":
    # y1 = object1.y0 + object1.h * 0.5  # starts in the middle of object1
    y1 = object1.y0 + const_UBH * 0.5  # starts from the middle of header
  elif line_type == "Dashed":
    y1 = object1.y0 + const_UBH * 0.5  # starts from the middle of header

  # Second coordinate should be the same as first
  y2 = y1

  # Last coordinate for continous lines (use statements)
  if line_type == "Continuous":
    ind = object2.use.index("use " + object1.name)
    y6 = object2.y0 + const_UBH                    \
                    + check_if_type_stat(object2)  \
                    + ind * const_UBH              \
                    + 0.5 * const_UBH

  # Last coordinate for dashed lines (call statements)
  elif line_type == "Dashed":
    y6 = object2.y0 + const_UBH * 0.5  # hits in the middle of the header

  # Penultimate coordinate should be the same as last
  y5 = y6

  # Walk!
  x, y = walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list)

  # Start writing a spline
  if line_type == "Continuous":
    file.write("3 2 0 2 0 7 ")
    file.write("%5d" % (depth))
    file.write(" -1 -1 0.000 0 1 1 %6d" % len(x))
  elif line_type == "Dashed":
    file.write("3 2 1 2 0 7 ")
    file.write("%5d" % (depth))
    file.write(" -1 -1 8.000 0 1 1 %6d" % len(x))  # 8.000 is dash length

  # Arrow settings
  if line_type == "Continuous":
    file.write("\n 1 1 1.00 135.00 180.00")
    file.write("\n 6 1 1.00 135.00 180.00")
  elif line_type == "Dashed":
    file.write("\n 1 0 1.00 135.00 180.00")
    file.write("\n 6 0 1.00 135.00 180.00")

  cnt = 0
  for i in range(len(x)):
    if cnt % 4 == 0:
      file.write("\n       ")
    file.write(" %9d %9d" % ( x[i] * const_XFS, y[i] * const_XFS))
    cnt = cnt + 1

  cnt = 0
  for i in range(len(x)):
    if cnt % 4 == 0:
      file.write("\n       ")
    if i == 0 or i == len(x)-1:
      file.write(" 0.000")
    else:
      file.write(" 1.000")
    cnt = cnt + 1

  file.write("\n")

#===============================================================================
# Walk from one object to another, avoiding all objects in the graph
#
# Parameters:
#   - x1, y1, ... x6, y6:  coordinates the way Ivan introduced them
#   - obj_list:            list of all objects
# Returns:
#   - x, y:                coordinates with all steps from one object to another
#-------------------------------------------------------------------------------
def walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list):

  # Walk
  x    = []
  y    = []
  dist = []
  keep = []

  x.append(x1)
  y.append(y1)

  x.append(x2)
  y.append(y2)

  #-----------
  #
  # Main loop
  #
  #-----------
  for i in range(0, 512):

    #--------------------------   3 2 1
    # Set eight possible direc    4 c 0
    #--------------------------   5 6 7
    step_x    = []
    step_y    = []
    step_dist = []

    stride = attribute.box_margins * 0.45

    # Step 0                        # Step 1
    step_x.append(x[-1] + stride);  step_x.append(x[-1] + stride)
    step_y.append(y[-1]);           step_y.append(y[-1] + stride)

    # Step 2                        # Step 3
    step_x.append(x[-1]);           step_x.append(x[-1] - stride)
    step_y.append(y[-1] + stride);  step_y.append(y[-1] + stride)

    # Step 4                        # Step 5
    step_x.append(x[-1] - stride);  step_x.append(x[-1] - stride)
    step_y.append(y[-1]);           step_y.append(y[-1] - stride)

    # Step 6                        # Step 7
    step_x.append(x[-1]);           step_x.append(x[-1] + stride)
    step_y.append(y[-1] - stride);  step_y.append(y[-1] - stride)

    #---------------------------------------------------
    # Eliminate steps which would fall in other objects
    #---------------------------------------------------
    eliminate_steps = []
    for o in range(len(obj_list)):
      for s in range(len(step_x)):
        if step_x[s] >= (obj_list[o].x0                 - stride * 0.5) and \
           step_x[s] <= (obj_list[o].x0 + obj_list[o].w + stride * 0.5) and \
           step_y[s] >= (obj_list[o].y0                 - stride * 0.5) and \
           step_y[s] <= (obj_list[o].y0 + obj_list[o].h + stride * 0.5):
          eliminate_steps.append(s)
    eliminate_steps.sort(reverse = True)
    for e in range(len(eliminate_steps)):
      step_x.pop(eliminate_steps[e])
      step_y.pop(eliminate_steps[e])

    #-------------------------------------
    # Eliminate steps which would go back
    #-------------------------------------
    eliminate_steps = []
    for s in range(len(step_x)):
      if step_x[s] == x[-2] and step_y[s] == y[-2]:
        eliminate_steps.append(s)
    eliminate_steps.sort(reverse = True)
    for e in range(len(eliminate_steps)):
      step_x.pop(eliminate_steps[e])
      step_y.pop(eliminate_steps[e])

    #-----------------------------------------
    # From the remaining (possible) steps, do
    # find the one closest to the destination
    #-----------------------------------------
    for s in range(len(step_x)):
      dx = step_x[s] - x5
      dy = step_y[s] - y5
      step_dist.append(math.sqrt(dx*dx + dy*dy))

    # Index of direction with minimum distance
    min_dist = step_dist.index(min(step_dist))

    x.   append(step_x[min_dist])
    y.   append(step_y[min_dist])
    dist.append(min(step_dist))
    keep.append(True)

    # Check if converged
    if dist[-1] < (attribute.box_margins * 0.5):
      x = x[:-2]
      y = y[:-2]
      break

    # Check if it wobbles (only if you are close)
    if len(dist) > 2:
      if dist[-1] < (attribute.box_margins):
        if dist[-1] > dist[-2]:
          x = x[:-3]
          y = y[:-3]
          break

  x.   append(x5)
  y.   append(y5)
  keep.append(True)

  x.   append(x6)
  y.   append(y6)
  keep.append(True)

  #------------------------------------------------
  #
  # Eliminate the points in-between straight lines
  #
  #------------------------------------------------

  # Mark points in between straight lines for deletion
  for i in range(1, len(x)-1):
    dx_p = x[i+1] - x[i]
    dy_p = y[i+1] - y[i]
    dx_m = x[i]   - x[i-1]
    dy_m = y[i]   - y[i-1]
    if abs(dx_p - dx_m) < 0.1 and abs(dy_p - dy_m) < 0.1:
      keep[i] = False

  # Yet, keep the points next to ones which are kept (to preserve curves)
  keep_2 = keep[:]
  for i in range(1, len(x)-1):
    if not keep[i]:
      if keep[i-1] or keep[i+1]:
        keep_2[i] = True

  # Make a compressed list of x and y coordinates
  x_c = []
  y_c = []
  for i in range(0, len(x)):
    if keep_2[i]:
      x_c.append(x[i])
      y_c.append(y[i])

  return x_c, y_c

#===============================================================================
# Function to plot spline (with 2 coordinates)
#
# Parameters:
#   - file:       Xfig file's handle
#   - obj_list:
#   - x0:         first coordinate on x axis
#   - y0:         first coordinate on y axis
# Returns:
#   - nothing
# Used by:
#   - function for plotting spline connections for legend
#-------------------------------------------------------------------------------
def plot_spline_legend(file, obj_list, x0, y0, width, line_type):

  x1 = x0 + width

  if line_type == "Continuous":
    file.write("3 0 0 1 0 7 ")
    file.write("%5d" % (50))
    file.write(" -1 -1 0.000 0 1 1 2")             # 2 --> number of points
  else:
    file.write("3 0 1 1 0 7 ")
    file.write("%5d" % (50))
    file.write(" -1 -1 4.000 0 1 1 2")             # 2 --> number of points

  if line_type == "Continuous":
    file.write("\n 1 1 2.00 120.00 120.00")        # arrow settings
    file.write("\n 6 1 2.00 120.00 120.00")        # arrow settings
  else:
    file.write("\n 1 0 2.00 120.00 120.00")        # arrow settings
    file.write("\n 6 0 2.00 120.00 120.00")        # arrow settings

  file.write("\n%9d %9d" % ( (x0) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("%9d %9d" %   ( (x1) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("\n 0.000 0.000\n")

#===============================================================================
# Function for plotting all spline connections
#
# Parameters:
#   - file:      Xfig file's handle
#   - obj_list:  list of all objects representing modules or subroutines
# Returns:
#   - nothing
# Used by:
#   - function for plotting everything (the entire graph) from object list
#-------------------------------------------------------------------------------
def plot_all_spline(file, obj_list):

  use_objects  = []
  mod_objects  = []
  call_objects = []

  # Getting list with only modules
  for i in range(len(obj_list)):
    if obj_list[i].type == "Module":
      mod_objects.append(obj_list[i])

  # Getting list with objects that have use statements
  for i in range(len(obj_list)):
    if obj_list[i].use != "None":
      use_objects.append(obj_list[i])

  # Getting list with objects that have call statements
  for i in range(len(obj_list)):
    if obj_list[i].call != 0:
      call_objects.append(obj_list[i])


  depth_list_use  = list(range(const_SLU,    \
                               const_SLU + len(mod_objects)))
  depth_list_call = list(range(const_SLC,    \
                               const_SLC + len(call_objects)))

  # Plotting connections for use statements
  for i in range(len(use_objects)):
    use = use_objects[i].use
    for k in range(len(use)):
      used = use[k]
      used = used.strip("use ")
      for m in range(len(mod_objects)):
        if used == mod_objects[m].name:
          plot_spline(file,               \
                      obj_list,           \
                      mod_objects[m],     \
                      use_objects[i],     \
                      "Continuous",       \
                      depth_list_use[m])

  # Plotting connections for call statements
  for i in range(len(call_objects)):
    call = call_objects[i].call
    for k in range(len(call)):
      called = call[k]
      for m in range(len(obj_list)):
        if called in obj_list[m].name:
          plot_spline(file,             \
                      obj_list,         \
                      call_objects[i],  \
                      obj_list[m],      \
                      "Dashed",         \
                      depth_list_call[i])

#===============================================================================
# Function to plot line
#
# Parameters:
#   - file:     Xfig file's handle
#   - x0:       first coordinate -> on x axis in centimeters
#   - y0:       first coordinate -> on y axis in centimeters
#   - x1:       second coordinate -> on x axis in centimeters
#   - y1:       second coordinate -> on y axis in centimeters
# Returns:
#   - nothing
# Used by:
#   - function for plotting grid
#-------------------------------------------------------------------------------
def plot_line(file, x0, y0, x1, y1):

  file.write("2 1 0 1 2 7 500 -1 -1 0.000 0 0 -1 0 0 2")

  file.write("\n%9d %9d" % ( (x0) * const_XFS,  \
                             (y0) * const_XFS))
  file.write("%9d %9d" %   ( (x1) * const_XFS,  \
                             (y1) * const_XFS))
  file.write("\n")

#===============================================================================
# Function to plot grid with coordinates for ROW BASED
#
# Parameters:
#   - file:         Xfig file's handle
#   - obj_list:     list of all objects
# Returns:
#   - nothing
# Used by:
#   - function for plotting everything (the entire graph)
#-------------------------------------------------------------------------------
def plot_grid(xf, obj_list):

  min_v = 0
  max_v = max(grid.x)
  min_h = 0
  max_h = max(grid.y)

  # Plot grid

  # Plot vertical lines
  for i in range(len(grid.x)):
    plot_line(xf, grid.x[i], min_h, grid.x[i], max_h)

  # Plot horizontal lines
  for j in range(len(grid.y)):
    plot_line(xf, min_v, grid.y[j], max_v, grid.y[j])

  # Plot coordinates of each spot in grid
  for i in range(len(grid.x)-1):
    for j in range(len(grid.y)-1):
      plot_text_right(xf, grid.x[i+1]-0.5, grid.y[j]+0.5,  \
                      "({}, {})".format(i, j))

#===============================================================================
# Function to plot module name box (module header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (module name)
#   - object:       object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - function for plotting module box
#-------------------------------------------------------------------------------
def plot_mod_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_mod_frame(file, x0, y0, box_width, const_UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, const_UBH, text)

#===============================================================================
# Function to plot subroutine name box (subroutine header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (subroutine name)
#   - object:       object to plot (subroutine)
# Returns:
#   - nothing
# Used by:
#   - function for plotting subroutine box
#-------------------------------------------------------------------------------
def plot_sub_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_sub_frame(file, x0, y0, box_width, const_UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, const_UBH, text)

#===============================================================================
# Function to plot function name box (function header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (function name)
#   - object:       object to plot (function)
# Returns:
#   - nothing
# Used by:
#   - function for plotting function box
#-------------------------------------------------------------------------------
def plot_fun_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_fun_frame(file, x0, y0, box_width, const_UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, const_UBH, text)

#===============================================================================
# Function to plot program name box (program header box)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         text to plot (program name)
#   - object:       object to plot (program)
# Returns:
#   - nothing
# Used by:
#   - function for plotting program box
#-------------------------------------------------------------------------------
def plot_prog_name(file, x0, y0, text, object):

  box_width = find_width(object)

  # Plot module framing box first
  plot_prog_frame(file, x0, y0, box_width, const_UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, const_UBH, text)

#===============================================================================
# Function to plot type statements (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting type statements box
#-------------------------------------------------------------------------------
def plot_type_stat_text_left(file, x0, y0, object):

  type_stat      = object.type_stat
  type_stat_len  = check_if_type_stat(object)
  box_width      = find_width(object)
  y_pos          = 0.25 + (y0 + const.FONT_SIZE    \
                 + (const_UBH-const.FONT_SIZE)*0.5)

  type_stat_num  = list(range(type_stat_len))

  if type_stat_len != 0:
    for i in range(type_stat_len):
      plot_text_left(file, x0, y_pos + type_stat_num[i], box_width,     \
                     const_UBH, type_stat[i], const.FONT_HEADER)

#===============================================================================
# Function to plot function type (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting function type box
#-------------------------------------------------------------------------------
def plot_fun_type_text_left(file, x0, y0, object):

  fun_type      = object.fun_type
  box_width     = find_width(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = type_stat_len + 0.25                                    \
                + (y0 + const.FONT_SIZE + (const_UBH-const.FONT_SIZE)*0.5)

  plot_text_left(file, x0, y_pos, box_width,            \
                 const_UBH, fun_type, const.FONT_NORMAL)

#===============================================================================
# Function to plot use statements (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting use statements box
#-------------------------------------------------------------------------------
def plot_use_text_left(file, x0, y0, \
                       use_list,     \
                       object):

  use_list_num  = list(range(len(use_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  box_width     = find_width(object)
  y_pos         = fun_type_len + type_stat_len + 0.25       \
                + (y0 + const.FONT_SIZE + (const_UBH-const.FONT_SIZE)*0.5)

  for i in range(len(use_list)):
    plot_text_left(file, x0, y_pos + use_list_num[i],       \
                   box_width, const_UBH, use_list[i], const.FONT_NORMAL)

#===============================================================================
# Function to plot variables (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting variable box
#-------------------------------------------------------------------------------
def plot_var_text_left(file, x0, y0, \
                       var_list,     \
                       use_list,     \
                       object):

  box_width     = find_width(object)
  var_list_num  = list(range(len(var_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = fun_type_len + use_len(use_list) + type_stat_len    \
                + 0.25 + (y0 + const.FONT_SIZE                        \
                + (const_UBH-const.FONT_SIZE)*0.5)

  for i in range(len(var_list)):
    plot_text_left(file, x0, y_pos + var_list_num[i],                 \
                   box_width, const_UBH, var_list[i], const.FONT_NORMAL)

#===============================================================================
# Function to plot methods (text)
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - meth_list:    list of methods
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - function for plotting methods box
#-------------------------------------------------------------------------------
def plot_meth_text_left(x0, y0, xf, \
                        var_list,   \
                        meth_list,  \
                        use_list,   \
                        object):

  if object.var == 0:
    var_list = []

  box_width     = find_width(object)
  meth_list_num = list(range(len(meth_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = fun_type_len + type_stat_len                         \
                + len(var_list) + use_len(use_list)                    \
                + (0.25 + (y0 + const.FONT_SIZE                        \
                + (const_UBH-const.FONT_SIZE)*0.5))

  for i in range(len(meth_list)):
    plot_text_left(xf, x0, y_pos + meth_list_num[i],                   \
                   box_width, const_UBH, meth_list[i], const.FONT_NORMAL)

#===============================================================================
# Function to plot type statements box with text
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_type_stat(file, x0, y0,   \
                   object):

  box_width = find_width(object)

  # Plot type statement framing box first
  plot_type_stat_frame(file, x0, y0, box_width, const_UBH, object)

  # Plot text
  plot_type_stat_text_left(file, x0, y0, object)

#===============================================================================
# Function to plot function type box with text
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_fun_type_name(file, x0, y0,   \
                       object):

  box_width = find_width(object)

  # Plot function type framing box first
  plot_fun_type_frame(file, x0, y0, box_width, const_UBH, object)

  # Plot text
  plot_fun_type_text_left(file, x0, y0, object)

#===============================================================================
# Function to plot use statements box with text
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_use_name(file, x0, y0, \
                  use_list,     \
                  object):

  box_width = find_width(object)

  # Plot use statements framing box first
  plot_use_frame(file, x0, y0, box_width, const_UBH, use_list, object)

  # Plot text
  plot_use_text_left(file, x0, y0, use_list, object)

#===============================================================================
# Function to plot variable box with text
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_var_name(file, x0, y0,       \
                  var_list,           \
                  use_list,           \
                  object):

  box_width = find_width(object)

  # Plot variable framing box first
  plot_var_frame(file, x0, y0, box_width, const_UBH, var_list, use_list, object)

  # Plot text
  plot_var_text_left(file, x0, y0, var_list, use_list, object)

#===============================================================================
# Function to plot methods box with text
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - var_list:     list of variables
#   - meth_list:    list of methods
#   - use_list:     list of use statements
#   - object:       object to plot
# Returns:
#   - nothing
# Used by:
#   - functions for plotting modules, subroutines and functions
#-------------------------------------------------------------------------------
def plot_meth_name(file, x0, y0,      \
                   var_list,          \
                   meth_list,         \
                   use_list,          \
                   object):

  box_width = find_width(object)

  # Plot methods framing box first
  plot_meth_frame(file, x0, y0, box_width, const_UBH,           \
                  var_list, meth_list, use_list, object)

  # Plot text
  plot_meth_text_left(x0, y0, file, var_list, meth_list, use_list, object)


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

#===============================================================================
# Find grid and object coordinates
#
# Parameters:
#   - obj_list:     list of all objects
# Returns:
#   - nothing
#-------------------------------------------------------------------------------
def find_coordinates(obj_list):

  # Grid coordinates
  n_row = 0
  n_col = 0
  for o in range(len(obj_list)):
    n_row = max(n_row, obj_list[o].row)
    n_col = max(n_col, obj_list[o].column)

  widths  = [0] * (n_col + 1)
  heights = [0] * (n_row + 1)
  grid.x  = [0] * (n_col + 2)
  grid.y  = [0] * (n_row + 2)

  for o in range(len(obj_list)):
    row = obj_list[o].row
    col = obj_list[o].column
    widths[col]  = max(widths [col], find_width (obj_list[o])  \
                 + attribute.box_margins * 2.0)
    heights[row] = max(heights[row], find_height(obj_list[o])  \
                 + attribute.box_margins * 2.0)

  for o in range(len(obj_list)):
    row = obj_list[o].row
    col = obj_list[o].column
    grid.x[col] = sum(widths [0:col])
    grid.y[row] = sum(heights[0:row])
  grid.x[n_col+1] = sum(widths)
  grid.y[n_row+1] = sum(heights)

  # Find object coordinates
  for o in range(len(obj_list)):
    row = obj_list[o].row
    col = obj_list[o].column
    xc = (grid.x[col] + grid.x[col+1]) * 0.5
    yc = (grid.y[row] + grid.y[row+1]) * 0.5
    obj_list[o].x0 = xc - obj_list[o].w * 0.5
    obj_list[o].y0 = yc - obj_list[o].h * 0.5
    obj_list[o].x1 = xc + obj_list[o].w * 0.5
    obj_list[o].y1 = yc + obj_list[o].h * 0.5

#===============================================================================
# Function to start definition of a compound in xfig
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         module name)
#   - object:       object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - plot_module
#-------------------------------------------------------------------------------
def plot_mod_start_compound(file, x0, y0, text, object):
  box_width  = find_width(object)
  box_height = find_height(object)

  file.write("6 %9d %9d %9d %9d\n" % (       \
     x0            *const_XFS - const_CMR,   \
     y0            *const_XFS - const_CMR,   \
    (x0+box_width) *const_XFS + const_CMR,   \
    (y0+box_height)*const_XFS + const_CMR))

#===============================================================================
# Function to end a compound in xfig
#
# Parameters:
#   - file:         Xfig file's handle
#   - x0:           object position on x axis in centimeters
#   - y0:           object position on y axis in centimeters
#   - text:         module name)
#   - object:       object to plot (module)
# Returns:
#   - nothing
# Used by:
#   - plot_module
#-------------------------------------------------------------------------------
def plot_mod_end_compound(file, x0, y0, text, object):
  file.write("-6\n")

