import Finder
from Objects.module_class import module_class
from Objects.mod_lvl      import mod_lvl

#===============================================================================
# Function for creating modules and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - mod_list:       list with only module objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def mod_list_fun(file_paths):

  modules_list = []

  for i in range(len(file_paths)):
    module_name = Finder.get_mod(file_paths[i]) # find modules from file paths
    sub_name = Finder.get_sub(file_paths[i])    # find subs from file paths

    if module_name != []:                       # if it is module append to list
      modules_list.append(module_class(file_paths[i]))
  mod_list = mod_lvl(modules_list)

  return mod_list

