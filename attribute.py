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
  def __init__(module, type, name, use, var, meth,\
               level, x0, x1, y0, y1, width, height):
    module.name   = name
    module.use    = use
    module.var    = var
    module.meth   = meth
    module.level  = level
    module.x0     = x0
    module.x1     = x1
    module.y0     = y0
    module.y1     = y1
    module.type   = type
    module.width  = width
    module.height = height

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
  def __init__(subroutine, type, name, use, var, meth,\
               level, x0, x1, y0, y1, width, height):

    subroutine.name    = name
    subroutine.use     = use
    subroutine.var     = var
    subroutine.meth    = meth
    subroutine.level   = level
    subroutine.x0      = x0
    subroutine.x1      = x1
    subroutine.y0      = y0
    subroutine.y1      = y1
    subroutine.type    = type
    subroutine.width   = width
    subroutine.height  = height

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
# Import attributes from fortran files to module
#-------------------------------------------------------------------------------
def module_class(filename):

  type         = "Module"
  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))
  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)
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
                  height)

  return module

#===============================================================================
# Import attributes from fortran files to subroutine
#-------------------------------------------------------------------------------
def subroutine_class(filename):

  type       = "Subroutine"
  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
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
                          height)
  return subroutine

#===============================================================================
# Print sub and mod information
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
# Determining levels of modules  (iterate 5 times)
#-------------------------------------------------------------------------------
def mod_lvl(modules_list):
  n = 0
  while n<5:
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
# Determining levels of subroutines (iterate 5 times)
#-------------------------------------------------------------------------------
def sub_lvl(subroutines_list,files):
  n = 0
  modules_list = mod_list_fun(files)
  while n<5:
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
  lvl_num = len(lvl_height(file_list))

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
# Function for creating spline connections
#-------------------------------------------------------------------------------
def plot_all_mod_spline(xf,file_list):
  uses = []
  mods = []

  # Getting list with modules
  for i in range(len(file_list)):
    if file_list[i].type == "Module":
      mods.append(file_list[i])

  # Getting list with objects that have use statements
  for i in range(len(file_list)):
    if file_list[i].use != "None":
      uses.append(file_list[i])

  # Plotting connections
  for i in range(len(uses)):
    use = uses[i].use
    for k in range(len(use)):
      used = use[k]
      used = used.strip("use ")
      for m in range(len(mods)):
        if used == mods[m].name:
          xfig.plot_spline(xf, mods[m],uses[i])

#===============================================================================
# Function for creating grid
#-------------------------------------------------------------------------------
def create_grid(file_list):
  width   = max_width(file_list)  + 2             # height of each spot
  height  = max_height(file_list) + 2             # width of each spot
  lvl_num = find_biggest(file_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths
  for i in range(len(file_list)):
    widths = width * i
    width_list.append(widths)

  # List with heights
  for i in range(lvl_num + 1):
    heights = height * i
    height_list.append(heights)

  # List of lists of levels
  for i in range(lvl_num + 1):
    lvl = lvl_list(file_list,i)
    lvl_lista.append(lvl)

  # Assign values to coordinates
  for i in range(len(lvl_lista)):
    lista = lvl_lista[i]
    for l in range(len(lvl_lista[i])):
      lista[l].x0 = width_list[l]
      lista[l].y0 = height_list[i]
      lista[l].x1 = lista[l].x0 + lista[l].width
      lista[l].y1 = lista[l].y0 + lista[l].height

      updated_list.append(lista[l])

  return updated_list

#===============================================================================
# Function for generating grid coordinates (not in use)
#-------------------------------------------------------------------------------
def grid(file_list,row,column):
  width   = max_width(file_list)  + 2             # height of each spot
  height  = max_height(file_list) + 2             # width of each spot
  lvl_num = find_biggest(file_list)               # max level

  width_list   = []
  height_list  = []
  lvl_lista    = []
  updated_list = []

  # List with widths
  for i in range(len(file_list)):
    widths = width * i
    width_list.append(widths)

  # List with heights
  for i in range(lvl_num + 1):
    heights = height * i
    height_list.append(heights)

  x = width_list[row]
  y = height_list[column]

  return (x,y)
#===============================================================================
# Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def get_file_list(file_path):
  mod_list   = mod_list_fun(file_path) # list of all mod classes
  sub_list   = sub_list_fun(file_path) # list of all sub classes
  file_list  = [*mod_list,*sub_list]   # list of all classes(mod + sub)
  file_list  = remove_empty(file_list) # remove empty files from list
  file_list  = update(file_list)       # updating coordinates
  arrange_by_level(file_list)          # arranging by level
  file_list = lvl_file_list(file_list) # put it together

  for i in range(len(file_list)):      # assign these values
    file_list[i].x1     = file_list[i].x1 + file_list[i].x0
    file_list[i].width  = file_list[i].x1 - file_list[i].x0
    file_list[i].height = file_list[i].y1 - file_list[i].y0

  file_list = create_grid(file_list)   # plot it with "grid"
  return file_list
