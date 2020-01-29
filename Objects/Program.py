
#===============================================================================
# Defining program class
#
# Parameters:
#   - program:    initialize name (so you can write program.name to get name)
#   - type:       type of object (can be module/subroutine/function/program)
#   - name:       name of the program
#   - use:        list of program use statements
#   - var:        list of program variables
#   - meth:       list of program methods
#   - level:      level of program
#   - x0:         first corner(upper left) position on x axis in centimeters
#   - y0:         first corner(upper left) position on y axis in centimeters
#   - width:      program box width
#   - height:     program box height
#   - call:       call statements of program
#   - type_stat:  type statements of program
#   - row:        row placement in grid
#   - column:     column placement in grid
# Returns:
#   - nothing
# Used by:
#   - program for importing attributes(parameters) to program class(object)
#-------------------------------------------------------------------------------
class Program(object):
  def __init__(program, type, name, use, var, meth, level,  \
               x0, y0, width, height, call,                 \
               type_stat, row, column, path):

    program.name      = name
    program.use       = use
    program.var       = var
    program.meth      = meth
    program.call      = call
    program.level     = level
    program.x0        = x0
    program.y0        = y0
    program.type      = type
    program.w         = width
    program.h         = height
    program.type_stat = type_stat
    program.row       = row
    program.column    = column
    program.path      = path

