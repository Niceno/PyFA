#===============================================================================
# Finding module
#-------------------------------------------------------------------------------
import re

def get_mod(filename):
  modules = []
  pattern = re.compile(".+?(?=_Mod$)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:
      for line in myfile:
          if pattern.search(line) != None:      # if a match is found
              modules.append(( line.rstrip("\n")))

  modules = [s.strip() for s in modules if s.strip()] # getting rid of whitespaces
  mod_list = ' '.join(modules)                       # class into a list
  mod_name = re.sub("module ", "", mod_list)
  print("Module: ",mod_name)

get_mod("Mesh_Mod.f90")


#below not working
def get_var(filename):
  var = []
  pattern = re.compile(".+?(?=::)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:
    for line in myfile:
      if pattern.search(line) != None:      # if a match is found
        var.append(( line.rstrip("\n")))

  var = [s.strip() for s in var if s.strip()] # getting rid of whitespaces
 # var_list = ' '.join(var)                       # class into a list
 #var_name = re.sub(" ", "", var_list)
 # for i in range(len(var)):
  nov = var[1]
  res = nov.split("::")

  print("Var: ", res[:])



get_var("Mesh_Mod.f90")
