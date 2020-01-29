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
def load_ij_coordinates(file_with_names, obj_list):

  list = obj_list
  try: myfile = open(file_with_names, 'rt')
  except:
    print("File", file_with_names, "can't be found!  Exiting")
    sys.exit()

  with myfile:
    for line in myfile:
      if not line.startswith("#"):
        data = line.split(";")
        obj_list = update_box_ij_pos(list,          \
                                     data[2],       \
                                     int(data[1]),  \
                                     int(data[0]))
  myfile.close()

  return obj_list

