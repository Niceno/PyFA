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

  if name   == "Black":
    return  0
  elif name == "Blue":
    return  1
  elif name == "Green":
    return  2
  elif name == "Cyan":
    return  3
  elif name == "Red":
    return  4
  elif name == "Magenta":
    return  5
  elif name == "Yellow":
    return  6
  elif name == "White":
    return  7
  elif name == "LtBlue":
    return 11
  elif name == "Pink2":
    return 28
  elif name == "Green2":
    return 14

