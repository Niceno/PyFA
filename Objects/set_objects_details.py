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
def set_objects_details(obj_list, object_details):

  for o in range(len(obj_list)):
    obj_list[o].detail = object_details

  if object_details == "Reduced":
    for o in range(len(obj_list)):
      obj_list[o].vars = []

  if object_details == "Minimal":
    for o in range(len(obj_list)):
      obj_list[o].vars    = []
      obj_list[o].methods = []

  return obj_list

