import Xfig

#===============================================================================
# Function to create list with positions of objects on x axis
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - box_pos:      list of x axis coordinates for objects
# Used by:
#   - Function for creating lists of classes at specific level and updating
#-------------------------------------------------------------------------------
def x_pos(obj_list):

  # Create list with all box widths
  box_widths = [0] + []                       # initialize box_widths list
  for i in range(len(obj_list)):
    box = Xfig.find_width(obj_list[i])
    box_widths.append(box)                    # list of box widths of all boxes

  # Create new list for boxes to be parallel
  sum = 0
  box_pos = []
  for item in box_widths:
    sum += item + 1
    box_pos.append(sum)

  return box_pos

