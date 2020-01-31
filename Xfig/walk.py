import math  # needed for sqrt

#===============================================================================
# Walk from one object to another, avoiding all objects in the graph
#
# Parameters:
#   - x1, y1, ... x6, y6:  coordinates the way Ivan introduced them
#   - obj_list:            list of all objects
# Returns:
#   - x, y:                coordinates with all steps from one object to another
#-------------------------------------------------------------------------------
def walk(x1, y1, x2, y2, x5, y5, x6, y6, obj_list, box_margins):

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

