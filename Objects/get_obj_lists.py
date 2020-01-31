from Objects.classify_objects     import classify_objects
from Objects.module_objects       import module_objects
from Objects.program_objects      import program_objects
from Objects.subroutine_objects   import subroutine_objects
from Objects.function_objects     import function_objects
from Objects.place_objects_column import place_objects_column
from Objects.place_objects_row    import place_objects_row
from Objects.update_dimensions    import update_dimensions

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
def get_obj_lists(file_paths,             \
                  object_representation,  \
                  object_hierarchy,       \
                  align_boxes):

  mod_list  = module_objects (file_paths, [])         # list of all mod classes
  sub_list  = subroutine_objects (file_paths, mod_list)   # list of all sub classes
  fun_list  = function_objects (file_paths, mod_list)   # list of all fun classes
  prog_list = program_objects(file_paths, mod_list)   # list of all prog classes

  obj_list  = [*mod_list,   \
               *sub_list,   \
               *fun_list,   \
               *prog_list]               # list of all classes(mod+sub+fun+prog)

  obj_list, obj_memb  = classify_objects(obj_list)

  if object_representation == "Reduced":
    for o in range(len(obj_list)):
      obj_list[o].vars = []

  if object_representation == "Minimal":
    for o in range(len(obj_list)):
      obj_list[o].vars    = []
      obj_list[o].methods = []

  obj_list = update_dimensions(obj_list)

  if object_hierarchy == "Column-Based":
    obj_list = place_objects_column(obj_list, align_boxes)
  elif object_hierarchy == "Row-Based":
    obj_list = place_objects_row(obj_list, align_boxes)

  return obj_list, obj_memb

