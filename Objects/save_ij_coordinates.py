#===============================================================================
# Function for saving logical coordinates into .ij file
#
# Parameters:
#   - obj_list:     list of objects
#   - file_name:    name of saved .txt file
# Returns:
#   - nothing
# Note:
#   - creates a .txt file in PyFA folder
# Used by:
#   - main program (simple.py)
#-------------------------------------------------------------------------------
def save_ij_coordinates(obj_list,file_name):

  # Write list of all names into a .txt file
  text_file = open(file_name,"w")
  text_file.write("#\n")
  text_file.write("#  i;   j;   name\n")
  text_file.write("#\n")

  for o in range(len(obj_list)):
    text_file.write("%4d;%4d;   %s\n" % (obj_list[o].column,  \
                                         obj_list[o].row,     \
                                         obj_list[o].name))
  text_file.close()
  print("File", file_name, \
        "with (i,j) coordinates has been created!")

