from Objects.place_objects_column import place_objects_column
from Objects.place_objects_row    import place_objects_row

#===============================================================================
# Function for creating complete and updated object list
#
# Parameters:
#   - file_paths:   paths to .f90 files
# Returns:
#   - obj_list:     list with all created and updated objects
# Used by:
#   - main program (simple.py)
#-------------------------------------------------------------------------------
def place_objects(obj_list,          \
                  object_hierarchy,  \
                  align_boxes):

  if object_hierarchy == "Column-Based":
    obj_list = place_objects_column(obj_list, align_boxes)

  elif object_hierarchy == "Row-Based":
    obj_list = place_objects_row(obj_list, align_boxes)

  return obj_list

