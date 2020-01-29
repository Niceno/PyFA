import Finder
from Objects.check_use  import check_use
from Objects.Subroutine import Subroutine

#===============================================================================
# Import attributes from fortran files to subroutine object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - subroutine:   object of type "Subroutine" with assigned attributes
# Used by:
#   - Function for appending subroutines (all subroutine objects) into a list
#-------------------------------------------------------------------------------
def subroutine_class(file_path):

  sub_name   = Finder.get_sub(file_path)
  use_list   = check_use(Finder.get_use(file_path))
  var_list   = Finder.get_var(file_path)
  call_list  = Finder.get_call(file_path)
  type_stat  = Finder.get_type(file_path)
  meth_list  = 0
  path       = file_path

  subroutine = Subroutine(sub_name,   \
                          path,       \
                          use_list,   \
                          var_list,   \
                          meth_list,  \
                          call_list,  \
                          type_stat)
  return subroutine

