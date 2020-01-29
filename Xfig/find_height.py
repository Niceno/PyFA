import Const

#===============================================================================
# Function for calculating height of a box
#
# Parameters:
#   - object:    object for calculating height
# Returns:
#   - height     height of the box
# Used by:
#   - Function for updating object attributes
#-------------------------------------------------------------------------------
def find_height(object):

  use_list     = object.use
  var_list     = object.var
  meth_list    = object.meth
  call_list    = object.call
  type_list    = object.type_stat
  len_fun_type = 0

  if use_list == "None":
    use_list = []
  if var_list == 0:
    var_list = []
  if meth_list == 0:
    meth_list = []
  if type_list == 0:
    type_list = []
  if object.type == "Function":
    fun_type = object.fun_type
    if fun_type != 0:
      len_fun_type = 1

  height = Const.UNIT_BOX_HEIGHT  \
         + len(var_list)          \
         + len(meth_list)         \
         + len(use_list)          \
         + len(type_list)         \
         + len_fun_type

  return height

