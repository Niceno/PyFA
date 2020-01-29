import Finder
from Objects.check_use import check_use
from Objects.Program   import Program

#===============================================================================
# Import attributes from fortran files to program object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - program:      object of type "Program" with assigned attributes
# Used by:
#   - Function for appending programs (all program objects) into a list
#-------------------------------------------------------------------------------
def program_class(file_path):

  type       = "Program"
  prog_name  = Finder.get_prog(file_path)
  use_list   = check_use(Finder.get_use(file_path))
  call_list  = Finder.get_call(file_path)
  type_stat  = Finder.get_type(file_path)
  var_list   = 0
  meth_list  = 0
  level      = 0
  x0         = 0
  y0         = 0
  width      = 0
  height     = 0
  row        = 0
  column     = 0
  path       = file_path

  program = Program(type,        \
                    prog_name,   \
                    use_list,    \
                    var_list,    \
                    meth_list,   \
                    level,       \
                    x0,          \
                    y0,          \
                    width,       \
                    height,      \
                    call_list,   \
                    type_stat,   \
                    row,         \
                    column,      \
                    path)
  return program

