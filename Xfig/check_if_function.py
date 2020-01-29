#===============================================================================
# Function to check if object is function
#
# Parameters:
#   - object:  checked object
# Returns:
#   - fun_type_len:  1 if it is function, 0 if it is not function
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def check_if_function(object):

  if object.Type() == "Function":
    fun_type_len = 1

  else:
    fun_type_len = 0

  return fun_type_len

