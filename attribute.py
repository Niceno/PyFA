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
  def __init__(module, type, name, use, var, meth, level, x0, x1, y0, y1):
    module.name  = name
    module.use   = use
    module.var   = var
    module.meth  = meth
    module.level = level
    module.x0    = x0
    module.x1    = x1
    module.y0    = y0
    module.y1    = y1
    module.type  = type

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
          "\n\ny1: ",        abc.y1        )


#===============================================================================
# Define subroutine class
#-------------------------------------------------------------------------------
class Subroutine(object):
  def __init__(subroutine, type, name, use, var, meth, level, x0, x1, y0, y1):
    subroutine.name  = name
    subroutine.use   = use
    subroutine.var   = var
    subroutine.meth  = meth
    subroutine.level = level
    subroutine.x0    = x0
    subroutine.x1    = x1
    subroutine.y0    = y0
    subroutine.y1    = y1
    subroutine.type  = type

  def print_it(abc):
    print("\nSubroutine name: ", abc.name, \
          "\n\nUse : ",          abc.use,  \
          "\n\nVariables: ",     abc.var,  \
          "\n\nLevel: ",         abc.level,\
          "\n\nType: ",          abc.type, \
          "\n\nx0: ",            abc.x0,   \
          "\n\nx1: ",            abc.x1,   \
          "\n\ny0: ",            abc.y0,   \
          "\n\ny1: ",            abc.y1    )

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

  module = Module(type,         \
                  module_name,  \
                  use_list,     \
                  var_list,     \
                  meth_list,    \
                  level,        \
                  x0,           \
                  x1,           \
                  y0,           \
                  y1)

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

  subroutine = Subroutine(type,       \
                          sub_name,   \
                          use_list,   \
                          var_list,   \
                          meth_list,  \
                          level,      \
                          x0,         \
                          x1,         \
                          y0,         \
                          y1)

  return subroutine

#===============================================================================
# Finding biggest level of list (not needed for now)
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
            if modules_list[z].name == mod_use_list[k]:
              lvl = modules_list[z].level
              mod_lvl.append(lvl) # find level
        if mod_lvl == []:
          mod_lvl = [0]
        else:
          mod_lvl = mod_lvl
        mod_lvl = max(mod_lvl)   # take the biggest used module level from list

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
            if modules_list[z].name == sub_use_list[k]:
              lvl = modules_list[z].level
              sub_lvl.append(lvl)   # find level
        if sub_lvl == []:
          sub_lvl = [0]
        else:
          sub_lvl = sub_lvl

        sub_lvl = max(sub_lvl)      # take the biggest used sub level from list
        subroutines_list[i].level = sub_lvl + 1   # add 1 level to max level
  return subroutines_list

#===============================================================================
# Functions for appending subs and mods in their lists
#-------------------------------------------------------------------------------
def mod_list_fun(files):
  modules_list = []
  for i in range(len(files)):
    module_name = finder.get_mod(files[i]) #find modules from imported files
    sub_name = finder.get_sub(files[i])    #find subroutines from imported files
    if sub_name == 0:
      modules_list.append(module_class(files[i]))
  mod_list = mod_lvl(modules_list)
  return mod_list

def sub_list_fun(files):
  modules_list = []
  subroutines_list = []

  for i in range(len(files)):
    module_name = finder.get_mod(files[i]) #find modules from imported files
    sub_name = finder.get_sub(files[i])    #find subroutines from imported files
    modules_list = mod_list_fun(files)
    if sub_name != 0:
      subroutines_list.append(subroutine_class(files[i]))
  sub_list = sub_lvl(subroutines_list,files)

  return sub_list

#===============================================================================
# Print subs and mods and their levels
#-------------------------------------------------------------------------------
def print_levels(file_list):

  for i in range(len(file_list)):
    print("\nName: ", file_list[i].name,           \
          "\nType: ", file_list[i].type,           \
          "\nModules used: ", file_list[i].use,    \
          "\nLevel: ", file_list[i].level)

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

    file_list[i].x0 = xfig.x_pos(file_list)[i]            # update x0
    file_list[i].x1 = xfig.choose_width(file_list[i])     # update x1
    file_list[i].y0 = (file_list[i].level*2)+1            # update y0
    file_list[i].y1 = find_y1(file_list[i])               # update y1

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
# Function for creating lists of classes with same level
#-------------------------------------------------------------------------------
def lvl_list(file_list,lvl):
  list = []
  for i in range(len(file_list)):
    if file_list[i].level == lvl:
      list.append(file_list[i])
  for i in range(len(list)):
    list[i].x0 = xfig.x_pos(list)[i]

  return list

#===============================================================================
# Function for putting all classes together again
#-------------------------------------------------------------------------------
def lvl_file_list(file_list):
  lvl_lista = []
  lvl_num = len(lvl_height(file_list))

  for i in range(lvl_num):
    lvl = lvl_list(file_list,i)
    lvl_lista.append(lvl)
  flat_list = [item for sublist in lvl_lista for item in sublist]

  return flat_list

#===============================================================================
# Function for creating complete and updated file list
#-------------------------------------------------------------------------------
def get_file_list(file_path):
  mod_list   = mod_list_fun(file_path) # list of all mod classes
  sub_list   = sub_list_fun(file_path) # list of all sub classes
  file_list  = [*mod_list,*sub_list]             # list of all classes(mod + sub)
  file_list  = remove_empty(file_list) # remove empty files from list
  file_list  = update(file_list)       # updating coordinates
  arrange_by_level(file_list)          # arranging by level
  file_list = lvl_file_list(file_list) # put it together
  return file_list
