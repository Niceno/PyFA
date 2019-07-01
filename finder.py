#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re

#===============================================================================
# Find module name
#-------------------------------------------------------------------------------
def get_mod(filename):

  module = []                                         # initialize module list
  pattern = re.compile(".+?(?=_Mod$)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:               # open file
    for line in myfile:                               # read line by line
      if pattern.search(line) != None:                # search for pattern
        module.append(( line.rstrip("\n")))           # add lines to list

  module = [s.strip() for s in module if s.strip()]   # remove whitespaces
  mod_list = ' '.join(module)                         # class into a list
  module_name = re.sub("module ", "", mod_list)       # remove "module "

  return module_name

#===============================================================================
# Find subroutine name
#-------------------------------------------------------------------------------
def get_sub(filename):

  subroutine = []                               # initialize module list
  pattern = re.compile(".+?(?=subroutine)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:         # open file
    for line in myfile:                         # read line by line
      if pattern.search(line) != None:          # search for pattern
        subroutine.append(( line.rstrip("\n"))) # add line with pattern to list

  subroutine = [s.strip() for s in subroutine if s.strip()] # remove whitespaces

  if len(subroutine) != 0:                      # if subroutine is not empty
    sub_string = subroutine[0]                  # take the first string
    sub_name = re.sub("subroutine ", "", sub_string)   # return subroutine name

  elif len(subroutine) == 0:
    sub_name = 0                                # if no subroutine return 0

  return sub_name

#===============================================================================
# Decide if header is module or subroutine
#-------------------------------------------------------------------------------
def get_header(filename):

  sub_name = get_sub(filename)
  module_name = get_mod(filename)

  if len(module_name) != 0:      # if module_name is not empty take module name
    header = module_name
  elif len(module_name) == 0:    # if module_name is empty take sub name
    header = sub_name

  return header

#===============================================================================
# Find all variables
#-------------------------------------------------------------------------------
def get_all_var(filename):

  # find all var names

  vars = []
  with open(filename) as file:                # open file
    for line in file:                         # read line by line
      vars_help = re.findall("(?<=:: ).*$", line)  # looking for line with ::
      vars.append(vars_help)                  # list of lists of vars with []
  vars2 = [x for x in vars if x != []]        # remove empty lists

  flat_list = []                              # create a list of strings of vars
  for sublist in vars2:                       # instead of having lists in lists
      for item in sublist:
          flat_list.append(item)

  var_name_list = [i.split("!")[0] for i in flat_list]     # takes from :: to !
  var_name_list = clean_list(var_name_list)                # deletes spaces
  var_name_list = [":: " + suit for suit in var_name_list] # adds ":: "
                                                           # to every var


  # find all var types

  var_type = []
  pattern = re.compile("::", re.IGNORECASE)

  with open (filename, 'rt') as myfile:          # open file
    for line in myfile:                          # read line by line
      if pattern.search(line) != None:           # search for pattern
        var_type.append(( line.rstrip("\n")))    # add line with pattern to list

  var_type = [s.strip() for s in var_type if s.strip()]   # remove whitespaces
  var_type_list = [i.split()[0] for i in var_type]        # take first string
  var_type_list = ([s.strip(",") for s in var_type_list]) # remove ","

  # merge var names and var types into one var list

  var_list = [var_type_list[i] + var_name_list[i] \
                    for i in range(len(var_type_list))]

  return var_list

#===============================================================================
# Find subroutine variables and choose variables to print
#-------------------------------------------------------------------------------
def get_var(filename):

  var_list = get_all_var(filename)
  sub_name = get_sub(filename)
  module_name = get_mod(filename)

  if len(module_name) == 0:                      # if it is subroutine

    sub_var_list = []
    with open(filename) as file:                 # open file
      for line in file:                          # read line by line
        meths = re.findall("\((.*)\)", line)     # looking for line with "()"
        sub_var_list.append(meths)               # add those lines to list
    sub_var_list2 = [x for x in sub_var_list if x != []]  # remove empty lists

    flat_list = []
    for sublist in sub_var_list2:
      for item in sublist:
        flat_list.append(item)

    sub_var_list = flat_list[0]                  # sub variables inside of ()
    sub_var_list = sub_var_list.split(",")       # split by "," and remove ","
    sub_var_list = var_list[0:len(sub_var_list)] # return only sub variables

  elif len(module_name) != 0:                    # if it is not subroutine

    sub_var_list = var_list                      # return all variables

  return sub_var_list

#===============================================================================
# Find methods
#-------------------------------------------------------------------------------
def get_meth(filename):
  module_name = get_mod(filename)

  methods = []

  with open(filename) as file:                    # open file
    for line in file:                             # read line by line
      meths = re.findall("(?<=_Mod/)(.*)(?=.f90)", line) # search _Mod and .f90
      methods.append(meths)                       # add those lines to list
  methods2 = [x for x in methods if x != []]      # remove empty lists

  flat_meth_list = []                        # create only one list with strings
  for sublist in methods2:                   # instead of list with lists
    for item in sublist:
      flat_meth_list.append(item)

  # check if any method is found
  if len(module_name) == 0:
    meth_list = [""]
  elif flat_meth_list == []:
    meth_list = ["No methods available"]
  elif flat_meth_list != []:
    meth_list = [i.split()[0] for i in flat_meth_list]

  return meth_list

#===============================================================================
# Deletes spaces in all strings of a list (needed at one point)
#-------------------------------------------------------------------------------
def clean_list(list_item):
  if isinstance(list_item, list):
    for index in range(len(list_item)):
      if isinstance(list_item[index], list):
        list_item[index] = clean_list(list_item[index])
      if not isinstance(list_item[index], (int, tuple, float, list)):
        list_item[index] = list_item[index].strip()

  return list_item
