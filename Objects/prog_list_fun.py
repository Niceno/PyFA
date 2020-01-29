import Finder
from Objects.program_class import program_class
from Objects.prog_lvl      import prog_lvl

#===============================================================================
# Function for creating programs and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - program_list:   list with only program objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def prog_list_fun(file_paths):

  program_list = []

  for i in range(len(file_paths)):
    program_name = Finder.get_prog(file_paths[i]) # find program from file paths
    if program_name != 0:                 # if it is program then append to list
      program_list.append(program_class(file_paths[i]))

  program_list = prog_lvl(program_list,file_paths)

  return program_list

