
#===============================================================================
# Defining function class
#
# Parameters:
#   - function:   initialize name (so you can write function.name to get name)
#   - type:       type of object (can be module/subroutine/function/program)
#   - name:       name of the function
#   - use:        list of function use statements
#   - var:        list of function variables
#   - meth:       list of function methods
#   - level:      level of function
#   - x0:         first corner(upper left) position on x axis in centimeters
#   - y0:         first corner(upper left) position on y axis in centimeters
#   - width:      function box width
#   - height:     function box height
#   - fun_type:   type of function
#   - call:       call statements of function
#   - type_stat:  type statements of function
#   - row:        row placement in grid
#   - column:     column placement in grid
# Returns:
#   - nothing
# Used by:
#   - Function for importing attributes(parameters) to function class(object)
#-------------------------------------------------------------------------------
class Function(object):
  def __init__(function, type, name, use, var, meth,  \
               level, x0, y0, width, height,          \
               fun_type, call, type_stat, row, column, path):

    function.name      = name
    function.use       = use
    function.var       = var
    function.meth      = meth
    function.call      = call
    function.level     = level
    function.x0        = x0
    function.y0        = y0
    function.type      = type
    function.w         = width
    function.h         = height
    function.fun_type  = fun_type
    function.type_stat = type_stat
    function.row       = row
    function.column    = column
    function.path      = path
    function.in_module = []

