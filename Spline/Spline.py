import math  # needed for sqrt
import Const

class Spline():

  def __init__(self, obj1, obj2, line, deep):

    self.object1   = obj1
    self.object2   = obj2
    self.line_type = line
    self.depth     = deep

    self.x = []
    self.y = []

  def N_Points(self):
    return len(self.x)

#===============================================================================
# Walk from one object to another, avoiding all objects in the graph
#
# Parameters:
#   - x1, y1, ... x6, y6:  coordinates the way Ivan introduced them
#   - obj_list:            list of all objects
# Returns:
#   - x, y:                coordinates with all steps from one object to another
#-------------------------------------------------------------------------------
def Walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list, box_margins):

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
  for i in range(0, 1024):

    #--------------------------   3 2 1
    # Set eight possible direc    4 c 0
    #--------------------------   5 6 7
    step_x    = []
    step_y    = []
    step_dist = []

    stride = box_margins * 0.45

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
    if dist[-1] < (box_margins * 0.5):
      x = x[:-2]
      y = y[:-2]
      break

    # Check if it wobbles (only if you are close)
    if len(dist) > 2:   # WARNING: GHOST NUMBER
      if dist[-1] < (box_margins):
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
def Connect(obj_list, object1, object2, line_type, depth,  \
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

  # Create a new spline object and walk!
  spline = Spline(object1.name, object2.name, line_type, depth)

  spline.x,  \
  spline.y = Walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list, box_margins)

  return spline
