from const import STARTING_LAYER_USE  as const_SLU
from const import STARTING_LAYER_CALL as const_SLC
from Xfig.plot_spline import plot_spline

#===============================================================================
# Function for plotting all spline connections
#
# Parameters:
#   - file:      Xfig file's handle
#   - obj_list:  list of all objects representing modules or subroutines
# Returns:
#   - nothing
# Used by:
#   - function for plotting everything (the entire graph) from object list
#-------------------------------------------------------------------------------
def plot_all_spline(file, obj_list):

  use_objects  = []
  mod_objects  = []
  call_objects = []

  # Getting list with only modules
  for i in range(len(obj_list)):
    if obj_list[i].type == "Module":
      mod_objects.append(obj_list[i])

  # Getting list with objects that have use statements
  for i in range(len(obj_list)):
    if obj_list[i].use != "None":
      use_objects.append(obj_list[i])

  # Getting list with objects that have call statements
  for i in range(len(obj_list)):
    if obj_list[i].call != 0:
      call_objects.append(obj_list[i])


  depth_list_use  = list(range(const_SLU,    \
                               const_SLU + len(mod_objects)))
  depth_list_call = list(range(const_SLC,    \
                               const_SLC + len(call_objects)))

  # Plotting connections for use statements
  for i in range(len(use_objects)):
    use = use_objects[i].use
    for k in range(len(use)):
      used = use[k]
      used = used.strip("use ")
      for m in range(len(mod_objects)):
        if used == mod_objects[m].name:
          plot_spline(file,               \
                      obj_list,           \
                      mod_objects[m],     \
                      use_objects[i],     \
                      "Continuous",       \
                      depth_list_use[m])

  # Plotting connections for call statements
  for i in range(len(call_objects)):
    call = call_objects[i].call
    for k in range(len(call)):
      called = call[k]
      for m in range(len(obj_list)):
        if called in obj_list[m].name:
          plot_spline(file,             \
                      obj_list,         \
                      call_objects[i],  \
                      obj_list[m],      \
                      "Dashed",         \
                      depth_list_call[i])

