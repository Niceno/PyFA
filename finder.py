#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re

#===============================================================================
# Finding module
#-------------------------------------------------------------------------------

def get_mod(filename):
  modules = []
  pattern = re.compile(".+?(?=_Mod$)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:
      for line in myfile:
          if pattern.search(line) != None:
              modules.append(( line.rstrip("\n")))

  modules = [s.strip() for s in modules if s.strip()] # remove whitespaces
  mod_list = ' '.join(modules)                        # class into a list
  module_name = re.sub("module ", "", mod_list)       # remove "module"
  print("Module: ",module_name)

#get_mod("Mesh_Mod.f90")

#===============================================================================
# Finding variables
#-------------------------------------------------------------------------------
def get_var(filename):

# finding variables
  vars = []
  with open(filename) as file:
    for line in file:
      urls = re.findall("(?<=:: ).*$", line)
      vars.append(urls)
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
      if pattern.search(line) != None:      # if a match is found
        var_type.append(( line.rstrip("\n")))

  var_type = [s.strip() for s in var_type if s.strip()] # getting rid of whitespaces
  var_type_list = [i.split()[0] for i in var_type]
  var_type_list = ([s.strip(',') for s in var_type_list])

# merge into one list

  result_list = [var_type_list[i] + var_list[i] for i in range(len(var_type_list))]
  print("Variables: ", result_list[:])

#get_var("Eddy_Mod.f90")


#===============================================================================
# Finding module and variable function
#-------------------------------------------------------------------------------

def get_all(filename):

  get_mod(filename)

  get_var(filename)


get_all("Mesh_Mod.f90")
