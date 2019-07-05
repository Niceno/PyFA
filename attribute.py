#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse

#filename = "Eddy_Mod.f90"
filename = "Save_Vtk.f90"

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
# Define what to choose
#-------------------------------------------------------------------------------
module_name = finder.get_mod(filename)

if len(module_name) != 0:
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  meth_list  = finder.get_meth(filename)
  p1 = Module(module_name, use_list, var_list, meth_list)

else:
  sub_name   = finder.get_sub(filename)
  use_list   = check_use(finder.get_use(filename))
  var_list   = finder.get_var(filename)
  p1 = Subroutine(sub_name, use_list, var_list)

p1.print_it()
