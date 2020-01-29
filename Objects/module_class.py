import Finder
from Objects.check_use import check_use
from Objects.Module    import Module

#===============================================================================
# Import attributes from fortran files to module object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - module:       object of type "Module" with assigned attributes
# Used by:
#   - Function for appending modules (all module objects) into a list
#-------------------------------------------------------------------------------
def module_class(file_path):

  type         = "Module"
  module_name  = Finder.get_mod(file_path)
  use_list     = check_use(Finder.get_use(file_path))
  var_list     = Finder.get_var(file_path)
  meth_list    = Finder.get_meth(file_path)
  call_list    = Finder.get_call(file_path)
  type_stat    = Finder.get_type(file_path)
  level        = 0
  x0           = 0
  y0           = 0
  width        = 0
  height       = 0
  row          = 0
  column       = 0
  path         = file_path

  module = Module(type,         \
                  module_name,  \
                  use_list,     \
                  var_list,     \
                  meth_list,    \
                  level,        \
                  x0,           \
                  y0,           \
                  width,        \
                  height,       \
                  call_list,    \
                  type_stat,    \
                  row,          \
                  column,       \
                  path)

  return module

