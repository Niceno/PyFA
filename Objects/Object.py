#===============================================================================
# Mother for differet programming constructs:
#
# Function, Module, Program and Subroutine
#
# Parameters:
#
#   - self:       its own self, reserved parameter in Python
#   - name:       name of the object
#   - path:       path to file where the object is defined
#   - use:        list of object's use statements
#   - var:        list of object's variables
#   - meth:       list of object's methods
#   - call:       list of object's call statements
# Returns:
#   - nothing, it is a class definition
# Used by:
#   - Function, Module, Program and Subroutine classes
#-------------------------------------------------------------------------------
class Object():

  def __init__(self, name, path,      \
               use, var, meth, call, types):

    self.name      = name
    self.path      = path

    # Logical properties
    self.use   = use    # list of use statements
    self.var   = var    # list of local variables
    self.meth  = meth   # list of member functions
    self.call  = call   # list of calls
    self.types = types  # list of defined types

    self.level     = 0

    # Geometrical properties
    self.x0        = 0.0
    self.y0        = 0.0
    self.row       = 0
    self.column    = 0
    self.w         = 0.0
    self.h         = 0.0

  def Type(self):
    return self.__class__.__name__
