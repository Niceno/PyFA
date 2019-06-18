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
  file.write("%5d %5d"   % ( x0       *450,  y0        *450))
  file.write("%5d %5d"   % ((x0+box_width)*450,  y0        *450))
  file.write("%5d %5d"   % ((x0+box_width)*450, (y0+box_height)*450))
  file.write("%5d %5d"   % ( x0       *450, (y0+box_height)*450))
  file.write("%5d %5d\n" % ( x0       *450,  y0        *450))

#===============================================================================
# Function to print frameless text
#-------------------------------------------------------------------------------
def plot_xfig_text_cm(file, x0, y0, box_width, box_height, text):

  file.write("4 1 0 50 -1 18 ")
  font_size = box_height * 0.5
  file.write("%3d" % (font_size * 36))    # font size
  file.write(" 0.0000 4 ")
  text_width  = 3                         # could be any value
  text_height = 3                         # could be any value
  file.write("%5d" % (text_height * 450)) # text height in xfig units
  file.write("%5d" % (text_width  * 450)) # text width in xfig units
  file.write("%5d %5d" % ( (x0+(box_width*0.5)) *450,  \
                           (y0+font_size+(box_height-font_size)*0.5)*450))
  file.write("%s%s\\001" % (" ", text))

#===============================================================================
# Function to print framed text
#-------------------------------------------------------------------------------
def plot_xfig_text_box_cm(file, x0, y0, box_width, box_height, text):

  # Plot framing box first
  plot_xfig_box_cm(file, x0, y0, box_width, box_height)

  # Plot text
  plot_xfig_text_cm(file, x0, y0, box_width, box_height, text)

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("Great program for extracting UML from Fortran.")

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
write_xfig_header(xf)

# Draw a text box
plot_xfig_text_box_cm(xf, 2, 2, 8, 1, "PROBA")

xf.close()
