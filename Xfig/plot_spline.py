import Const
from Xfig.walk import walk

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
def plot_spline(file, obj_list, object1, object2, line_type, depth,  \
                box_margins):

  # print("Connecting ", object1.name, "and", object2.name)

  offset = box_margins * 1.00

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
    y1 = object1.y0  \
       + Const.UNIT_BOX_HEIGHT * 0.5  # starts from the middle of header
  elif line_type == "Dashed":
    y1 = object1.y0  \
       + Const.UNIT_BOX_HEIGHT * 0.5  # starts from the middle of header

  # Second coordinate should be the same as first
  y2 = y1

  # Last coordinate for continous lines (use statements)
  if line_type == "Continuous":
    ind = object2.uses.index("use " + object1.name)
    y6 = object2.y0 + Const.UNIT_BOX_HEIGHT        \
                    + object2.N_Types()            \
                    + ind * Const.UNIT_BOX_HEIGHT  \
                    + 0.5 * Const.UNIT_BOX_HEIGHT

  # Last coordinate for dashed lines (call statements)
  elif line_type == "Dashed":
    y6 = object2.y0   \
       + Const.UNIT_BOX_HEIGHT * 0.5  # hits in the middle of the header

  # Penultimate coordinate should be the same as last
  y5 = y6

  # Walk!
  x, y = walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list, box_margins)

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
    file.write(" %9d %9d" % ( x[i] * Const.XFIG_SCALE,  \
                              y[i] * Const.XFIG_SCALE))
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

