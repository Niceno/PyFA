#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
import os
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
# Import attributes from fortran file and return filled in class
#-------------------------------------------------------------------------------
def module_class(filename):

  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))
  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)

  if use_list == "None":        # if use list is empty,module level is 0
    level = 0
  elif use_list != "None":      # if use list is not empty,module level is "?"
    level = 0  ## should be "?"

  if use_list != "None":
    use_list = [i.split()[1] for i in use_list]    # only take name of used
    use_list = ([s.strip(",") for s in use_list])  # modules without other info

  modules = Module(module_name, use_list, var_list, meth_list, level)

  return modules


def subroutine_class(filename):

  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)

  if use_list == []:           # if use list is empty,module level is 0
    level = 0
  else:                        # if use list is not empty,module level is "?"
    level = 0                       ## should be "?"

  if use_list != "None":
    use_list = [i.split()[1] for i in use_list]    # only take name of used
    use_list = ([s.strip(",") for s in use_list])  # modules without other info

  subroutine = Subroutine(sub_name, use_list, var_list, level)

  return subroutine

#===============================================================================
# Finding current level of module
#-------------------------------------------------------------------------------
def find_level(modules_list,name):
  for i in range(len(modules_list)):
    if modules_list[i].name == name:
      lvl = modules_list[i].level
  return lvl

#===============================================================================
# Collecting classes into lists
#-------------------------------------------------------------------------------
root = "/home/simcic/Development/Synthetic-Eddies"

files = browse.source_files(root)        # list of all fortran files in root
subroutines_list = []                    # initialize list
modules_list     = []                    # initialize list

for i in range(len(files)):
  module_name = finder.get_mod(files[i])  # find all modules from imported files

# If it is module then append to modules list
  if module_name != []:
    modules_list.append(module_class(files[i]))

# If it isn't module then append to subroutines list
  else:
    subroutines_list.append(subroutine_class(files[i]))

#===============================================================================
# Determining levels of modules (not working for now)
#-------------------------------------------------------------------------------

for i in range(len(modules_list)):

  if modules_list[i].use != "None":     # if there are use statements in module
    use_list = modules_list[i].use      # get them
    lvl = []
    for k in range(len(use_list)):      # for every use in module
      lvl.append(find_level(modules_list,use_list[k])) # find used module level

    lvl = max(lvl)                    # take the biggest module level from list
    modules_list[i].level = lvl + 1   # stopped here
    print(use_list)


print("\nModule name: ", modules_list[2].name, "\nModules used: ",   \
      modules_list[2].use, "\nLevel: ", modules_list[2].level)

print("\nModule name: ", modules_list[0].name, "\nModules used: ",   \
      modules_list[0].use, "\nLevel: ", modules_list[0].level)
