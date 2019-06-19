#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import math

#===============================================================================
# Handy constants
#-------------------------------------------------------------------------------
XFS = 450   # xfig scale; xfig units for one cm
UBH = 0.75  # unit box height
UBW = 6.0   # unit box width

#===============================================================================
# Function to write xfig header
#-------------------------------------------------------------------------------
def write_xfig_header(file):
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
# Function to plot an empty box
#-------------------------------------------------------------------------------
def plot_xfig_box_cm(file, x0, y0, box_width, box_height):
  file.write("2 2 0 1 0 7 50 -1 -1 0.000 0 0 -1 0 0 5\n")
  file.write("%5d %5d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%5d %5d\n" % ( x0           *XFS,  y0            *XFS))

#===============================================================================
# Function to plot an empty module box
#-------------------------------------------------------------------------------
def plot_xfig_mod_box_cm(file, x0, y0, box_width, box_height):
  file.write("2 2 0 1 0 28 50 -1 20 0.000 0 0 -1 0 0 5\n")
  file.write("%5d %5d"   % ( x0           *XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS,  y0            *XFS))
  file.write("%5d %5d"   % ((x0+box_width)*XFS, (y0+box_height)*XFS))
  file.write("%5d %5d"   % ( x0           *XFS, (y0+box_height)*XFS))
  file.write("%5d %5d\n" % ( x0           *XFS,  y0            *XFS))

#===============================================================================
# Function to print centered frameless text
#-------------------------------------------------------------------------------
def plot_xfig_text_center_cm(file, x0, y0, box_width, box_height, text):

  file.write("4 1 0 50 -1 18 ")           # 18 is helvetica bold
  font_size = box_height * 0.5
  file.write("%3d" % (font_size * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%5d" % (text_height * XFS)) # text height in xfig units
  file.write("%5d" % (text_width  * XFS)) # text width in xfig units
  file.write("%5d %5d" % ( (x0+(box_width*0.5)) *XFS,  \
                           (y0+font_size+(box_height-font_size)*0.5)*XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print left aligned frameless text
#-------------------------------------------------------------------------------
def plot_xfig_text_left_cm(file, x0, y0, box_width, box_height, text):

  file.write("4 0 0 50 -1 16 ")           # 16 is helvetica
  font_size = box_height * 0.5
  file.write("%3d" % (font_size * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%5d" % (text_height * XFS)) # text height in xfig units
  file.write("%5d" % (text_width  * XFS)) # text width in xfig units
  file.write("%5d %5d" % ( (x0+          (box_height-font_size)*0.5)*XFS,  \
                           (y0+font_size+(box_height-font_size)*0.5)*XFS))
  file.write("%s%s\\001\n" % (" ", text))

#===============================================================================
# Function to print module name
#-------------------------------------------------------------------------------
def plot_xfig_mod_name_box_cm(file, x0, y0, box_width, box_height, text):

  # Plot module framing box first
  plot_xfig_mod_box_cm(file, x0, y0, box_width, box_height)

  # Plot text
  plot_xfig_text_center_cm(file, x0, y0, box_width, box_height, text)

#===============================================================================
# Function to print variable name
#-------------------------------------------------------------------------------
def plot_xfig_var_name_box_cm(file, x0, y0, box_width, box_height, text):

  # Plot text
  plot_xfig_text_left_cm(file, x0, y0, box_width, box_height, text)

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("Great program for extracting UML from Fortran.")


# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
write_xfig_header(xf)

# Draw a text box
plot_xfig_mod_name_box_cm(xf, 1, UBH,   UBW, UBH,   "Const_Mod")

plot_xfig_var_name_box_cm(xf, 1, UBH*2, UBW, UBH, "real :: x, y")
plot_xfig_var_name_box_cm(xf, 1, UBH*3, UBW, UBH, "character :: name")

xf.close()
