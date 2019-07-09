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
  def __init__(module, name, use, var, meth, level):
    module.name  = name
    module.use   = use
    module.var   = var
    module.meth  = meth
    module.level = level

  def print_it(abc):
    print("\nModule name: ", abc.name,     \
          "\n\nUse : ",      abc.use,      \
          "\n\nVariables: ", abc.var,      \
          "\n\nMethods: ",   abc.meth,     \
          "\n\nLevel: ",     abc.level)

#===============================================================================
# Define subroutine class
#-------------------------------------------------------------------------------
class Subroutine(object):
  def __init__(subroutine, name, use, var, level):
    subroutine.name  = name
    subroutine.use   = use
    subroutine.var   = var
    subroutine.level = level

  def print_it(abc):
    print("\nSubroutine name: ", abc.name, \
          "\n\nUse : ",          abc.use,  \
          "\n\nVariables: ",     abc.var,  \
          "\n\nLevel: ",         abc.level)

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
# Import attributes from fortran file and return filled in class
#-------------------------------------------------------------------------------
def module_class(filename):

  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))
  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)
  level        = 0

  if use_list != "None":
    use_list = [i.split()[1] for i in use_list]    # only take name of used
    use_list = ([s.strip(",") for s in use_list])  # modules without other info

  modules = Module(module_name, use_list, var_list, meth_list, level)

  return modules


def subroutine_class(filename):

  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  level      = 0

  if use_list != "None":
    use_list = [i.split()[1] for i in use_list]    # only take name of used
    use_list = ([s.strip(",") for s in use_list])  # modules without other info

  subroutine = Subroutine(sub_name, use_list, var_list, level)

  return subroutine

#===============================================================================
# Finding current level of module
#-------------------------------------------------------------------------------
def find_level(list,name):
  for i in range(len(list)):
    if list[i].name == name:
      lvl = list[i].level
  return lvl

#===============================================================================
# Finding biggest level of list (not needed for now)
#-------------------------------------------------------------------------------
def find_biggest(list):
  lvls = []
  for i in range(len(list)):
    lvl = list[i].level
    lvls.append(lvl)
  lvl = get_max(lvls)
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
        mod_lvl = []
        for k in range(len(mod_use_list)):      # for every use in module
          mod_lvl.append(find_level(modules_list,mod_use_list[k])) # find level

        mod_lvl = max(mod_lvl)   # take the biggest used module level from list
        modules_list[i].level = mod_lvl + 1     # add 1 level to max level
  return modules_list

#===============================================================================
# Determining levels of subroutines (iterate 5 times)
#-------------------------------------------------------------------------------
def sub_lvl(subroutines_list,modules_list):
  n = 0
  while n<5:
    n += 1

    for i in range(len(subroutines_list)):

      if subroutines_list[i].use != "None":       # if there are use statements
        sub_use_list = subroutines_list[i].use    # get use list of subroutines
        sub_lvl = []
        for k in range(len(sub_use_list)):        # for every use in subroutine
          sub_lvl.append(find_level(modules_list,sub_use_list[k])) # find level

        sub_lvl = max(sub_lvl)      # take the biggest used sub level from list
        subroutines_list[i].level = sub_lvl + 1  # add 1 level to max level
  return subroutines_list


#===============================================================================
# Print subs and mods and their levels
#-------------------------------------------------------------------------------
def mod_list_fun(files):
  modules_list = []
  for i in range(len(files)):
    module_name = finder.get_mod(files[i]) #find all modules from imported files

    if module_name != []:
      modules_list.append(module_class(files[i]))
  mod_list = mod_lvl(modules_list)
  return mod_list

def sub_list_fun(files):
  modules_list = []
  subroutines_list = []

  for i in range(len(files)):
    module_name = finder.get_mod(files[i]) #find all modules from imported files
    modules_list = mod_list_fun(files)
    if module_name == []:
      subroutines_list.append(subroutine_class(files[i]))
  sub_list = sub_lvl(subroutines_list,modules_list)
  return sub_list

#===============================================================================
# Print subs and mods and their levels
#-------------------------------------------------------------------------------
def print_levels(mod_list,sub_list):

  for i in range(len(mod_list)):
    print("\nModule name: ", mod_list[i].name,        \
          "\nLevel: ", mod_list[i].level,             \
          "\nModules used: ", mod_list[i].use)        \

  for i in range(len(sub_list)):
    print("\nSubroutine name: ", sub_list[i].name,    \
          "\nLevel: ", sub_list[i].level,             \
          "\nModules used: ", sub_list[i].use)        \
