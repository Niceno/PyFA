#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import finder
import browse
import attribute
#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
XFS                     = 450             # xfig scale; xfig units for one cm
UBH                     = 0.75            # unit box height
THICKNESS               = 2               # box line thickness
FONT_SIZE               = UBH * 0.5       # font size depending on box height
FONT_HEADER             = "Courier-Bold"  # font for headers
FONT_NORMAL             = "Courier"       # font for everything else
COLOR_BOX               = "White"         # color of var,meth and use boxes
COLOR_HEADER_MODULE     = "LtBlue"        # color of module header
COLOR_HEADER_SUBROUTINE = "Pink2"         # color of subroutine header
COLOR_HEADER_FUNCTION   = "Yellow"        # color of function header
COLOR_HEADER_PROGRAM    = "Green2"        # color of program header
OBJECT_REPRESENTATION   = "Normal"        # "Compresssed"
OBJECT_HIERARCHY        = "Row-Based"     # "Column-Based"

#===============================================================================
# Function to choose use statements list length
#
# Parameters:
#   - list:  list of use statements
# Returns:
#   - use_list_len:  number of use statements, zero if none
# Used by:
#   - Functions which plot frames, to determine box height
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
#   - Functions which plot frames, to determine box height
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
#   - Functions which plot frames, to determine box height
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
#   - Functions which plot text
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
#   - Functions which plot frames
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
# Choose box width depending on longest string
#
# Parameters:
#   - filename:   name of the Fortran file being read (.f90)
# Returns:
#   - var_width:  box width in Xfig drawing units
# Used by:
#   - Functions which plot boxes
# Warning:
#   - Uses ghost parameter 0.4 to convert width from characters to Xfig units
#-------------------------------------------------------------------------------
def choose_width(filename):

  var_list     = filename.var
  meth_list    = filename.meth
  header_name  = filename.name
  use_list     = filename.use

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

  var_length      = max(var_list,  key=len)
  meth_length     = max(meth_list, key=len)
  use_length      = max(use_list,  key=len)
  fun_type_length = max(fun_type,  key=len)

  lengths = [len(var_length), len(meth_length), \
             len(header_name),len(use_length),  \
             len(fun_type_length)]

  box_width = max(lengths)
  box_width = box_width * UBH * 0.4  # gives the best ratio for width

  return box_width

#===============================================================================
# Function to write xfig header
#
# Parameters:
#   - file:  Xfig file's handle
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

  # Plot a variable text box
  plot_var_name(file, x0, y0,     \
                var_list,         \
                use_list,         \
                object)

  # Plot a method text box
  plot_meth_name(file, x0, y0,    \
                 var_list,        \
                 meth_list,       \
                 use_list,        \
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
                    program_name,      \
                    use_list,          \
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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_HEADER_MODULE))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS,  y0            *XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_HEADER_SUBROUTINE))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS,  y0            *XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_HEADER_FUNCTION))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS,  y0            *XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_HEADER_PROGRAM))
  file.write("15 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS,  y0            *XFS))

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
    color = COLOR_HEADER_MODULE
  if object.type == "Subroutine":
    color = COLOR_HEADER_SUBROUTINE
  if object.type == "Function":
    color = COLOR_HEADER_FUNCTION
  if object.type == "Program":
    color = COLOR_HEADER_PROGRAM

  file.write("2 2 0 ")
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(color))
  file.write("11 -1 30 0.000 0 0 -1 0 0 5\n")         # 30*5 = 150% intensity
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS, (y0+box_height)*XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_BOX))
  file.write("11 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height           \
                                                +fun_type_len            \
                                                +type_stat_len)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height           \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS, (y0+box_height)*XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_BOX))
  file.write("12 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height          \
                                                 +use_len(use_list)     \
                                                 +fun_type_len          \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height          \
                                                 +use_len(use_list)     \
                                                 +fun_type_len          \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS, (y0+box_height)*XFS))

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
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_BOX))
  file.write("14 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height            \
                                                 +len(var_list)           \
                                                 +use_len(use_list)       \
                                                 +fun_type_len            \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height            \
                                                 +len(var_list)           \
                                                 +use_len(use_list)       \
                                                 +fun_type_len            \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS, (y0+box_height)*XFS))

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

  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)

  file.write("2 2 0 ")
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(COLOR_BOX))
  file.write("13 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height           \
                                                 +len(var_list)          \
                                                 +use_len(use_list)      \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height           \
                                                 +len(var_list)          \
                                                 +use_len(use_list)      \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ((x0+box_width)*XFS, (y0+box_height           \
                                                 +len(var_list)          \
                                                 +len(meth_list)         \
                                                 +use_len(use_list)      \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d"   % ( x0           *XFS, (y0+box_height           \
                                                 +len(var_list)          \
                                                 +len(meth_list)         \
                                                 +use_len(use_list)      \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))
  file.write("%9d %9d\n" % ( x0           *XFS, (y0+box_height           \
                                                 +len(var_list)          \
                                                 +use_len(use_list)      \
                                                 +fun_type_len           \
                                                 +type_stat_len)*XFS))

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

  file.write("4 1 0 10 -1 ")              # 45 is depth
  file.write("%5d" % xfig_font_code(FONT_HEADER))
  file.write("%3d" % (FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%9d" % (text_height * XFS)) # text height in xfig units
  file.write("%9d" % (text_width  * XFS)) # text width in xfig units
  file.write("%9d %9d" % ( (x0+(box_width*0.5)) *XFS,  \
                           (y0+FONT_SIZE+(box_height-FONT_SIZE)*0.5)*XFS))
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

  file.write("4 0 0 10 -1 ")              # 45 is depth
  file.write("%5d" % xfig_font_code(font))
  file.write("%3d" % (FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%9d" % (text_height * XFS)) # text height in xfig units
  file.write("%9d" % (text_width  * XFS)) # text width in xfig units
  file.write("%9d %9d" % ( (x0+          (box_height-FONT_SIZE)*0.5)*XFS,  \
                           (y0+FONT_SIZE+(box_height-FONT_SIZE)*0.5)*XFS))
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

  file.write("4 2 2 500 -1 ")               # 45 is depth
  file.write("%5d" % xfig_font_code(FONT_NORMAL))
  file.write("%3d" % (FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%9d" % (text_height * XFS)) # text height in xfig units
  file.write("%9d" % (text_width  * XFS)) # text width in xfig units
  file.write("%9d %9d" % ( (x0)*XFS,  \
                           (y0)*XFS))
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
def plot_spline(file, object1, object2, depth):

  use_list = object2.use

  # First coordinate at half of the box
  x1 = object1.x1
  y1 = (object1.y0 + object1.y1)/2

  # Last coordinate
  x6 = object2.x0
  y6 = object2.y0 + UBH + check_if_type_stat(object2) + len(use_list)/2

  # Second coordinate
  x2 = x1 + 2
  y2 = y1

  # Third coordinate
  x3 = object1.x1 + 3
  y3 = object1.y1

  # Fourth coordinate
  x4 = object2.x0 - 3
  y4 = object2.y0

  # Fifth coordinate
  x5 = x6 - 2
  y5 = y6

  file.write("3 2 0 2 0 7 ")
  file.write("%5d" % (depth))
  file.write(" -1 -1 0.000 0 1 1 6")                   # 6 --> number of points

  file.write("\n 1 1 1.00 135.00 180.00")              # arrow settings
  file.write("\n 6 1 1.00 135.00 180.00")              # arrow settings

  file.write("\n%9d %9d" % ( (x1) *XFS,  \
                             (y1)*XFS))
  file.write("%9d %9d" %   ( (x2) *XFS,  \
                             (y2)*XFS))
  file.write("%9d %9d" %   ( (x3) *XFS,  \
                             (y3)*XFS))
  file.write("%9d %9d" %   ( (x4) *XFS,  \
                             (y4)*XFS))
  file.write("%9d %9d" %   ( (x5) *XFS,  \
                             (y5)*XFS))
  file.write("%9d %9d" %   ( (x6) *XFS,  \
                             (y6)*XFS))

  file.write("\n 0.000 1.000 1.000 1.000 1.000 0.000\n")

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
def plot_dashed_spline(file, object1, object2, depth):

  # First coordinate
  x1 = object1.x1
  y1 = (object1.y0 + object1.y1)/2

  # Last coordinate
  x6 = object2.x0
  y6 = object2.y0 + UBH/2

  # Second coordinate
  x2 = x1 + 2
  y2 = y1

  # Third coordinate
  x3 = object1.x1 + 3
  y3 = object1.y0

  # Fourth coordinate
  x4 = object2.x0 - 3
  y4 = object2.y1

  # Fifth coordinate
  x5 = x6 - 2
  y5 = y6

  file.write("3 2 1 2 0 7 ")
  file.write("%5d" % (depth))
  file.write(" -1 -1 8.000 0 1 1 6")                   # 6 --> number of points
                                                       # 8 --> dash length

  file.write("\n 1 0 1.00 135.00 180.00")              # arrow settings
  file.write("\n 6 0 1.00 135.00 180.00")              # arrow settings

  file.write("\n%9d %9d" % ( (x1) *XFS,  \
                             (y1)*XFS))
  file.write("%9d %9d" %   ( (x2) *XFS,  \
                             (y2)*XFS))
  file.write("%9d %9d" %   ( (x3) *XFS,  \
                             (y3)*XFS))
  file.write("%9d %9d" %   ( (x4) *XFS,  \
                             (y4)*XFS))
  file.write("%9d %9d" %   ( (x5) *XFS,  \
                             (y5)*XFS))
  file.write("%9d %9d" %   ( (x6) *XFS,  \
                             (y6)*XFS))

  file.write("\n 0.000 1.000 1.000 1.000 1.000 0.000\n")

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


  depth_list_use = list(range(101,101+len(mod_objects)))   # depths for modules
  depth_list_call = list(range(201,201+len(call_objects))) # depths for calls

  # Plotting connections for use statements
  for i in range(len(use_objects)):
    use = use_objects[i].use
    for k in range(len(use)):
      used = use[k]
      used = used.strip("use ")
      for m in range(len(mod_objects)):
        if used == mod_objects[m].name:
          plot_spline(file, mod_objects[m],use_objects[i], depth_list_use[m])

  # Plotting connections for call statements
  for i in range(len(call_objects)):
    call = call_objects[i].call
    for k in range(len(call)):
      called = call[k]
      for m in range(len(obj_list)):
        if called in obj_list[m].name:
          plot_dashed_spline(file, call_objects[i],            \
                             obj_list[m], depth_list_call[i])

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

  file.write("\n%9d %9d" % ( (x0) *XFS,  \
                             (y0)*XFS))
  file.write("%9d %9d" %   ( (x1) *XFS,  \
                             (y1)*XFS))
  file.write("\n")

#===============================================================================
# Function to plot grid with coordinates
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

  width   = attribute.max_width(obj_list)  + 2      # height of each grid spot
  height  = attribute.max_height(obj_list) + 2      # width of each grid spot
  max_lvl = attribute.find_max_lvl(obj_list)        # max level

  width_list    = []
  height_list   = []
  list_lvl      = []

  # List with widths (columns)
  for i in range(len(obj_list)):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(max_lvl + 15):
    heights = height * i
    height_list.append(heights)


  for i in range(0,len(obj_list)):
    for l in range(0,max_lvl+1):
       if obj_list[i].level == l:
          list_lvl.append(obj_list[i].level)
  max_element = max(list_lvl,key=list_lvl.count)
  occurances_of_max = list_lvl.count(max_element)

  width_list  = width_list[:(occurances_of_max + max_lvl + 2)]
  height_list = height_list[:max_lvl + 2]

  min_v = 0
  max_v = max(width_list)
  min_h = 0
  max_h = max(height_list)

 # Plot grid

  # Plot vertical lines
  for i in range(0,len(width_list)):
    plot_line(xf, width_list[i], min_h, width_list[i], max_h)

  # Plot horizontal lines
  for i in range(0,len(height_list)):
    plot_line(xf, min_v, height_list[i], max_v, height_list[i])

  # Plot coordinates of each spot in grid
  for column in range(0,len(width_list)-1):
    for row in range(0,len(height_list)-1):
      plot_text_right(xf, width_list[column]+width-0.5, height_list[row]+1,  \
                      "({}, {})".format(row, column))

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

  box_width = choose_width(object)

  # Plot module framing box first
  plot_mod_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, UBH, text)

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

  box_width = choose_width(object)

  # Plot module framing box first
  plot_sub_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, UBH, text)

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

  box_width = choose_width(object)

  # Plot module framing box first
  plot_fun_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, UBH, text)

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

  box_width = choose_width(object)

  # Plot module framing box first
  plot_prog_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center(file, x0, y0, box_width, UBH, text)

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
  box_width      = choose_width(object)
  y_pos          = 0.25 + (y0 + FONT_SIZE + (UBH-FONT_SIZE)*0.5)

  type_stat_num  = list(range(0,type_stat_len))

  if type_stat_len != 0:
    for i in range(type_stat_len):
      plot_text_left(file, x0, y_pos + type_stat_num[i],       \
                     box_width, UBH, type_stat[i], FONT_HEADER)

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
  box_width     = choose_width(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = type_stat_len + 0.25 + (y0 + FONT_SIZE + (UBH-FONT_SIZE)*0.5)

  plot_text_left(file, x0, y_pos, box_width, UBH, fun_type, FONT_NORMAL)

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

  use_list_num  = list(range(0,len(use_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  box_width     = choose_width(object)
  y_pos         = fun_type_len + type_stat_len + 0.25       \
                + (y0 + FONT_SIZE + (UBH-FONT_SIZE)*0.5)

  for i in range(len(use_list)):
    plot_text_left(file, x0, y_pos + use_list_num[i],       \
                   box_width, UBH, use_list[i], FONT_NORMAL)

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

  box_width     = choose_width(object)
  var_list_num  = list(range(0,len(var_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = fun_type_len + use_len(use_list) + type_stat_len    \
                + 0.25 + (y0 + FONT_SIZE + (UBH-FONT_SIZE)*0.5)

  for i in range(len(var_list)):
    plot_text_left(file, x0, y_pos + var_list_num[i],                 \
                   box_width, UBH, var_list[i], FONT_NORMAL)

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

  box_width     = choose_width(object)
  meth_list_num = list(range(0,len(meth_list)))
  fun_type_len  = check_if_function(object)
  type_stat_len = check_if_type_stat(object)
  y_pos         = fun_type_len + type_stat_len                         \
                + len(var_list) + use_len(use_list)                    \
                + (0.25 + (y0 + FONT_SIZE + (UBH-FONT_SIZE)*0.5))

  for i in range(len(meth_list)):
    plot_text_left(xf, x0, y_pos + meth_list_num[i],                   \
                   box_width, UBH, meth_list[i], FONT_NORMAL)

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

  box_width = choose_width(object)

  # Plot type statement framing box first
  plot_type_stat_frame(file, x0, y0, box_width, UBH, object)

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

  box_width = choose_width(object)

  # Plot function type framing box first
  plot_fun_type_frame(file, x0, y0, box_width, UBH, object)

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

  box_width = choose_width(object)

  # Plot use statements framing box first
  plot_use_frame(file, x0, y0, box_width, UBH, use_list, object)

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

  box_width = choose_width(object)

  # Plot variable framing box first
  plot_var_frame(file, x0, y0, box_width, UBH, var_list, use_list, object)

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

  box_width = choose_width(object)

 # Plot methods framing box first
  plot_meth_frame(file, x0, y0, box_width, UBH,           \
                  var_list, meth_list, use_list, object)

 # Plot text
  plot_meth_text_left(x0, y0, file, var_list, meth_list, use_list, object)
