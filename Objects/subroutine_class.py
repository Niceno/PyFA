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

  type       = "Subroutine"
  sub_name   = Finder.get_sub(file_path)
  use_list   = check_use(Finder.get_use(file_path))
  var_list   = Finder.get_var(file_path)
  call_list  = Finder.get_call(file_path)
  type_stat  = Finder.get_type(file_path)
  meth_list  = 0
  level      = 0
  x0         = 0
  y0         = 0
  width      = 0
  height     = 0
  row        = 0
  column     = 0
  path       = file_path

  subroutine = Subroutine(type,       \
                          sub_name,   \
                          use_list,   \
                          var_list,   \
                          meth_list,  \
                          level,      \
                          x0,         \
                          y0,         \
                          width,      \
                          height,     \
                          call_list,  \
                          type_stat,  \
                          row,        \
                          column,     \
                          path)
  return subroutine

