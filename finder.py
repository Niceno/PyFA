#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re

#===============================================================================
# Finding module
#-------------------------------------------------------------------------------

def get_mod(filename):
  modules = []
  pattern = re.compile(".+?(?=_Mod$)", re.IGNORECASE)  #search for pattern

  with open (filename, 'rt') as myfile:
    for line in myfile:
      if pattern.search(line) != None:
        modules.append(( line.rstrip("\n")))

  modules = [s.strip() for s in modules if s.strip()] # remove whitespaces
  mod_list = ' '.join(modules)                        # class into a list
  module_name = re.sub("module ", "", mod_list)       # remove "module"

  print("Module: ",module_name)
  #return module_name


#===============================================================================
# Finding variables
#-------------------------------------------------------------------------------

def get_var(filename):

# finding variables

  vars = []
  with open(filename) as file:
    for line in file:
      vars_help = re.findall("(?<=:: ).*$", line)
      vars.append(vars_help)
  vars2 = [x for x in vars if x != []]

  flat_list = []
  for sublist in vars2:
      for item in sublist:
          flat_list.append(item)

  var_list = [i.split()[0] for i in flat_list]
  var_list = [":: " + suit for suit in var_list]

# finding var type

  var_type = []
  pattern = re.compile("::", re.IGNORECASE)

  with open (filename, 'rt') as myfile:
    for line in myfile:
      if pattern.search(line) != None:
        var_type.append(( line.rstrip("\n")))

  var_type = [s.strip() for s in var_type if s.strip()] # remove whitespaces
  var_type_list = [i.split()[0] for i in var_type]
  var_type_list = ([s.strip(',') for s in var_type_list])

# merge into one list

  var_result_list = [var_type_list[i] + var_list[i] \
                    for i in range(len(var_type_list))]

  print("Variables: ", var_result_list[:])


#===============================================================================
# Finding functions
#-------------------------------------------------------------------------------

def get_function(filename):

  functions = []
  with open(filename) as file:
    for line in file:
      funs = re.findall("(?<=_Mod/)(.*)(?=.f90)", line)
      functions.append(funs)
  functions2 = [x for x in functions if x != []]

  flat_list = []
  for sublist in functions2:
    for item in sublist:
      flat_list.append(item)

  fun_list = [i.split()[0] for i in flat_list]

  print("Functions: ", fun_list[:])


#===============================================================================
# Finding all function
#-------------------------------------------------------------------------------

def get_all(filename):

  get_mod(filename)

  get_var(filename)

  get_function(filename)

get_all("Mesh_Mod.f90")
