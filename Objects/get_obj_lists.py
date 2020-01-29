from Objects.classify_objects  import classify_objects
from Objects.mod_list_fun      import mod_list_fun
from Objects.prog_list_fun     import prog_list_fun
from Objects.sub_list_fun         import sub_list_fun
from Objects.fun_list_fun         import fun_list_fun
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

  mod_list  = mod_list_fun(file_paths)   # list of all mod classes
  sub_list  = sub_list_fun(file_paths)   # list of all sub classes
  fun_list  = fun_list_fun(file_paths)   # list of all fun classes
  prog_list = prog_list_fun(file_paths)  # list of all prog classes
  obj_list  = [*mod_list,   \
               *sub_list,   \
               *fun_list,   \
               *prog_list]               # list of all classes(mod+sub+fun+prog)

  obj_list, obj_memb  = classify_objects(obj_list)

  if object_representation == "Reduced":
    for o in range(len(obj_list)):
      obj_list[o].var = 0

  if object_representation == "Minimal":
    for o in range(len(obj_list)):
      obj_list[o].var  = 0
      obj_list[o].meth = 0

  obj_list = update_dimensions(obj_list)

  if object_hierarchy == "Column-Based":
    obj_list = place_objects_column(obj_list, align_boxes)
  elif object_hierarchy == "Row-Based":
    obj_list = place_objects_row(obj_list, align_boxes)

  return obj_list, obj_memb

