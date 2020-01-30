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

  len_fun_type = 0
  if object.Type() == "Function": len_fun_type = 1

  height = Const.UNIT_BOX_HEIGHT  \
         + object.N_Vars()        \
         + object.N_Methods()     \
         + object.N_Uses()        \
         + object.N_Types()       \
         + len_fun_type

  return height

