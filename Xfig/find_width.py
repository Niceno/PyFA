import Const

#===============================================================================
# Choose box width depending on longest string
#
# Parameters:
#   - filename:   name of the Fortran file being read (.f90)
# Returns:
#   - var_width:  box width in Xfig drawing units
# Used by:
#   - functions which plot boxes
# Warning:
#   - Uses ghost parameter 0.4 to convert width from characters to Xfig units
#-------------------------------------------------------------------------------
def find_width(filename):

  header_name = filename.name
  var_list    = filename.var
  meth_list   = filename.meth
  use_list    = filename.use
  type_list   = filename.types

  if filename.Type() == "Function":
    fun_type = filename.fun_type
  else:
    fun_type = ["0"]
  if use_list == 0:
    use_list = ["0"]
  else:
    use_list = use_list
  if meth_list == 0:
    meth_list = ["0"]
  else:
    meth_list = meth_list
  if var_list == []:
    var_list = ["No variables"]
  if var_list == 0:
    var_list = ["No variables"]
  if type_list == 0:
    type_list = ["No new types"]

  var_length      = max(var_list,  key=len)
  meth_length     = max(meth_list, key=len)
  use_length      = max(use_list,  key=len)
  if fun_type != 0:
    fun_type_length = max(fun_type,  key=len)
  else:
    fun_type_length = 0
  type_length     = max(type_list, key=len)

  if fun_type != 0:
    lengths = [len(var_length),      len(meth_length), \
               len(header_name),     len(use_length),  \
               len(fun_type_length), len(type_length)]
  else:
    lengths = [len(var_length),      len(meth_length), \
               len(header_name),     len(use_length),  \
               len(type_length)]

  box_width = max(lengths)
  box_width = box_width  \
            * Const.UNIT_BOX_HEIGHT * 0.4  # gives the best ratio for width

  return box_width

