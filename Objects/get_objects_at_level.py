from Objects.x_pos import x_pos

#===============================================================================
# Function for creating lists of objects at specific level
#  and updating x coordinates
#
# Parameters:
#   - obj_list:     list of objects
#   - lvl:          level
# Returns:
#   - list:         list of objects with updated x0 coordinate
# Used by:
#   - Function for creating lists of classes at specific level
#-------------------------------------------------------------------------------
def lvl_list(obj_list,lvl):

  list = []

  for i in range(len(obj_list)):
    if obj_list[i].level == lvl:
      list.append(obj_list[i])

  for i in range(len(list)):
    list[i].x0 = x_pos(list)[i]

  return list

