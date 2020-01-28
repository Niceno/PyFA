#===============================================================================
# Function to choose use statements list length
#
# Parameters:
#   - list:  list of use statements
# Returns:
#   - use_list_len:  number of use statements, zero if none
# Used by:
#   - functions which plot frames, to determine box height
#-------------------------------------------------------------------------------
def use_len(list):
  if list != 0:
    use_list_len = len(list)
  else:
    use_list_len = 0
  return use_list_len

