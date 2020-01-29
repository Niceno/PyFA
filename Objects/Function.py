from Objects.Object import Object  # mother

#===============================================================================
# Defining Function class
#
# Parameters:
#   - see explanation for Object class
#   - fun_type:   function type
#   - type_stat:  type statements of subroutine
#   - in_module:  holds the module name it is in
# Returns:
#   - nothing
# Used by:
#   - function_class (object)
#-------------------------------------------------------------------------------
class Function(Object):
  def __init__(self, name, path,      \
               use, var, meth, call,  \
               fun_type, types):

    # Call mother's init
    Object.__init__(self, name, path,      \
                    use, var, meth, call, types)

    self.fun_type  = fun_type
    self.in_module = []

