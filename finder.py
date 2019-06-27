#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re

#===============================================================================
# Find module
#-------------------------------------------------------------------------------

def get_mod(filename):

  modules = []
  pattern = re.compile(".+?(?=_Mod$)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:               #search for pattern
    for line in myfile:
      if pattern.search(line) != None:
        modules.append(( line.rstrip("\n")))

  modules = [s.strip() for s in modules if s.strip()] # remove whitespaces
  mod_list = ' '.join(modules)                        # class into a list
  module_name = re.sub("module ", "", mod_list)       # remove "module "

  return module_name

#===============================================================================
# Find subroutine
#-------------------------------------------------------------------------------

def get_sub(filename):

  subroutine = []
  pattern = re.compile(".+?(?=subroutine)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:          #search for pattern
    for line in myfile:
      if pattern.search(line) != None:
        subroutine.append(( line.rstrip("\n")))  # add line with pattern to list

  subroutine = [s.strip() for s in subroutine if s.strip()] # remove whitespaces

  if len(subroutine) != 0:                   # check if subroutine is not empty
    sub_string = subroutine[0]
    sub_name = re.sub("subroutine ", "", sub_string)   # return subroutine name
  elif len(subroutine) == 0:
    sub_name = 0                             # if it is empty return 0

  return sub_name

#===============================================================================
# Find if header is module or subroutine
#-------------------------------------------------------------------------------

def get_header(filename):

  sub_name = get_sub(filename)
  module_name = get_mod(filename)

  if len(module_name) != 0:      # if module_name is not empty take module_name
    header = module_name
  elif len(module_name) == 0:    # if module_name is empty take sub_name
    header = sub_name

  return header

#===============================================================================
# Find variables
#-------------------------------------------------------------------------------

def get_var(filename):

  # find var names

  vars = []
  with open(filename) as file:
    for line in file:
      vars_help = re.findall("(?<=:: ).*$", line)  # looking for line with ::
      vars.append(vars_help)                  # list of lists of vars with []
  vars2 = [x for x in vars if x != []]        # list of lists of vars without []

  flat_list = []                              #create 1 list of strings of vars
  for sublist in vars2:
      for item in sublist:
          flat_list.append(item)

  var_name_list = [i.split("!")[0] for i in flat_list]     # takes from :: to !
  var_name_list = clean_list(var_name_list)                # deletes spaces
  var_name_list = [":: " + suit for suit in var_name_list] # adds ":: "
                                                           # to every var


  # find var types

  var_type = []
  pattern = re.compile("::", re.IGNORECASE)

  with open (filename, 'rt') as myfile:          # search for pattern
    for line in myfile:
      if pattern.search(line) != None:
        var_type.append(( line.rstrip("\n")))    # add line with pattern to list

  var_type = [s.strip() for s in var_type if s.strip()]   # remove whitespaces
  var_type_list = [i.split()[0] for i in var_type]        # take first word
  var_type_list = ([s.strip(",") for s in var_type_list]) # remove ","

  # merge var names and var types into one var list

  var_list = [var_type_list[i] + var_name_list[i] \
                    for i in range(len(var_type_list))]

  return var_list

#===============================================================================
# Find methods
#-------------------------------------------------------------------------------

def get_meth(filename):

  methods = []
  with open(filename) as file:
    for line in file:
      meths = re.findall("(?<=_Mod/)(.*)(?=.f90)", line)  # search for methods
      methods.append(meths)
  methods2 = [x for x in methods if x != []]

  flat_list = []
  for sublist in methods2:
    for item in sublist:
      flat_list.append(item)

  # check if any method is found

  if flat_list == []:
    meth_list = ["No methods available"]
  else:
    meth_list = [i.split()[0] for i in flat_list]

  return meth_list

#===============================================================================
# Deletes spaces in all strings of a list
#-------------------------------------------------------------------------------

def clean_list(list_item):
  if isinstance(list_item, list):
    for index in range(len(list_item)):
      if isinstance(list_item[index], list):
        list_item[index] = clean_list(list_item[index])
      if not isinstance(list_item[index], (int, tuple, float, list)):
        list_item[index] = list_item[index].strip()

  return list_item
