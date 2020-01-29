from Objects.find_max_lvl import find_max_lvl
from Objects.lvl_list     import lvl_list

#===============================================================================
# Function for creating grid and updating coordinates - (Column-Based hierarchy)
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - updated_list: list of objects with updated coordinates (plotting in grid)
# Used by:
#   - Function for creating complete and updated file list
#===============================================================================
def place_objects_column(obj_list, align_boxes):

  max_lvl = find_max_lvl(obj_list)               # max level

  lvl_lista    = []
  updated_list = []

  # List of lists of levels
  for i in range(max_lvl + 2):
    lvl = lvl_list(obj_list,i)
    lvl_lista.append(lvl)

  # Assign values to coordinates
  for i in range(len(lvl_lista)):
    lista = lvl_lista[i]
    # Choose alignment
    if align_boxes == "Diagonal":
      column = i
    elif align_boxes == "Left":
      column = 0

    for l in range(len(lvl_lista[i])):

      lista[l].column = i
      lista[l].row    = l+column

      updated_list.append(lista[l])

  return updated_list
