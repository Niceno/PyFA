#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse

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
  def __init__(module, name, use, var, meth):
    module.name = name
    module.use  = use
    module.var  = var
    module.meth = meth

  def print_it(abc):
    print("\nModule name: ", abc.name,     \
          "\n\nUse : ",      abc.use,      \
          "\n\nVariables: ", abc.var,      \
          "\n\nMethods: ",   abc.meth)

#===============================================================================
# Define subroutine class
#-------------------------------------------------------------------------------
class Subroutine(object):
  def __init__(subroutine, name, use, var):
    subroutine.name = name
    subroutine.use  = use
    subroutine.var  = var

  def print_it(abc):
    print("\nSubroutine name: ", abc.name, \
          "\n\nUse : ",          abc.use,  \
          "\n\nVariables: ",     abc.var)

#===============================================================================
# Define
#-------------------------------------------------------------------------------
def module_class(filename):

  module_name  = finder.get_mod(filename)
  use_list     = check_use(finder.get_use(filename))
  var_list     = finder.get_var(filename)
  meth_list    = finder.get_meth(filename)
  modules_list = Module(module_name, use_list, var_list, meth_list)

  return modules_list


def subroutine_class(filename):

  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  subroutine = Subroutine(sub_name, use_list, var_list)

  return subroutine

#===============================================================================
# Collecting classes into lists
#-------------------------------------------------------------------------------

root = "/home/simcic/Development/PyFA"

files = browse.source_files(root)        # list of all fortran files in root
subroutines_list = []
modules_list = []

for i in range(len(files)):

  module_name = finder.get_mod(files[i])

  if module_name != []:
    modules_list.append(module_class(files[i]))

  else:
    subroutines_list.append(subroutine_class(files[i]))

print(subroutines_list[1].name)
print(modules_list[1].name)
