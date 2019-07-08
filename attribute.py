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
    subroutine.name = name
    subroutine.use  = use
    subroutine.var  = var
    subroutine.level = level
  def print_it(abc):
    print("\nSubroutine name: ", abc.name, \
          "\n\nUse : ",          abc.use,  \
          "\n\nVariables: ",     abc.var,  \
          "\n\nLevel: ",         abc.level)
#===============================================================================
# Define
#-------------------------------------------------------------------------------
def module_class(filename):

  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))

  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)

  if use_list == "None":
    level = 0
  elif use_list != "None":
    level = "?"

  if use_list =="None":
    use_list = "None"
  else:
    use_list = [i.split()[1] for i in use_list]           # take use name
    use_list = ([s.strip(",") for s in use_list])         # remove ","

  modules_list = Module(module_name, use_list, var_list, meth_list, level)

  return modules_list


def subroutine_class(filename):

  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)

  if use_list == []:
    level = 0
  else:
    level = "?"

  if use_list =="None":
    use_list = "None"
  else:
    use_list = [i.split()[1] for i in use_list]           # take use name
    use_list = ([s.strip(",") for s in use_list])         # remove ","

  subroutine = Subroutine(sub_name, use_list, var_list, level)

  return subroutine

#===============================================================================
# Collecting classes into lists
#-------------------------------------------------------------------------------

root = "/home/simcic/Development/Synthetic-Eddies"

files = browse.source_files(root)        # list of all fortran files in root
subroutines_list = []
modules_list = []

for i in range(len(files)):

  module_name = finder.get_mod(files[i])

  if module_name != []:
    modules_list.append(module_class(files[i]))

  else:
    subroutines_list.append(subroutine_class(files[i]))

"""
name_list = []
for i in range(len(modules_list)):
  name_list.append(modules_list[i].name)

  if modules_list[i].level != 0:

    use_list = modules_list[i].use
    modules_list[i].level =  "?"

    print(modules_list[i].name,modules_list[i].level)

print("Imena: ",name_list)
"""


#print(subroutines_list[2].name)
print("\nModule name: ",modules_list[2].name,"\nModules used: ",modules_list[2].use,\
"\nLevel: ",modules_list[2].level)

print("\nModule name: ",modules_list[1].name,"\nModules used: ",modules_list[1].use,\
"\nLevel: ",modules_list[1].level)
