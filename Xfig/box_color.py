#===============================================================================
# Return the code value of a Xfig box color
#
# Parameters:
#   - name:  color name, the same name as in Xfig
# Returns:
#   - number corresponding to color code, as defined in Xfig format
# Used by:
#   - functions which plot frames
#-------------------------------------------------------------------------------
def box_color(name):

  if name   == "Yellow":
    return  6
  elif name == "White":
    return  7
  elif name == "LtBlue":
    return 11
  elif name == "Pink2":
    return 28
  elif name == "Green2":
    return 14

