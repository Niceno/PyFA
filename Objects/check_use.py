#===============================================================================
# Function to check if use list is empty
#
# Parameters:
#   - list:      use list to check
# Returns:
#   - use_list:  if it exists return use list, return "None" if list is empty(0)
# Used by:
#   - functions for importing attributes to objects
#-------------------------------------------------------------------------------
def check_use(list):

  if list == 0:
    use_list = "None"
  else:
    use_list = list

  return use_list

