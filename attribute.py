#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
import const

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
#   - x1:         second corner(upper right) position on x axis in centimeters
#   - y1:         second corner(upper right) position on y axis in centimeters
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
  def __init__(module, type, name, use, var, meth,          \
               level, x0, x1, y0, y1, width, height,        \
               call, type_stat, row, column, path):

    module.name      = name
    module.use       = use
    module.var       = var
    module.meth      = meth
    module.call      = call
    module.level     = level
    module.x0        = x0
    module.x1        = x1
    module.y0        = y0
    module.y1        = y1
    module.type      = type
    module.width     = width
    module.height    = height
    module.type_stat = type_stat
    module.row       = row
    module.column    = column
    module.path      = path

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
#   - x1:         second corner(upper right) position on x axis in centimeters
#   - y1:         second corner(upper right) position on y axis in centimeters
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
  def __init__(subroutine, type, name, use, var, meth,       \
               level, x0, x1, y0, y1, width, height,         \
               call, type_stat, row, column, path):

    subroutine.name      = name
    subroutine.use       = use
    subroutine.var       = var
    subroutine.meth      = meth
    subroutine.call      = call
    subroutine.level     = level
    subroutine.x0        = x0
    subroutine.x1        = x1
    subroutine.y0        = y0
    subroutine.y1        = y1
    subroutine.type      = type
    subroutine.width     = width
    subroutine.height    = height
    subroutine.type_stat = type_stat
    subroutine.row       = row
    subroutine.column    = column
    subroutine.path      = path

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
#   - x1:         second corner(upper right) position on x axis in centimeters
#   - y1:         second corner(upper right) position on y axis in centimeters
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
  def __init__(function, type, name, use, var, meth,     \
               level, x0, x1, y0, y1, width, height,     \
               fun_type, call, type_stat, row, column, path):

    function.name      = name
    function.use       = use
    function.var       = var
    function.meth      = meth
    function.call      = call
    function.level     = level
    function.x0        = x0
    function.x1        = x1
    function.y0        = y0
    function.y1        = y1
    function.type      = type
    function.width     = width
    function.height    = height
    function.fun_type  = fun_type
    function.type_stat = type_stat
    function.row       = row
    function.column    = column
    function.path      = path

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
#   - x1:         second corner(upper right) position on x axis in centimeters
#   - y1:         second corner(upper right) position on y axis in centimeters
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
  def __init__(program, type, name, use, var, meth, level,     \
               x0, x1, y0, y1, width, height, call,            \
               type_stat, row, column, path):

    program.name      = name
    program.use       = use
    program.var       = var
    program.meth      = meth
    program.call      = call
    program.level     = level
    program.x0        = x0
    program.x1        = x1
    program.y0        = y0
    program.y1        = y1
    program.type      = type
    program.width     = width
    program.height    = height
    program.type_stat = type_stat
    program.row       = row
    program.column    = column
    program.path      = path

#===============================================================================
# Function to check if use list is empty
#
# Parameters:
#   - list:      use list to check
# Returns:
#   - use_list:  if it exists return use list, return "None" if list is empty(0)
# Used by:
#   - Functions for importing attributes to objects
#-------------------------------------------------------------------------------
def check_use(list):

  if list == 0:
    use_list = "None"
  else:
    use_list = list
  return use_list

#===============================================================================
# Import attributes from fortran files to module object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - module:       object of type "Module" with assigned attributes
# Used by:
#   - Function for appending modules (all module objects) into a list
#-------------------------------------------------------------------------------
def module_class(file_path):

  type         = "Module"
  module_name  = finder.get_mod(file_path)
  use_list     = check_use(finder.get_use(file_path))
  var_list     = finder.get_var(file_path)
  meth_list    = finder.get_meth(file_path)
  call_list    = finder.get_call(file_path)
  type_stat    = finder.get_type(file_path)
  level        = 0
  x0           = 0
  x1           = 0
  y0           = 0
  y1           = 0
  width        = 0
  height       = 0
  row          = 0
  column       = 0
  path         = file_path

  module = Module(type,         \
                  module_name,  \
                  use_list,     \
                  var_list,     \
                  meth_list,    \
                  level,        \
                  x0,           \
                  x1,           \
                  y0,           \
                  y1,           \
                  width,        \
                  height,       \
                  call_list,    \
                  type_stat,    \
                  row,          \
                  column,       \
                  path)

  return module

#===============================================================================
# Import attributes from fortran files to subroutine object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - subroutine:   object of type "Subroutine" with assigned attributes
# Used by:
#   - Function for appending subroutines (all subroutine objects) into a list
#-------------------------------------------------------------------------------
def subroutine_class(file_path):

  type       = "Subroutine"
  sub_name   = finder.get_sub(file_path)
  use_list   = check_use(finder.get_use(file_path))
  var_list   = finder.get_var(file_path)
  call_list  = finder.get_call(file_path)
  type_stat  = finder.get_type(file_path)
  meth_list  = 0
  level      = 0
  x0         = 0
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0
  row        = 0
  column     = 0
  path       = file_path

  subroutine = Subroutine(type,       \
                          sub_name,   \
                          use_list,   \
                          var_list,   \
                          meth_list,  \
                          level,      \
                          x0,         \
                          x1,         \
                          y0,         \
                          y1,         \
                          width,      \
                          height,     \
                          call_list,  \
                          type_stat,  \
                          row,        \
                          column,     \
                          path)
  return subroutine

#===============================================================================
# Import attributes from fortran files to function object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - function:     object of type "Function" with assigned attributes
# Used by:
#   - Function for appending functions (all function objects) into a list
#-------------------------------------------------------------------------------
def function_class(file_path):

  type       = "Function"
  fun_name   = finder.get_fun(file_path)
  use_list   = check_use(finder.get_use(file_path))
  var_list   = finder.get_var(file_path)
  fun_type   = finder.get_fun_type(file_path)
  call_list  = finder.get_call(file_path)
  type_stat  = finder.get_type(file_path)
  meth_list  = 0
  level      = 0
  x0         = 0
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0
  row        = 0
  column     = 0
  path       = file_path

  function = Function(type,       \
                      fun_name,   \
                      use_list,   \
                      var_list,   \
                      meth_list,  \
                      level,      \
                      x0,         \
                      x1,         \
                      y0,         \
                      y1,         \
                      width,      \
                      height,     \
                      fun_type,   \
                      call_list,  \
                      type_stat,  \
                      row,        \
                      column,     \
                      path)

  return function

#===============================================================================
# Import attributes from fortran files to program object
#
# Parameters:
#   - file_path:    path to .f90 file
# Returns:
#   - program:      object of type "Program" with assigned attributes
# Used by:
#   - Function for appending programs (all program objects) into a list
#-------------------------------------------------------------------------------
def program_class(file_path):

  type       = "Program"
  prog_name  = finder.get_prog(file_path)
  use_list   = check_use(finder.get_use(file_path))
  call_list  = finder.get_call(file_path)
  type_stat  = finder.get_type(file_path)
  var_list   = 0
  meth_list  = 0
  level      = 0
  x0         = 0
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0
  row        = 0
  column     = 0
  path       = file_path

  program = Program(type,        \
                    prog_name,   \
                    use_list,    \
                    var_list,    \
                    meth_list,   \
                    level,       \
                    x0,          \
                    x1,          \
                    y0,          \
                    y1,          \
                    width,       \
                    height,      \
                    call_list,   \
                    type_stat,   \
                    row,         \
                    column,      \
                    path)
  return program

#===============================================================================
# Function for printing out all object information
#
# Parameters:
#   - obj_list:   list of objects
# Returns:
#   - nothing
# Used by:
#   - Main program, only for printing information
#-------------------------------------------------------------------------------
def print_info(obj_list):

  for i in range(len(obj_list)):
    print("\nName: ",            obj_list[i].name,        \
          "\nType: ",            obj_list[i].type,        \
          "\nModules used: ",    obj_list[i].use,         \
          "\nVariables: ",       obj_list[i].var,         \
          "\nMethods: ",         obj_list[i].meth,        \
          "\nCalls: ",           obj_list[i].call,        \
          "\nType statements: ", obj_list[i].type_stat,   \
          "\nLevel: ",           obj_list[i].level,       \
          "\nWidth: ",           obj_list[i].width,       \
          "\nHeight: ",          obj_list[i].height,      \
          "\nX0:",               obj_list[i].x0,          \
          "Y0:",                 obj_list[i].y0,          \
          "\nX1:",               obj_list[i].x1,          \
          "Y1:",                 obj_list[i].y1,          \
          "\nFile path:",        obj_list[i].path)

#===============================================================================
# Function to find maximum level of objects from list
#
# Parameters:
#   - obj_list:    list of objects
# Returns:
#   - lvl:         max level of objects from list
# Used by:
#   - Functions for creating grid and updating coordinates of objects
#-------------------------------------------------------------------------------
def find_max_lvl(obj_list):
  lvls = []
  for i in range(len(obj_list)):
    lvl = obj_list[i].level
    lvls.append(lvl)
  lvl = max(lvls)
  return lvl

#===============================================================================
# Function for determining and importing levels of modules (iterate 8 times)
#
# Parameters:
#   - modules_list:    list of module objects
# Returns:
#   - modules_list:    list of module objects with imported correct levels
# Used by:
#   - Function for appending module objects into a list
#-------------------------------------------------------------------------------
def mod_lvl(modules_list):

  n = 0
  while n<8:
    n += 1
    for i in range(len(modules_list)):

      if modules_list[i].use != "None":         # if there are use statements
        mod_use_list = modules_list[i].use      # get use list of modules
        mod_use_list = [i.split()[1] for i in mod_use_list]   # only take name
        mod_use_list = ([s.strip(",") for s in mod_use_list]) # modules without
                                                              # other info
        mod_lvl      = []
        for k in range(len(mod_use_list)):      # for every use in module
          for z in range(len(modules_list)):
            if modules_list[z].name == mod_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              mod_lvl.append(lvl) # add level
        if mod_lvl == []:         # if mod_lvl is empty, level is 0
          mod_lvl = [0]
        else:
          mod_lvl = mod_lvl
        mod_lvl = max(mod_lvl)    # take the max used module level from list
        modules_list[i].level = mod_lvl + 1     # add 1 level to max level
  return modules_list

#===============================================================================
# Function for determining and importing levels of subroutines (iterate 8 times)
#
# Parameters:
#   - subroutines_list: list of subroutine objects
#   - file_paths:       list of all paths to .f90 files
# Returns:
#   - subroutines_list: list of subroutine objects with imported correct levels
# Used by:
#   - Function for appending subroutine objects into a list
#-------------------------------------------------------------------------------
def sub_lvl(subroutines_list,file_paths):

  modules_list = mod_list_fun(file_paths)

  n = 0
  while n<8:
    n += 1
    for i in range(len(subroutines_list)):

      if subroutines_list[i].use != "None":       # if there are use statements
        sub_use_list = subroutines_list[i].use    # get use list of subroutines
        sub_use_list = [i.split()[1] for i in sub_use_list]    # only take name
        sub_use_list = ([s.strip(",") for s in sub_use_list])  # modules without
                                                               # other info
        sub_lvl      = []
        for k in range(len(sub_use_list)):        # for every use in subroutine
          for z in range(len(modules_list)):
            if modules_list[z].name == sub_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              sub_lvl.append(lvl)   # add level
        if sub_lvl == []:           # if sub_lvl is empty, level is 0
          sub_lvl = [0]
        else:
          sub_lvl = sub_lvl

        sub_lvl = max(sub_lvl)      # take the biggest used sub level from list
        subroutines_list[i].level = sub_lvl + 1   # add 1 level to max level
  return subroutines_list

#===============================================================================
# Function for determining and importing levels of functions (iterate 8 times)
#
# Parameters:
#   - functions_list:   list of function objects
#   - file_paths:       list of all paths to .f90 files
# Returns:
#   - functions_list:   list of function objects with imported correct levels
# Used by:
#   - Function for appending function objects into a list
#-------------------------------------------------------------------------------
def fun_lvl(functions_list,file_paths):
  n = 0
  modules_list = mod_list_fun(file_paths)
  while n<8:
    n += 1

    for i in range(len(functions_list)):

      if functions_list[i].use != "None":       # if there are use statements
        fun_use_list = functions_list[i].use    # get use list of functions
        fun_use_list = [i.split()[1] for i in fun_use_list]    # only take name
        fun_use_list = ([s.strip(",") for s in fun_use_list])  # modules without
                                                               # other info
        fun_lvl      = []
        for k in range(len(fun_use_list)):        # for every use in function
          for z in range(len(modules_list)):
            if modules_list[z].name == fun_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              fun_lvl.append(lvl)   # add level
        if fun_lvl == []:           # if fun_lvl is empty, level is 0
          fun_lvl = [0]
        else:
          fun_lvl = fun_lvl

        fun_lvl = max(fun_lvl)      # take the biggest used fun level from list
        functions_list[i].level = fun_lvl + 1   # add 1 level to max level
  return functions_list

#===============================================================================
# Function for determining and importing levels of programs (iterate 8 times)
#
# Parameters:
#   - program_list:   list of program objects
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - program_list:   list of program objects with imported correct levels
# Used by:
#   - Function for appending program objects into a list
#-------------------------------------------------------------------------------
def prog_lvl(program_list, file_paths):
  n = 0
  modules_list = mod_list_fun(file_paths)
  while n<8:
    n += 1

    for i in range(len(program_list)):

      if program_list[i].use != "None":       # if there are use statements
        prog_use_list = program_list[i].use    # get use list of program
        prog_use_list = [i.split()[1] for i in prog_use_list]  # only take name
        prog_use_list = ([s.strip(",") for s in prog_use_list])# modules without
                                                               # other info
        prog_lvl      = []
        for k in range(len(prog_use_list)):        # for every use in program
          for z in range(len(modules_list)):
            if modules_list[z].name == prog_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              prog_lvl.append(lvl)   # add level
        if prog_lvl == []:           # if prog_lvl is empty, level is 0
          prog_lvl = [0]
        else:
          prog_lvl = prog_lvl

        prog_lvl = max(prog_lvl)   # take the biggest used prog level from list
        program_list[i].level = prog_lvl + 1   # add 2 levels to max level
  return program_list

#===============================================================================
# Function for creating modules and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - mod_list:       list with only module objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def mod_list_fun(file_paths):
  modules_list = []

  for i in range(len(file_paths)):
    module_name = finder.get_mod(file_paths[i]) # find modules from file paths
    sub_name = finder.get_sub(file_paths[i])    # find subs from file paths

    if module_name != []:                       # if it is module append to list
      modules_list.append(module_class(file_paths[i]))
  mod_list = mod_lvl(modules_list)
  return mod_list

#===============================================================================
# Function for creating subroutines and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - sub_list:       list with only subrorutine objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def sub_list_fun(file_paths):
  subroutines_list = []

  for i in range(len(file_paths)):
    sub_name = finder.get_sub(file_paths[i])  # find subroutines from file paths
    if sub_name != 0:                         # if it is sub then append to list
      subroutines_list.append(subroutine_class(file_paths[i]))
  sub_list = sub_lvl(subroutines_list,file_paths)

  return sub_list

#===============================================================================
# Function for creating functions and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - fun_list:       list with only function objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def fun_list_fun(file_paths):
  functions_list = []

  for i in range(len(file_paths)):
    fun_name = finder.get_fun(file_paths[i])  # find functions from file paths
    if fun_name != 0:                    # if it is function then append to list
      functions_list.append(function_class(file_paths[i]))
  fun_list = fun_lvl(functions_list,file_paths)

  return fun_list

#===============================================================================
# Function for creating programs and appending into list
#
# Parameters:
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - program_list:   list with only program objects
# Used by:
#   - Function for creating complete and updated object list
#-------------------------------------------------------------------------------
def prog_list_fun(file_paths):
  program_list = []

  for i in range(len(file_paths)):
    program_name = finder.get_prog(file_paths[i]) # find program from file paths
    if program_name != 0:                 # if it is program then append to list
      program_list.append(program_class(file_paths[i]))

  program_list = prog_lvl(program_list,file_paths)
  return program_list

#===============================================================================
# Function for calculating y1 coordinate
#
# Parameters:
#   - object:    object for calculating y1
# Returns:
#   - y1:        second coordinate on y axis (lower corners)
# Used by:
#   - Function for updating object attributes
#-------------------------------------------------------------------------------
def find_y1(object):

  UBH          = 0.75
  use_list     = object.use
  var_list     = object.var
  meth_list    = object.meth
  call_list    = object.call
  type_list    = object.type_stat
  len_fun_type = 0

  if use_list == "None":
    use_list = []
  if var_list == 0:
    var_list = []
  if meth_list == 0:
    meth_list = []
  if type_list == 0:
    type_list = []
  if object.type == "Function":
    fun_type = object.fun_type
    if fun_type != 0:
      len_fun_type = 1

  y1 = object.y0 + UBH + len(var_list) + len(meth_list) + len(use_list)    \
     + len(type_list) + len_fun_type

  return y1

#===============================================================================
# Function for updating (importing) coordinates of objects
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - obj_list:     list of objects with updated coordinates
# Used by:
#   - Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def update(obj_list):
  for i in range(len(obj_list)):

    obj_list[i].x0 = x_pos(obj_list)[i]                              # update x0
    obj_list[i].x1 = xfig.choose_width(obj_list[i]) + obj_list[i].x0 # update x1
    obj_list[i].y0 = (obj_list[i].level*2)+1                         # update y0
    obj_list[i].y1 = find_y1(obj_list[i])                            # update y1

    obj_list[i].height = obj_list[i].y1 - obj_list[i].y0
    obj_list[i].width  = obj_list[i].x1 - obj_list[i].x0

  return obj_list

#===============================================================================
# Function to create list with positions of objects on x axis
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - box_pos:      list of x axis coordinates for objects
# Used by:
#   - Function for creating lists of classes at specific level and updating
#-------------------------------------------------------------------------------
def x_pos(obj_list):

  # Create list with all box widths
  box_widths = [0] + []                       # initialize box_widths list
  for i in range(len(obj_list)):
    box = xfig.choose_width(obj_list[i])
    box_widths.append(box)                    # list of box widths of all boxes

  # Create new list for boxes to be parallel
  sum = 0
  box_pos = []
  for item in box_widths:
    sum += item + 1
    box_pos.append(sum)

  return box_pos

#===============================================================================
# Function for creating lists of objects at specific level
#  and updating x coordinates
#
# Parameters:
#   - obj_list:     list of objects
#   - lvl:          level
# Returns:
#   - list:         list of objects with updated x0 coordinate
# Used by:
#   - Function for creating lists of classes at specific level
#-------------------------------------------------------------------------------
def lvl_list(obj_list,lvl):
  list = []
  for i in range(len(obj_list)):
    if obj_list[i].level == lvl:
      list.append(obj_list[i])
  for i in range(len(list)):
    list[i].x0 = x_pos(list)[i]
  return list

#===============================================================================
# Function for finding maximum width of all objects
#
# Parameters:
#   - obj_list:    list of objects
# Returns:
#   - max_width:   maximum width of all objets (boxes)
# Used by:
#   - Functions for creating and updating grid
#-------------------------------------------------------------------------------
def max_width(obj_list):
  widths_list = []
  for i in range(len(obj_list)):
    widths = obj_list[i].x1 - obj_list[i].x0
    widths_list.append(widths)

  max_width = max(widths_list)
  return max_width

#===============================================================================
# Function for finding max height of all objects
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - max_height:   maximum height of all objets (boxes)
# Used by:
#   - Functions for creating and updating grid
#-------------------------------------------------------------------------------
def max_height(obj_list):
  heights_list = []
  for i in range(len(obj_list)):
    heights = obj_list[i].y1 - obj_list[i].y0
    heights_list.append(heights)

  max_height = max(heights_list)
  return max_height

#===============================================================================
# Function for creating grid and updating coordinates - (Row-Based hierarchy)
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - updated_list: list of objects with updated coordinates (plotting in grid)
# Used by:
#   - Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def create_grid_row(obj_list):
  width   = max_width(obj_list)  + 2             # height of each grid spot
  height  = max_height(obj_list) + 2             # width of each grid spot
  max_lvl = find_max_lvl(obj_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths (columns)
  for i in range(len(obj_list) + 2):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(max_lvl + 2):
    heights = height * i
    height_list.append(heights)

  # List of lists of levels
  for i in range(max_lvl + 2):
    lvl = lvl_list(obj_list,i)
    lvl_lista.append(lvl)

  # Assign values to coordinates
  for i in range(len(lvl_lista)):
    lista = lvl_lista[i]

    # Choose alignment
    if align_boxes == "Diagonal":
      row = i
    elif align_boxes == "Left":
      row = 0

    for l in range(len(lvl_lista[i])):

      lista[l].x0 = ((width_list[l+row]          \
                    + width_list[l+1+row])/2)    \
                    - (lista[l].width/2)

      lista[l].y0 = ((height_list[i]           \
                    + height_list[i+1])/2)     \
                    - (lista[l].height/2)

      lista[l].x1 = lista[l].x0 + lista[l].width
      lista[l].y1 = lista[l].y0 + lista[l].height

      lista[l].row    = i
      lista[l].column = l+row

      updated_list.append(lista[l])

  return updated_list

#===============================================================================
# Function for creating grid and updating coordinates - (Column-Based hierarchy)
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - updated_list: list of objects with updated coordinates (plotting in grid)
# Used by:
#   - Function for creating complete and updated file list
#===============================================================================
def create_grid_column(obj_list):
  width   = max_width(obj_list)  + 2             # height of each grid spot
  height  = max_height(obj_list) + 2             # width of each grid spot
  max_lvl = find_max_lvl(obj_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths (columns)
  for i in range(len(obj_list) + 2):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(len(obj_list) + 2):
    heights = height * i
    height_list.append(heights)

  # List of lists of levels
  for i in range(max_lvl + 2):
    lvl = lvl_list(obj_list,i)
    lvl_lista.append(lvl)

  # Assign values to coordinates
  for i in range(len(lvl_lista)):
    lista = lvl_lista[i]

    # Choose alignment
    if align_boxes == "Diagonal":
      column = i
    elif align_boxes == "Left":
      column = 0

    for l in range(len(lvl_lista[i])):

      lista[l].x0 = ((width_list[i]          \
                    + width_list[i+1])/2)    \
                    - (lista[l].width/2)

      lista[l].y0 = ((height_list[l+column]           \
                    + height_list[l+1+column])/2)     \
                    - (lista[l].height/2)

      lista[l].x1 = lista[l].x0 + lista[l].width
      lista[l].y1 = lista[l].y0 + lista[l].height

      lista[l].row    = i
      lista[l].column = l+column

      updated_list.append(lista[l])

  return updated_list

#===============================================================================
# Function for updating only 1 box by row and column (change placement in grid)
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - nothing
# Used by:
#   - finder.py - Function for searching coordinates in file and updating them
#-------------------------------------------------------------------------------
def update_box_pos(obj_list, name, row, column):

  width   = max_width(obj_list)  + 2             # height of each grid spot
  height  = max_height(obj_list) + 2             # width of each grid spot
  max_lvl = find_max_lvl(obj_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths (columns)
  for i in range(len(obj_list)):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(len(obj_list)):
    heights = height * i
    height_list.append(heights)

  # Assign new coordinates
  for i in range(len(obj_list)):
    if name == obj_list[i].name:
      obj_list[i].x0 = ((width_list[column]         \
                      +   width_list[column+1])/2)  \
                      -  (obj_list[i].width/2)

      obj_list[i].y0 = ((height_list[row]           \
                      +   height_list[row+1])/2)    \
                      -  (obj_list[i].height/2)

      obj_list[i].x1     = obj_list[i].x0 + obj_list[i].width
      obj_list[i].y1     = obj_list[i].y0 + obj_list[i].height
      obj_list[i].row    = row
      obj_list[i].column = column

  return obj_list
#===============================================================================
# Function for saving names of all objects into .txt file
#
# Parameters:
#   - obj_list:     list of objects
#   - file_name:    name of saved .txt file
# Returns:
#   - nothing
# Note:
#   - creates a .txt file in PyFA folder
# Used by:
#   - Main program (simple.py)
#-------------------------------------------------------------------------------
def write_names(obj_list,file_name):

  # Write list of all names into a .txt file
  text_file = open(file_name,"w")
  text_file.write("#\n")
  text_file.write("#  X,  Y,  Name\n")
  text_file.write("#")

  for i in range(0,len(obj_list)):

    text_file.write("\n {:>3},{:>3},  {}".format(obj_list[i].row,     \
                                                 obj_list[i].column,  \
                                                 obj_list[i].name))
  text_file.close()
  print("File", const.OBJ_FILE_NAME, \
        "with object coordinates has been created!")

#===============================================================================
# Function for removing subroutine objects that are already printed
#  in module methods (functions)
#
# Parameters:
#   - obj_list:     list of objects
# Returns:
#   - obj_list:     list of objects without subroutine objects already printed
#                   in module methods (functions)
# Used by:
#   - Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def remove_unnecessary_subs(obj_list):

  meth_list = []            # list of all methods
  indexes   = []            # list of indexes of all unwanted subroutines

  for i in range(0,len(obj_list)):
    if obj_list[i].type == "Module":
      meth_list.append(obj_list[i].meth)

  # Flat list of all methods in modules
  meth_list = [item for sublist in meth_list for item in sublist]

  # List of indexes of all unwanted subroutines
  for i in range(0,len(obj_list)):
    for m in range(0,len(meth_list)):
      method = meth_list[m]
      name   = obj_list[i].name
      name2  = ""
      if "/" in method:
        method = method.split("/", 1)[-1]
      if "(" in name:
        name = name.split("(", 1)[0]
      if "Mod_" in name:
        name2 = name.split("Mod_", 1)[-1]
      if name == method or name2 == method:
        indexes.append(i)

  # Delete unwanted subroutines from objects list
  for index in sorted(indexes, reverse=True):
    del obj_list[index]

  return obj_list

#===============================================================================
# Function for creating complete and updated object list
#
# Parameters:
#   - file_paths:   paths to .f90 files
# Returns:
#   - obj_list:     list with all created and updated objects
# Used by:
#   - Main program (simple.py)
#-------------------------------------------------------------------------------
def get_obj_list(file_paths):

  mod_list  = mod_list_fun(file_paths)   # list of all mod classes
  sub_list  = sub_list_fun(file_paths)   # list of all sub classes
  fun_list  = fun_list_fun(file_paths)   # list of all fun classes
  prog_list = prog_list_fun(file_paths)  # list of all prog classes
  obj_list  = [*mod_list,   \
               *sub_list,   \
               *fun_list,   \
               *prog_list]               # list of all classes(mod+sub+fun+prog)

  obj_list  = remove_unnecessary_subs(obj_list)

  if object_representation == "Compresssed":
    for i in range(0,len(obj_list)):
      obj_list[i].var  = 0
      obj_list[i].meth = 0

  obj_list  = update(obj_list)

  if object_hierarchy == "Column-Based":
    obj_list = create_grid_column(obj_list)
  elif object_hierarchy == "Row-Based":
    obj_list = create_grid_row(obj_list)
  elif object_hierarchy != "Row-Based" and "Column-Based":
    print("Insert correct object hierarchy!")
    obj_list = create_grid_row(obj_list)

  return obj_list
