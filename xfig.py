#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import finder
#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
XFS = 450              # xfig scale; xfig units for one cm
UBH = 0.75             # unit box height
THICKNESS = 2          # box line thickness
FONT_SIZE = UBH * 0.5  # font size depending on box height
#===============================================================================
# Function that returns list indexes
#-------------------------------------------------------------------------------
def list_num(lista):

  list_num_string = list(range(0,len(lista)))
  return list_num_string

#===============================================================================
# Return the code value of a Xfig font
#-------------------------------------------------------------------------------
def xfig_font_code(name):

  if name == "Courier":
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

  if name == "LtBlue":
    return 11
  elif name == "Pink2":
    return 28

#===============================================================================
# Choose the code value of a Xfig box color depending on header type
#-------------------------------------------------------------------------------

def choose_color(filename):

  sub_name = finder.get_sub(filename)
  module_name = finder.get_mod(filename)

  if len(module_name) != 0:
    color = "LtBlue"                 # LtBlue color for module
  elif len(module_name) == 0:
    color = "Pink2"                  # Pink2 color for subroutine

  return color


#===============================================================================
# Function to write xfig header
#-------------------------------------------------------------------------------
def write_header(file):

  file.write("#FIG 3.2  Produced by xfig version 3.2.6a\n")
  file.write("Landscape\n")
  file.write("Center\n")
  file.write("Metric\n")
  file.write("A4\n")
  file.write("100.00\n")
  file.write("Single\n")
  file.write("-2\n")
  file.write("1200 2\n")

#===============================================================================
# Function to plot box
#-------------------------------------------------------------------------------
def plot(file, x0, y0,      \
         module_name,       \
         var_list,          \
         meth_list,         \
         filename):

  # Draw a module text box
  plot_mod_name(file, x0, y0,     \
                module_name,      \
                filename)

  # Draw a variable text box
  plot_var_name(file, x0, y0,     \
                var_list,         \
                filename)

  # Draw a method text box
  plot_meth_name(file, x0, y0,    \
                 var_list,        \
                 meth_list,       \
                 filename)


#===============================================================================
# Function to plot an empty module frame
#-------------------------------------------------------------------------------
def plot_mod_frame(file, x0, y0, box_width, box_height, \
                   filename):

  file.write("2 2 0 ")
  file.write("%3d "       % THICKNESS)
  file.write("0")
  file.write("%3d "       % xfig_box_color(choose_color(filename)))
  file.write("50 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%5d %5d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%5d %5d\n" % ( x0           *XFS,  y0            *XFS))


#===============================================================================
# Function to plot an empty variable box depending on list length
#-------------------------------------------------------------------------------
def plot_var_frame(file, x0, y0, box_width, box_height, \
                   var_list):

  file.write("2 2 0 ")
  file.write("%3d"       % THICKNESS)
  file.write(" 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list))\
                                                 *XFS))
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height+len(var_list))\
                                                 *XFS))
  file.write("%5d %5d\n" % ( x0           *XFS, (y0+box_height)*XFS))

#===============================================================================
# Function to plot an empty method box depending on list length
#-------------------------------------------------------------------------------
def plot_meth_frame(file, x0, y0, box_width, box_height, \
                    var_list,                            \
                    meth_list):

  file.write("2 2 0 ")
  file.write("%3d"       % THICKNESS)
  file.write(" 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height+len(var_list))\
                                                                   *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list))\
                                                                   *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height+len(var_list) \
                                                 +len(meth_list))*XFS))
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height+len(var_list) \
                                                 +len(meth_list))*XFS))
  file.write("%5d %5d\n" % ( x0           *XFS, (y0+box_height+len(var_list))\
                                                                   *XFS))

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
  file.write("%5d %5d" % ( (x0+(box_width*0.5)) *XFS,  \
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
  file.write("%5d %5d" % ( (x0+          (box_height-FONT_SIZE)*0.5)*XFS,  \
                           (y0+FONT_SIZE+(box_height-FONT_SIZE)*0.5)*XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print module name
#-------------------------------------------------------------------------------
def plot_mod_name(file, x0, y0, text, filename):

  ubw = check_var(filename)

  # Plot module framing box first
  plot_mod_frame(file, x0, y0, ubw, UBH, filename)

  # Plot text
  plot_text_center_cm(file, x0, y0, ubw, UBH, text)


#===============================================================================
# Function to plot variables
#-------------------------------------------------------------------------------
def plot_var_text_left_cm(file, x0, y0, \
                          var_list,     \
                          filename):

  ubw = check_var(filename)
  var_list_num    = list_num(var_list)

  for i in range(len(var_list)):
    plot_text_left_cm(file, x0, 0.25+(y0+FONT_SIZE+(UBH-FONT_SIZE)*0.5) \
                      +var_list_num[i], ubw, UBH, var_list[i])


#===============================================================================
# Function to plot methods
#-------------------------------------------------------------------------------
  # Plot methods
def plot_meth_text_left_cm(x0, y0, xf, \
                           var_list,   \
                           meth_list,  \
                           filename):

  ubw = check_var(filename)
  meth_list_num    = list_num(meth_list)

  for i in range(len(meth_list)):
    plot_text_left_cm(xf, x0, 0.25+(y0+FONT_SIZE+(UBH-FONT_SIZE)*0.5) \
                      +len(var_list)+meth_list_num[i], ubw, UBH,      \
                       meth_list[i])

#===============================================================================
# Function to print variable box
#-------------------------------------------------------------------------------
def plot_var_name(file, x0, y0, \
                  var_list,     \
                  filename):

  ubw = check_var(filename)

  # Plot variable framing box first
  plot_var_frame(file, x0, y0, ubw, UBH, var_list)

  # Plot text
  plot_var_text_left_cm(file, x0, y0, var_list,filename)


#===============================================================================
# Function to print methods box
#-------------------------------------------------------------------------------
def plot_meth_name(file, x0, y0,      \
                   var_list,          \
                   meth_list,         \
                   filename):

  ubw = check_var(filename)

 # Plot methods framing box first
  plot_meth_frame(file, x0, y0, ubw, UBH, var_list, meth_list)

 # Plot text
  plot_meth_text_left_cm(x0, y0, file, var_list, meth_list,filename)


#===============================================================================
# Find box width depending on longest variable
#-------------------------------------------------------------------------------
def check_var(filename):

  list = finder.get_var(filename)
  longest_var = max(list, key=len)
  var_width = len(longest_var) / 3.7  # 3.7 gives the best ratio for width

  return var_width