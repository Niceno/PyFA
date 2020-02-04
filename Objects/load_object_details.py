import sys
from Objects.update_box_ij_pos import update_box_ij_pos

#===============================================================================
# Function for searching coordinates in .ij file and update them
#
# Parameters:
#   - file_with_names:  file with names and coordinates
#   - obj_list:         list of objects
# Returns:
#   - obj_list:         list of objects with updated placements in grid
# Used by:
#   - main program (function for changing object placement in grid)
#===============================================================================
def load_object_details(file_with_names, obj_list):

  list = obj_list
  try: myfile = open(file_with_names, 'rt')
  except:
    print("File", file_with_names, "can't be found!  Exiting")
    sys.exit()

  with myfile:
    for line in myfile:
      if not line.startswith("#"):
        data = line.split(";")
        name   = data[0].strip("\n").strip(" ")
        detail = data[1].strip("\n").strip(" ")
        for o in range(len(obj_list)):
          if obj_list[o].name == name:
            obj_list[o].detail = detail
  myfile.close()

  for o in range(len(obj_list)):
    if obj_list[o].detail == "Reduced":
      obj_list[o].vars = []
    if obj_list[o].detail == "Minimal":
      obj_list[o].vars    = []
      obj_list[o].methods = []

  return obj_list

