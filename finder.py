#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re
import xfig
import os

#===============================================================================
# Find module name
#-------------------------------------------------------------------------------
def get_mod(filename):

  module   = []                                        # initialize module list
  pattern  = re.compile(".+?(?=_Mod$)", re.IGNORECASE)
  pattern2 = re.compile("^\s*\S*use.*", re.IGNORECASE) # avoiding uses(for prog)

  with open (filename, 'rt') as myfile:               # open file
    for line in myfile:                               # read line by line
      if pattern.search(line) != None:                # search for pattern
        if not line.startswith("!"):                  # skip line start with "!"
          if not pattern2.search(line) != None:       # skip line with use
            module.append(( line.rstrip("\n")))       # add lines to list

  module = [s.strip() for s in module if s.strip()]   # remove whitespaces

  if len(module) != 0:                                # if module is not empty
    mod_string  = module[0]                           # take the first string
    module_name = re.sub("module ", "", mod_string)   # return subroutine

  elif len(module) == 0:
    module_name = []                                # if no module return empty

  return module_name

#===============================================================================
# Find subroutine name
#-------------------------------------------------------------------------------
def get_sub(filename):

  subroutine = []                               # initialize module list
  pattern    = re.compile(".+?(?=subroutine)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:         # open file
    for line in myfile:                         # read line by line
      if pattern.search(line) != None:          # search for pattern
        if not line.startswith("!"):            # skip line starting with "!"
          subroutine.append(( line.rstrip("\n"))) # add line with pattern to list

  subroutine = [s.strip() for s in subroutine if s.strip()] # remove whitespaces

  if len(subroutine) != 0:                      # if subroutine is not empty
    sub_string = subroutine[0]                  # take the first string
    sub_name   = re.sub("subroutine ", "", sub_string)     # return subroutine

    if sub_name.endswith("&"):
    #  sub_name =  sub_name[:-len("  &")]
      sub_name = sub_name + ")"

  elif len(subroutine) == 0:
    sub_name = 0                                # if no subroutine return 0

  return sub_name

#===============================================================================
# Find function name
#-------------------------------------------------------------------------------
def get_fun(filename):

  function = []                                 # initialize
  pattern    = re.compile(".+?(?=function)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:         # open file
    for line in myfile:                         # read line by line
      if pattern.search(line) != None:          # search for pattern
        if not line.startswith("!"):            # skip line starting with "!"
          function.append(( line.rstrip("\n"))) # add line with pattern to list
  function = [s.strip() for s in function if s.strip()] # remove whitespaces

  if len(function) != 0:                      # if function is not empty
    fun_string = function[0]                  # take the first string

    fun_name   = re.sub("integer function ", "", fun_string) # return function

    if fun_name.endswith("&"):
    #  fun_name =  fun_name[:-len("  &")]
      fun_name = fun_name + ")"

    if fun_name.startswith("!"):
      fun_name = 0

  elif len(function) == 0:
    fun_name = 0                                # if no function return 0

  return fun_name

#===============================================================================
# Find function name
#-------------------------------------------------------------------------------
def get_prog(filename):

  program = []                                 # initialize
  pattern    = re.compile(".+?(?=program)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:         # open file
    for line in myfile:                         # read line by line
      if pattern.search(line) != None:          # search for pattern
        if not line.startswith("!"):            # skip line starting with "!"
          program.append(( line.rstrip("\n"))) # add line with pattern to list
  program = [s.strip() for s in program if s.strip()] # remove whitespaces

  if len(program) != 0:                      # if program is not empty
    fun_string = program[0]                  # take the first string

    prog_name   = re.sub("program ", "", fun_string) # return program

    if prog_name.endswith("&"):
    #  prog_name =  prog_name[:-len("  &")]
      prog_name = prog_name + ")"

    if prog_name.startswith("!"):
      prog_name = 0

  elif len(program) == 0:
    prog_name = 0                                # if no program return 0

  return prog_name

#===============================================================================
# Find function name
#-------------------------------------------------------------------------------
def get_fun_type(filename):

  function = []                                 # initialize
  pattern    = re.compile(".+?(?=function)", re.IGNORECASE)

  with open (filename, 'rt') as myfile:         # open file
    for line in myfile:                         # read line by line
      if pattern.search(line) != None:          # search for pattern
        if not line.startswith("!"):            # skip line starting with "!"
          function.append(( line.rstrip("\n"))) # add line with pattern to list
  function = [s.strip() for s in function if s.strip()] # remove whitespaces

  if len(function) != 0:                      # if function is not empty
    fun_string = function[0]                  # take the first string

    fun_name = fun_string.split(" function")[0] # split by "function" and
                                                # take only part before phrase
    fun_name = "type " + fun_name

    if fun_name.endswith("&"):
    #  fun_name =  fun_name[:-len("  &")]
      fun_name = fun_name + ")"

    if fun_name.startswith("!"):
      fun_name = 0

  elif len(function) == 0:
    fun_name = 0                                # if no function return 0

  return fun_name

#===============================================================================
# Decide if header is module or subroutine
#-------------------------------------------------------------------------------
def get_header(filename):

  sub_name    = get_sub(filename)
  module_name = get_mod(filename)
  if sub_name != 0:      # if module_name is not empty take module name
    header = sub_name
  elif sub_name == 0:    # if module_name is empty take sub name
    header = module_name

  return header

#===============================================================================
# Find use statements
#-------------------------------------------------------------------------------
def get_use(filename):

  use_name = []
#  next_lines = []

  pattern   = re.compile("(use)\s", re.IGNORECASE)
#  pattern2  = re.compile("^(  use)(.*)(only)(.*)(&)$", re.IGNORECASE)
#  pattern3  = re.compile("(.*)(&)$", re.IGNORECASE)

  with open (filename, 'rt') as myfile:          # open file
    for line in myfile:                          # read line by line
      if pattern.search(line) != None:           # search for pattern
        if not line.startswith("!"):             # skip line starting with "!"
          use_name.append(( line.rstrip("\n")))  # add line with pattern to list

#      if pattern2.search(line) != None:
#        next_line = "use" + next(myfile)
#        print(next_line)
#        use_name.append(next_line)
#        if next_line.endswith("&"):
#          print("Found")
#          next_line2 = "use" + next(myfile)
#          use_name.append(next_line2)

  use_name = [s.strip() for s in use_name if s.strip()] # remove whitespace
#  print(use_name)

  # If you only want to take name of use statement without "type" or "only"
  use_name_list = [i.split()[1] for i in use_name]           # take use name
  use_name_list = ([s.strip(",") for s in use_name_list])    # remove ","
  use_name_list = ["use " + x for x in use_name_list]

  # Solve problem with having "!" in strings
  use_list = []
  for i in range(len(use_name)):
    string = use_name[i]
    string = string.split('!')[0]
    use_list.append(string)

  if use_name != []:                # use_name for whole line
    true_name_list = use_name_list  # use_name_list - take only name
  else:
    true_name_list = 0

  return true_name_list

#===============================================================================
# Find all variables
#-------------------------------------------------------------------------------
def get_all_var(filename):

  # Find all var names

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
  var_name_list2 = []
  for i in range(len(var_name_list)):
    string = var_name_list[i]
    string = string.split('!')[0]
    var_name_list2.append(string)


  # Find all var types

  var_type = []
  pattern  = re.compile("::", re.IGNORECASE)

  with open (filename, 'rt') as myfile:          # open file
    for line in myfile:                          # read line by line
      if pattern.search(line) != None:           # search for pattern
        if not line.startswith("!"):             # skip line starting with "!"
          var_type.append(( line.rstrip("\n")))  # add line with pattern to list

  var_type      = [s.strip() for s in var_type if s.strip()] # remove whitespace
  var_type_list = [i.split()[0] for i in var_type]           # take first string
  var_type_list = ([s.strip(",") for s in var_type_list])    # remove ","

  # merge var names and var types into one var list

  var_list = [var_type_list[i] + var_name_list2[i] \
             for i in range(len(var_type_list))]

  return var_list

#===============================================================================
# Find subroutine variables and choose variables to print
#-------------------------------------------------------------------------------
def get_var(filename):

  var_list    = get_all_var(filename)
  sub_name    = get_sub(filename)

  if sub_name != 0:                                # if it is subroutine

    sub_var_list = []
    result = re.search("\((.*)\)", sub_name)
    if result:
      sub_var_list = result.group(0)

    if isinstance(sub_var_list, list):
      sub_var_list = var_list
    else:
      sub_var_list = sub_var_list.split(",")       # split by "," and remove ","
      sub_var_list = var_list[0:len(sub_var_list)] # return only sub variables

  else:                                            # if it is not subroutine
    sub_var_list = var_list                        # return all variables

  return sub_var_list

#===============================================================================
# Find methods with their module name
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

  # Check if any method is found

  if len(module_name) == 0:
    meth_list = [""]
  elif flat_meth_list == []:
    meth_list = ["No methods available"]
  elif flat_meth_list != []:
    meth_list = [i.split()[0] for i in flat_meth_list]
    mod = get_mod(filename)                               # get module name
    meth_list = [mod + "_" + x for x in meth_list]        # add module name

  return meth_list

#===============================================================================
# Find only methods names
#-------------------------------------------------------------------------------

def get_only_meth(filename):
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

  # Check if any method is found

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
