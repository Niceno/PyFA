
#===============================================================================
# Defining subroutine class
#
# Parameters:
#   - subroutine: initialize name (so you can write subroutine.name to get name)
#   - type:       type of object (can be module/subroutine/function/program)
#   - name:       name of the subroutine
#   - use:        list of subroutine use statements
#   - var:        list of subroutine variables
#   - meth:       list of subroutine methods
#   - level:      level of subroutine
#   - x0:         first corner(upper left) position on x axis in centimeters
#   - y0:         first corner(upper left) position on y axis in centimeters
#   - width:      subroutine box width
#   - height:     subroutine box height
#   - call:       call statements of subroutine
#   - type_stat:  type statements of subroutine
#   - row:        row placement in grid
#   - column:     column placement in grid
# Returns:
#   - nothing
# Used by:
#   - Function for importing attributes(parameters) to subroutine class(object)
#-------------------------------------------------------------------------------
class Subroutine(object):
  def __init__(subroutine, type, name, use, var, meth,  \
               level, x0, y0, width, height,            \
               call, type_stat, row, column, path):

    subroutine.name      = name
    subroutine.use       = use
    subroutine.var       = var
    subroutine.meth      = meth
    subroutine.call      = call
    subroutine.level     = level
    subroutine.x0        = x0
    subroutine.y0        = y0
    subroutine.type      = type
    subroutine.w         = width
    subroutine.h         = height
    subroutine.type_stat = type_stat
    subroutine.row       = row
    subroutine.column    = column
    subroutine.path      = path
    subroutine.in_module = []

