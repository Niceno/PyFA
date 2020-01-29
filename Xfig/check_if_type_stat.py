#===============================================================================
# Function to check if object has type statements
#
# Parameters:
#   - object:  checked object
# Returns:
#   - fun_type_len:  1 if it is has type stat, 0 if not
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def check_if_type_stat(object):

  if object.types != 0:
    type_len = len(object.types)

  else:
    type_len = 0

  return type_len

