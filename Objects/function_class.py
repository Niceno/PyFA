import Finder
from Objects.check_use import check_use
from Objects.Function  import Function

#===============================================================================
# Import attributes from fortran files to function object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - function:     object of type "Function" with assigned attributes
# Used by:
#   - Function for appending functions (all function objects) into a list
#-------------------------------------------------------------------------------
def function_class(file_path):

  fun_name   = Finder.get_fun(file_path)
  use_list   = check_use(Finder.get_use(file_path))
  var_list   = Finder.get_var(file_path)
  fun_type   = Finder.get_fun_type(file_path)
  call_list  = Finder.get_call(file_path)
  type_stat  = Finder.get_type(file_path)
  meth_list  = 0
  path       = file_path

  function = Function(fun_name,   \
                      path,       \
                      use_list,   \
                      var_list,   \
                      meth_list,  \
                      call_list,  \
                      fun_type,   \
                      type_stat)

  return function

