import Finder
from Objects.function_class import function_class
from Objects.fun_lvl        import fun_lvl

#===============================================================================
# Function for creating functions and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - fun_list:       list with only function objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def fun_list_fun(file_paths):

  functions_list = []

  for i in range(len(file_paths)):
    fun_name = Finder.get_fun(file_paths[i])  # find functions from file paths
    if fun_name != 0:                    # if it is function then append to list
      functions_list.append(function_class(file_paths[i]))

  fun_list = fun_lvl(functions_list,file_paths)

  return fun_list

