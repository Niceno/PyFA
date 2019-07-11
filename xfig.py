#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import finder
import browse
import attribute
#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
XFS       = 450              # xfig scale; xfig units for one cm
UBH       = 0.75             # unit box height
THICKNESS = 2                # box line thickness
FONT_SIZE = UBH * 0.5        # font size depending on box height

#===============================================================================
# Function that returns list indexes
#-------------------------------------------------------------------------------
def list_num(lista):

  list_num_string = list(range(0,len(lista)))
  return list_num_string

#===============================================================================
# Function to choose use statements list length
#-------------------------------------------------------------------------------
def use_len(list):
  if list != 0:
    # Draw a use text box
    use_list_len = len(list)
  else:
    use_list_len = 0
  return use_list_len

#===============================================================================
# Return the code value of a Xfig font
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
# Return the code value of a Xfig box color (not needed)
#-------------------------------------------------------------------------------
def xfig_box_color(name):

  if name   == "LtBlue":
    return 11
  elif name == "Pink2":
    return 28

#===============================================================================
# Choose box width depending on longest string
#-------------------------------------------------------------------------------
def choose_width(filename):

  var_list    = finder.get_var(filename)
  meth_list   = finder.get_meth(filename)
  header_name = finder.get_header(filename)
  use_list    = finder.get_use(filename)

  if use_list == 0:
    use_list = ["0"]
  else:
    use_list = use_list

  var_length    = max(var_list, key=len)
  meth_length   = max(meth_list, key=len)
  use_length    = max(use_list, key=len)

  lengths   = [len(var_length), len(meth_length), \
               len(header_name),len(use_length)]

  var_width = max(lengths)
  var_width = var_width *0.32  #  gives the best ratio for width

  return var_width

#===============================================================================
# Function to return list with positions on x axis(without strategy for now)
#-------------------------------------------------------------------------------
def x_pos(files):

  # Create list with all box widths

  box_widths = [0] + []                       # initialize box_widths list
  for i in range(len(files)):
    box = choose_width(files[i])
    box_widths.append(box)                    # list of box widths of all boxes

  # Create new list for boxes to be parallel

  sum = 0
  box_pos = []
  for item in box_widths:
    sum += item + 1
    box_pos.append(sum)

  return box_pos

#===============================================================================
# Function to write xfig header
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
# Choose which one to plot (module or subroutine)
#-------------------------------------------------------------------------------
def plot(file, x0, y0,      \
         filename):

  module     = finder.get_mod(filename)       # module name
  subroutine = finder.get_sub(filename)       # subroutine name
  use_list   = finder.get_use(filename)       # use list

  # Module definition has been found, hence length is greater than zero
  if subroutine == 0:
    var_list  = finder.get_var(filename)
    meth_list = finder.get_meth(filename)
    use_list  = finder.get_use(filename)
    module_name = module

    plot_module(file, x0, y0,          \
                module_name,           \
                var_list,              \
                meth_list,             \
                use_list,              \
                filename)

  # Module defintion has not been found, hence it is a subroutine
  elif subroutine != 0:
    var_list    = finder.get_var(filename)
    module_name = subroutine
    plot_subroutine(file, x0, y0,      \
                    module_name,       \
                    var_list,          \
                    use_list,          \
                    filename)

#===============================================================================
# Function to plot module box
#-------------------------------------------------------------------------------
def plot_module(file, x0, y0,      \
         module_name,              \
         var_list,                 \
         meth_list,                \
         use_list,                 \
         filename):

  # Draw a module text box
  plot_mod_name(file, x0, y0,     \
                module_name,      \
                filename)

  if use_list != 0:
    # Draw a use text box
    plot_use_name(file, x0, y0,     \
                  use_list,         \
                  filename)
  else:
    use_list = 0


  # Draw a variable text box
  plot_var_name(file, x0, y0,     \
                var_list,         \
                use_list,         \
                filename)

  # Draw a method text box
  plot_meth_name(file, x0, y0,    \
                 var_list,        \
                 meth_list,       \
                 use_list,        \
                 filename)

#===============================================================================
# Function to plot subroutine box
#-------------------------------------------------------------------------------
def plot_subroutine(file, x0, y0,      \
                    module_name,       \
                    var_list,          \
                    use_list,          \
                    filename):

  # Draw a module text box
  plot_sub_name(file, x0, y0,     \
                module_name,      \
                filename)

  # Choose if use box exist
  if use_list != 0:
    # Draw a use text box
    plot_use_name(file, x0, y0,     \
                  use_list,         \
                  filename)
  else:
    use_list = 0

 # Draw a variable text box
  plot_var_name(file, x0, y0,     \
                var_list,         \
                use_list,         \
                filename)

#===============================================================================
# Function to plot an empty module frame
#-------------------------------------------------------------------------------
def plot_mod_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color("LtBlue"))
  file.write("50 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%7d %7d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%7d %7d\n" % ( x0           *XFS,  y0            *XFS))

#===============================================================================
# Function to plot an empty module frame
#-------------------------------------------------------------------------------
def plot_sub_frame(file, x0, y0, box_width, box_height):

  file.write("2 2 0 ")
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color("Pink2"))
  file.write("50 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%7d %7d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%7d %7d\n" % ( x0           *XFS,  y0            *XFS))


#===============================================================================
# Function to plot an empty use statements box depending on list length
#-------------------------------------------------------------------------------
def plot_use_frame(file, x0, y0, box_width, box_height, \
                   use_list):

  use_list_len = use_len(use_list)


  file.write("2 2 0 ")
  file.write("%3d"       % THICKNESS)
  file.write(" 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height+use_list_len) \
                                                 *XFS))
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height+use_list_len) \
                                                 *XFS))
  file.write("%7d %7d\n" % ( x0           *XFS, (y0+box_height)*XFS))


#===============================================================================
# Function to plot an empty variable box depending on list length
#-------------------------------------------------------------------------------
def plot_var_frame(file, x0, y0, box_width, box_height, \
                   var_list,                            \
                   use_list):

  use_list_len = use_len(use_list)

  file.write("2 2 0 ")
  file.write("%3d"       % THICKNESS)
  file.write(" 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list) \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height+len(var_list) \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d\n" % ( x0           *XFS, (y0+box_height)*XFS))

#===============================================================================
# Function to plot an empty method box depending on list length
#-------------------------------------------------------------------------------
def plot_meth_frame(file, x0, y0, box_width, box_height, \
                    var_list,                            \
                    meth_list,                           \
                    use_list):


  use_list_len = use_len(use_list)

  file.write("2 2 0 ")
  file.write("%3d"       % THICKNESS)
  file.write(" 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height+len(var_list) \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list) \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list) \
                                                 +len(meth_list)             \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d"   % ( x0           *XFS, (y0+box_height+len(var_list) \
                                                 +len(meth_list)             \
                                                 +use_list_len)*XFS))
  file.write("%7d %7d\n" % ( x0           *XFS, (y0+box_height+len(var_list) \
                                                 +use_list_len)*XFS))

#===============================================================================
# Function to print centered frameless text
#-------------------------------------------------------------------------------
def plot_text_center_cm(file, x0, y0, box_width, box_height, text):

  file.write("4 1 0 45 -1 ")              # 45 is depth
  file.write("%5d" % xfig_font_code("Helvetica-Bold"))
  file.write("%3d" % (FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%5d" % (text_height * XFS)) # text height in xfig units
  file.write("%5d" % (text_width  * XFS)) # text width in xfig units
  file.write("%7d %7d" % ( (x0+(box_width*0.5)) *XFS,  \
                           (y0+FONT_SIZE+(box_height-FONT_SIZE)*0.5)*XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print left aligned frameless text
#-------------------------------------------------------------------------------
def plot_text_left_cm(file, x0, y0, box_width, box_height, text):

  file.write("4 0 0 45 -1 ")              # 45 is depth
  file.write("%5d" % xfig_font_code("Helvetica"))
  file.write("%3d" % (FONT_SIZE * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%5d" % (text_height * XFS)) # text height in xfig units
  file.write("%5d" % (text_width  * XFS)) # text width in xfig units
  file.write("%7d %7d" % ( (x0+          (box_height-FONT_SIZE)*0.5)*XFS,  \
                           (y0+FONT_SIZE+(box_height-FONT_SIZE)*0.5)*XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print module name
#-------------------------------------------------------------------------------
def plot_mod_name(file, x0, y0, text, filename):

  box_width = choose_width(filename)

  # Plot module framing box first
  plot_mod_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center_cm(file, x0, y0, box_width, UBH, text)


#===============================================================================
# Function to print subroutine name
#-------------------------------------------------------------------------------
def plot_sub_name(file, x0, y0, text, filename):

  box_width = choose_width(filename)

  # Plot module framing box first
  plot_sub_frame(file, x0, y0, box_width, UBH)

  # Plot text
  plot_text_center_cm(file, x0, y0, box_width, UBH, text)


#===============================================================================
# Function to plot use statements
#-------------------------------------------------------------------------------
def plot_use_text_left_cm(file, x0, y0, \
                          use_list,     \
                          filename):

  box_width    = choose_width(filename)
  use_list_num = list_num(use_list)

  for i in range(len(use_list)):
    plot_text_left_cm(file, x0, 0.25+(y0+FONT_SIZE+(UBH-FONT_SIZE)*0.5) \
                      +use_list_num[i], box_width, UBH, use_list[i])

#===============================================================================
# Function to plot variables
#-------------------------------------------------------------------------------
def plot_var_text_left_cm(file, x0, y0, \
                          var_list,     \
                          use_list,     \
                          filename):

  box_width    = choose_width(filename)
  var_list_num = list_num(var_list)
  use_list_len = use_len(use_list)

  for i in range(len(var_list)):
    plot_text_left_cm(file, x0, (0.25+(y0+FONT_SIZE+(UBH-FONT_SIZE)*0.5)   \
                      +use_list_len) +var_list_num[i],                     \
                      box_width, UBH, var_list[i])



#===============================================================================
# Function to plot methods
#-------------------------------------------------------------------------------
  # Plot methods
def plot_meth_text_left_cm(x0, y0, xf, \
                           var_list,   \
                           meth_list,  \
                           use_list,   \
                           filename):

  box_width     = choose_width(filename)
  meth_list_num = list_num(meth_list)
  use_list_len  = use_len(use_list)

  for i in range(len(meth_list)):
    plot_text_left_cm(xf, x0, (0.25+(y0+FONT_SIZE+(UBH-FONT_SIZE)*0.5)   \
                      +len(var_list)+use_list_len+meth_list_num[i]),     \
                      box_width, UBH, meth_list[i])

#===============================================================================
# Function to print use statements box
#-------------------------------------------------------------------------------
def plot_use_name(file, x0, y0, \
                  use_list,     \
                  filename):

  box_width = choose_width(filename)

  # Plot variable framing box first
  plot_use_frame(file, x0, y0, box_width, UBH, use_list)

  # Plot text
  plot_use_text_left_cm(file, x0, y0, use_list, filename)


#===============================================================================
# Function to print variable box
#-------------------------------------------------------------------------------
def plot_var_name(file, x0, y0,       \
                  var_list,           \
                  use_list,           \
                  filename):

  box_width = choose_width(filename)

  # Plot variable framing box first
  plot_var_frame(file, x0, y0, box_width, UBH, var_list, use_list)

  # Plot text
  plot_var_text_left_cm(file, x0, y0, var_list, use_list, filename)


#===============================================================================
# Function to print methods box
#-------------------------------------------------------------------------------
def plot_meth_name(file, x0, y0,      \
                   var_list,          \
                   meth_list,         \
                   use_list,          \
                   filename):

  box_width = choose_width(filename)

 # Plot methods framing box first
  plot_meth_frame(file, x0, y0, box_width, UBH, var_list, meth_list, use_list)

 # Plot text
  plot_meth_text_left_cm(x0, y0, file, var_list, meth_list, use_list, filename)
