
#===============================================================================
# Defining module class
#
# Parameters:
#   - module:     initialize name (e.g. you can write module.name to get name)
#   - type:       type of object (can be module/subroutine/function/program)
#   - name:       name of the module
#   - use:        list of module use statements
#   - var:        list of module variables
#   - meth:       list of module methods
#   - level:      level of module
#   - x0:         first corner(upper left) position on x axis in centimeters
#   - y0:         first corner(upper left) position on y axis in centimeters
#   - width:      module box width
#   - height:     module box height
#   - call:       call statements of module
#   - type_stat:  type statements of module
#   - row:        row placement in grid
#   - column:     column placement in grid
#   - path:       path to .f90 file
# Returns:
#   - nothing
# Used by:
#   - Function for importing attributes(parameters) to module class(object)
#-------------------------------------------------------------------------------
class Module(object):
  def __init__(module, type, name, use, var, meth,  \
               level, x0, y0, width, height,        \
               call, type_stat, row, column, path):

    module.name      = name
    module.use       = use
    module.var       = var
    module.meth      = meth
    module.call      = call
    module.level     = level
    module.x0        = x0
    module.y0        = y0
    module.type      = type
    module.w         = width
    module.h         = height
    module.type_stat = type_stat
    module.row       = row
    module.column    = column
    module.path      = path

