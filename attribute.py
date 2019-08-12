#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
#===============================================================================
# Define module class
#-------------------------------------------------------------------------------
class Module(object):
  def __init__(module, type, name, use, var, meth,            \
               level, x0, x1, y0, y1, width, height, call, type_stat):
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

  def print_it(abc):
    print("\nModule name: ", abc.name,     \
          "\n\nUse : ",      abc.use,      \
          "\n\nVariables: ", abc.var,      \
          "\n\nMethods: ",   abc.meth,     \
          "\n\nLevel: ",     abc.level,    \
          "\n\nType: ",      abc.type,     \
          "\n\nx0: ",        abc.x0,       \
          "\n\nx1: ",        abc.x1,       \
          "\n\ny0: ",        abc.y0,       \
          "\n\ny1: ",        abc.y1,       \
          "\n\nWidth: ",     abc.width,    \
          "\n\nHeight: ",    abc.height    )

#===============================================================================
# Define subroutine class
#-------------------------------------------------------------------------------
class Subroutine(object):
  def __init__(subroutine, type, name, use, var, meth,       \
               level, x0, x1, y0, y1, width, height, call, type_stat):

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

def print_it(abc):
  print("\nName: ",            abc.name,     \
        "\n\nUse : ",          abc.use,      \
        "\n\nVariables: ",     abc.var,      \
        "\n\nLevel: ",         abc.level,    \
        "\n\nType: ",          abc.type,     \
        "\n\nx0: ",            abc.x0,       \
        "\n\nx1: ",            abc.x1,       \
        "\n\ny0: ",            abc.y0,       \
        "\n\ny1: ",            abc.y1,       \
        "\n\nWidth: ",         abc.width,    \
        "\n\nHeight: ",        abc.height    )

#===============================================================================
# Define function class
#-------------------------------------------------------------------------------
class Function(object):
  def __init__(function, type, name, use, var, meth,     \
               level, x0, x1, y0, y1, width, height, fun_type, call, type_stat):

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

def print_it(abc):
  print("\nName: ",            abc.name,     \
        "\n\nUse : ",          abc.use,      \
        "\n\nVariables: ",     abc.var,      \
        "\n\nLevel: ",         abc.level,    \
        "\n\nType: ",          abc.type,     \
        "\n\nFunction type: ", abc.fun_type, \
        "\n\nx0: ",            abc.x0,       \
        "\n\nx1: ",            abc.x1,       \
        "\n\ny0: ",            abc.y0,       \
        "\n\ny1: ",            abc.y1,       \
        "\n\nWidth: ",         abc.width,    \
        "\n\nHeight: ",        abc.height    )

#===============================================================================
# Define program class
#-------------------------------------------------------------------------------
class Program(object):
  def __init__(program, type, name, use, var, meth, level,     \
               x0, x1, y0, y1, width, height, call, type_stat):

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

def print_it(abc):
  print("\nName: ",            abc.name,     \
        "\n\nUse : ",          abc.use,      \
        "\n\nVariables: ",     abc.var,      \
        "\n\nLevel: ",         abc.level,    \
        "\n\nType: ",          abc.type,     \
        "\n\nx0: ",            abc.x0,       \
        "\n\nx1: ",            abc.x1,       \
        "\n\ny0: ",            abc.y0,       \
        "\n\ny1: ",            abc.y1,       \
        "\n\nWidth: ",         abc.width,    \
        "\n\nHeight: ",        abc.height    )

#===============================================================================
# Check if use list is empty
#-------------------------------------------------------------------------------
def check_use(list):

  if list == 0:
    use_list = "None"
  else:
    use_list = list
  return use_list

#===============================================================================
# Import attributes from fortran files to module object
#-------------------------------------------------------------------------------
def module_class(filename):

  type         = "Module"
  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))
  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)
  call_list    = finder.get_call(filename)
  type_stat    = finder.get_type(filename)
  level        = 0
  x0           = 1
  x1           = 0
  y0           = 0
  y1           = 0
  width        = 0
  height       = 0

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
                  type_stat)

  return module

#===============================================================================
# Import attributes from fortran files to subroutine object
#-------------------------------------------------------------------------------
def subroutine_class(filename):

  type       = "Subroutine"
  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  call_list  = finder.get_call(filename)
  type_stat  = finder.get_type(filename)
  meth_list  = 0
  level      = 0
  x0         = 1
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0

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
                          type_stat)
  return subroutine

#===============================================================================
# Import attributes from fortran files to function
#-------------------------------------------------------------------------------
def function_class(filename):

  type       = "Function"
  fun_name   = finder.get_fun(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  fun_type   = finder.get_fun_type(filename)
  call_list  = finder.get_call(filename)
  type_stat  = finder.get_type(filename)
  meth_list  = 0
  level      = 0
  x0         = 1
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0

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
                      type_stat)
  return function

#===============================================================================
# Import attributes from fortran files to program
#-------------------------------------------------------------------------------
def program_class(filename):

  type       = "Program"
  prog_name  = finder.get_prog(filename)
  use_list   = check_use(finder.get_use(filename))
  call_list  = finder.get_call(filename)
  type_stat  = finder.get_type(filename)
  var_list   = 0
  meth_list  = 0
  level      = 0
  x0         = 1
  x1         = 0
  y0         = 0
  y1         = 0
  width      = 0
  height     = 0

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
                    type_stat)
  return program

#===============================================================================
# Print mod,sub and function information
#-------------------------------------------------------------------------------
def print_levels(file_list):

  for i in range(len(file_list)):
    print("\nName: ",         file_list[i].name,     \
          "\nType: ",         file_list[i].type,     \
          "\nModules used: ", file_list[i].use,      \
          "\nVariables: ",    file_list[i].var,      \
          "\nMethods: ",      file_list[i].meth,     \
          "\nWidth: ",        file_list[i].width,    \
          "\nHeight: ",       file_list[i].height,   \
          "\nLevel: ",        file_list[i].level)

#===============================================================================
# Finding biggest level of list
#-------------------------------------------------------------------------------
def find_biggest(list):
  lvls = []
  for i in range(len(list)):
    lvl = list[i].level
    lvls.append(lvl)
  lvl = max(lvls)
  return lvl

#===============================================================================
# Finding current level of module
#-------------------------------------------------------------------------------
def find_level(list,name):
  for i in range(len(list)):
    if list[i].name == name:
      lvl = list[i].level
  return lvl

#===============================================================================
# Determining levels of modules  (iterate 8 times)
#-------------------------------------------------------------------------------
def mod_lvl(modules_list):
  n = 0
  while n<8:
    n += 1

    for i in range(len(modules_list)):

      if modules_list[i].use != "None":         # if there are use statements
        mod_use_list = modules_list[i].use      # get use list of modules
        mod_use_list = [i.split()[1] for i in mod_use_list]    # only take name
        mod_use_list = ([s.strip(",") for s in mod_use_list])  # modules without
                                                               # ˄˄ other info
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
        mod_lvl = max(mod_lvl)    # take the biggest used module level from list
        modules_list[i].level = mod_lvl + 1     # add 1 level to max level
  return modules_list

#===============================================================================
# Determining levels of subroutines (iterate 8 times)
#-------------------------------------------------------------------------------
def sub_lvl(subroutines_list,files):
  n = 0
  modules_list = mod_list_fun(files)
  while n<8:
    n += 1

    for i in range(len(subroutines_list)):

      if subroutines_list[i].use != "None":       # if there are use statements
        sub_use_list = subroutines_list[i].use    # get use list of subroutines
        sub_use_list = [i.split()[1] for i in sub_use_list]    # only take name
        sub_use_list = ([s.strip(",") for s in sub_use_list])  # modules without
                                                               # ˄˄  other info
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
# Determining levels of functions (iterate 8 times)
#-------------------------------------------------------------------------------
def fun_lvl(functions_list,files):
  n = 0
  modules_list = mod_list_fun(files)
  while n<8:
    n += 1

    for i in range(len(functions_list)):

      if functions_list[i].use != "None":       # if there are use statements
        fun_use_list = functions_list[i].use    # get use list of functions
        fun_use_list = [i.split()[1] for i in fun_use_list]    # only take name
        fun_use_list = ([s.strip(",") for s in fun_use_list])  # modules without
                                                               # ˄˄  other info
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
# Determining levels of program (iterate 8 times)
#-------------------------------------------------------------------------------
def prog_lvl(program_list,files):
  n = 0
  modules_list = mod_list_fun(files)
  while n<8:
    n += 1

    for i in range(len(program_list)):

      if program_list[i].use != "None":       # if there are use statements
        prog_use_list = program_list[i].use    # get use list of program
        prog_use_list = [i.split()[1] for i in prog_use_list]    # only take name
        prog_use_list = ([s.strip(",") for s in prog_use_list])  # modules without
                                                               # ˄˄  other info
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

        prog_lvl = max(prog_lvl)      # take the biggest used prog level from list
        program_list[i].level = prog_lvl + 2   # add 2 levels to max level
  return program_list

#===============================================================================
# Function for appending mods in list (list with only modules)
#-------------------------------------------------------------------------------
def mod_list_fun(files):
  modules_list = []

  for i in range(len(files)):
    module_name = finder.get_mod(files[i]) #find modules from imported files
    sub_name = finder.get_sub(files[i])    #find subroutines from imported files
    if sub_name == 0:                      # if it is module then append to list
      modules_list.append(module_class(files[i]))
  mod_list = mod_lvl(modules_list)
  return mod_list

#===============================================================================
# Function for appending subs in list (list with only subroutines)
#-------------------------------------------------------------------------------
def sub_list_fun(files):
  subroutines_list = []

  for i in range(len(files)):
    sub_name = finder.get_sub(files[i])   # find subroutines from imported files
    if sub_name != 0:                     # if it subroutine then append to list
      subroutines_list.append(subroutine_class(files[i]))
  sub_list = sub_lvl(subroutines_list,files)

  return sub_list

#===============================================================================
# Function for appending functions in list (list with only functions)
#-------------------------------------------------------------------------------
def fun_list_fun(files):
  functions_list = []

  for i in range(len(files)):
    fun_name = finder.get_fun(files[i])   # find functions from imported files
    if fun_name != 0:                     # if it function then append to list
      functions_list.append(function_class(files[i]))
  fun_list = fun_lvl(functions_list,files)

  return fun_list

#===============================================================================
# Function for appending program in list (list with only programs)
#-------------------------------------------------------------------------------
def prog_list_fun(files):
  program_list = []

  for i in range(len(files)):
    program_name = finder.get_prog(files[i])   # find program from imported files
    if program_name != 0:                 # if it s program then append to list
      program_list.append(program_class(files[i]))

  program_list = prog_lvl(program_list,files)
  return program_list

#===============================================================================
# Remove empty files from list (such as programs and others)
#-------------------------------------------------------------------------------
def remove_empty(file_list):
  i = 0
  while i<len(file_list):
      if file_list[i].name == [] :
          del file_list[i]
      else:
          i+=1
  return file_list

#===============================================================================
# Find y1 coordinate
#-------------------------------------------------------------------------------
def find_y1(file):
  UBH          = 0.75
  use_list     = file.use
  var_list     = file.var
  meth_list    = file.meth

  if use_list == "None":
    use_list = []
  if var_list == 0:
    var_list = []
  if meth_list == 0:
    meth_list = []

  y1 = file.y0 + UBH + len(var_list) + len(meth_list) + len(use_list)

  return y1

#===============================================================================
# Find the biggest box at certain level
#-------------------------------------------------------------------------------
def find_lvl_height(file_list,level):
  heights = []
  for i in range(len(file_list)):
    if file_list[i].level == level:
      height = file_list[i].y1 - file_list[i].y0
      heights.append(height)
  return heights

#===============================================================================
# Updating list attributes
#-------------------------------------------------------------------------------
def update(file_list):
  for i in range(len(file_list)):

    file_list[i].x0     = x_pos(file_list)[i]                 # update x0
    file_list[i].x1     = xfig.choose_width(file_list[i])     # update x1
    file_list[i].y0     = (file_list[i].level*2)+1            # update y0
    file_list[i].y1     = find_y1(file_list[i])               # update y1

  return file_list

#===============================================================================
# List with heights of levels
#-------------------------------------------------------------------------------
def lvl_height(file_list):
  heights_list = [0]
  biggest_lvl  = find_biggest(file_list)
  for i in range(biggest_lvl):
    heights = max(find_lvl_height(file_list,i))
    heights_list.append(heights)

  return heights_list

#===============================================================================
# Updating y coordinates (arranging by levels)
#-------------------------------------------------------------------------------
def arrange_by_level(file_list):
  lvl_heights = lvl_height(file_list)

  for i in range(len(file_list)):
    for l in range(len(lvl_heights)):
      if file_list[i].level == l:
        file_list[i].y0 = file_list[i].y0 + sum(lvl_heights[0:l+1])
        file_list[i].y1 = file_list[i].y1 + sum(lvl_heights[0:l+1])

#===============================================================================
# Function to return list with positions on x axis
#-------------------------------------------------------------------------------
def x_pos(files):
  # Create list with all box widths
  box_widths = [0] + []                       # initialize box_widths list
  for i in range(len(files)):
    box = xfig.choose_width(files[i])
    box_widths.append(box)                    # list of box widths of all boxes

  # Create new list for boxes to be parallel
  sum = 0
  box_pos = []
  for item in box_widths:
    sum += item + 1
    box_pos.append(sum)
  return box_pos

#===============================================================================
# Function for creating lists of classes with same level
#-------------------------------------------------------------------------------
def lvl_list(file_list,lvl):
  list = []
  for i in range(len(file_list)):
    if file_list[i].level == lvl:
      list.append(file_list[i])
  for i in range(len(list)):
    list[i].x0 = x_pos(list)[i]
  return list

#===============================================================================
# Function for putting all classes together again in list
#-------------------------------------------------------------------------------
def lvl_file_list(file_list):
  lvl_lista = []
  lvl_num   = len(lvl_height(file_list))

  for i in range(lvl_num+1):
    lvl = lvl_list(file_list,i)
    lvl_lista.append(lvl)
  flat_list = [item for sublist in lvl_lista for item in sublist]

  return flat_list

#===============================================================================
# Function for finding max width of level
#-------------------------------------------------------------------------------
def find_lvl_width(file_list,level):
  widths = []
  for i in range(len(file_list)):
    if file_list[i].level == level:
      width = file_list[i].width
      widths.append(width)
  return widths

#===============================================================================
# Function for finding max width of all files
#-------------------------------------------------------------------------------
def max_width(file_list):
  widths_list = []
  for i in range(len(file_list)):
    widths = file_list[i].x1 - file_list[i].x0
    widths_list.append(widths)

  max_width = max(widths_list)
  return max_width

#===============================================================================
# Function for finding max height of all files
#-------------------------------------------------------------------------------
def max_height(file_list):
  heights_list = []
  for i in range(len(file_list)):
    heights = file_list[i].y1 - file_list[i].y0
    heights_list.append(heights)

  max_height = max(heights_list)
  return max_height

#===============================================================================
# Function for creating grid
#-------------------------------------------------------------------------------
def create_grid(file_list):
  width   = max_width(file_list)  + 2             # height of each grid spot
  height  = max_height(file_list) + 2             # width of each grid spot
  max_lvl = find_biggest(file_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths (columns)
  for i in range(len(file_list) + 2):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(max_lvl + 2):
    heights = height * i
    height_list.append(heights)

  # List of lists of levels
  for i in range(max_lvl + 2):
    lvl = lvl_list(file_list,i)
    lvl_lista.append(lvl)

  # Assign values to coordinates
  for i in range(len(lvl_lista)):
    lista = lvl_lista[i]
    for l in range(len(lvl_lista[i])):
                                 # v===== remove i to start columns at 0
      lista[l].x0 = ((width_list[l+i]          \
                    + width_list[l+1+i])/2)    \
                    - (lista[l].width/2)

      lista[l].y0 = ((height_list[i]           \
                    + height_list[i+1])/2)     \
                    - (lista[l].height/2)

      lista[l].x1 = lista[l].x0 + lista[l].width
      lista[l].y1 = lista[l].y0 + lista[l].height

      updated_list.append(lista[l])

  return updated_list

#===============================================================================
# Function for generating grid coordinates (not in use)
#-------------------------------------------------------------------------------
def grid_coordinates(file_list,row,column):
  width   = max_width(file_list)  + 2             # height of each spot
  height  = max_height(file_list) + 2             # width of each spot
  max_lvl = find_biggest(file_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths
  for i in range(len(file_list) + 10):
    widths = width * i
    width_list.append(widths)

  # List with heights
  for i in range(max_lvl + 10):
    heights = height * i
    height_list.append(heights)

  x = width_list[row]
  y = height_list[column]

  return (x,y)

#===============================================================================
# Function for updating only 1 box by row and column
#-------------------------------------------------------------------------------
def update_box_pos(file_list, name, column, row):

  width   = max_width(file_list)  + 2             # height of each grid spot
  height  = max_height(file_list) + 2             # width of each grid spot
  max_lvl = find_biggest(file_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths (columns)
  for i in range(len(file_list)+10):
    widths = width * i
    width_list.append(widths)

  # List with heights (rows)
  for i in range(max_lvl + 10):
    heights = height * i
    height_list.append(heights)

  # Assign new coordinates
  for i in range(len(file_list)):
    if name == file_list[i].name:
      file_list[i].x0 = ((width_list[column]        \
                      +   width_list[column+1])/2)  \
                      -  (file_list[i].width/2)

      file_list[i].y0 = ((height_list[row]          \
                      +   height_list[row+1])/2)    \
                      -  (file_list[i].height/2)

      file_list[i].x1 = file_list[i].x0 + file_list[i].width
      file_list[i].y1 = file_list[i].y0 + file_list[i].height

#===============================================================================
# Function for assigning values to x1,width and height
#-------------------------------------------------------------------------------
def assign_values(file_list):

  for i in range(len(file_list)):
    file_list[i].x1     = file_list[i].x1 + file_list[i].x0
    file_list[i].width  = file_list[i].x1 - file_list[i].x0
    file_list[i].height = file_list[i].y1 - file_list[i].y0

  return file_list

#===============================================================================
# Function for saving names of all objects into .txt file
#-------------------------------------------------------------------------------
def write_names(obj_list,file_name):

  name_list = []                                  # initialize list

  for i in range(0,len(obj_list)):                # for every object in list
    name = obj_list[i].name                       # take name of the object
    name_list.append(name)                        # append name to the list
  name_list = sorted(name_list, key=str.lower)    # sort list alphabetically

  # Write list of all names into a .txt file
  open(file_name, "w").write                  \
      ("\n".join(("".join(item)) for item in name_list))

#===============================================================================
# Function for removing subroutine objects that are already in modules
#-------------------------------------------------------------------------------
def remove_unwanted_subs(obj_list):

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
      if meth_list[m] in obj_list[i].name:
        indexes.append(i)

  # Delete unwanted subroutines from objects list
  for index in sorted(indexes, reverse=True):
    del obj_list[index]

  return obj_list

#===============================================================================
# Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def get_obj_list(file_path):
  mod_list  = mod_list_fun(file_path)     # list of all mod classes
  sub_list  = sub_list_fun(file_path)     # list of all sub classes
  fun_list  = fun_list_fun(file_path)     # list of all fun classes
  prog_list = prog_list_fun(file_path)    # list of all prog classes
  file_list = [*mod_list,  \
               *sub_list,  \
               *fun_list,\
               *prog_list]                 # list of all classes(mod+sub+fun)
  file_list = remove_empty(file_list)     # remove empty files from list
  file_list = remove_unwanted_subs(file_list)
  file_list = update(file_list)           # updating coordinates
  arrange_by_level(file_list)             # arranging by levels
  file_list = lvl_file_list(file_list)    # put it together in list
  file_list = assign_values(file_list)    # assign x1,height and width
  file_list = create_grid(file_list)      # plot it with "grid" on

  return file_list
