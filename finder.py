#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re
import xfig
import os

#===============================================================================
# Function to search through .f90 file and returns module name
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - module_name:   name of the module, return [] if none
# Used by:
#   - Functions for assigning attributes to objects ! Variables in Grid_Mod
#-------------------------------------------------------------------------------
def get_mod(file_name_with_path):

  module   = []                                        # initialize module list
  pattern  = re.compile(".+?(?=_Mod$)", re.IGNORECASE)
  pattern2 = re.compile("^\s*\S*use.*", re.IGNORECASE) # avoiding uses(for prog)

  with open (file_name_with_path, 'rt') as myfile:    # open file
    for line in myfile:                               # read line by line
      if pattern.search(line) != None:                # search for pattern
        if not line.startswith("!"):                  # skip line start with "!"
          if not line.split(maxsplit=1)[0] == "!":    # skip line start with "!"
            if not pattern2.search(line) != None:       # skip line with use
              module.append(( line.rstrip("\n")))       # add lines to list

  module = [s.strip() for s in module if s.strip()]   # remove whitespaces

  if len(module) != 0:                                # if module is not empty
    mod_string  = module[0]                           # take the first string
    module_name = re.sub("module ", "", mod_string)   # return subroutine

  elif len(module) == 0:
    module_name = []

  return module_name

#===============================================================================
# Function to search through .f90 file and returns subroutine name
#
# Parameters:
#   - file_name_with_path:  fortran file with full path in front
# Returns:
#   - sub_name:   name of the subroutine, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_sub(file_name_with_path):

  subroutine = []                               # initialize module list
  pattern    = re.compile(".+?(?=subroutine)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          subroutine.append(( line.rstrip("\n")))  # add line with patt. to list

  subroutine = [s.strip() for s in subroutine if s.strip()] # remove whitespaces

  if len(subroutine) != 0:                      # if subroutine is not empty
    sub_string = subroutine[0]                  # take the first string
    sub_name   = re.sub("subroutine ", "", sub_string)     # return subroutine

    if sub_name.endswith("&"):
      sub_name = sub_name + ")"

  elif len(subroutine) == 0:
    sub_name = 0

  return sub_name

#===============================================================================
# Function to search through .f90 file and returns function name
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - fun_name:      name of the function, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_fun(file_name_with_path):

  function = []                                 # initialize
  pattern    = re.compile(".+?(?=function)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          function.append(( line.rstrip("\n")))    # add line with patt. to list
  function = [s.strip() for s in function if s.strip()] # remove whitespaces

  if len(function) != 0:                      # if function is not empty
    fun_name = function[0]                    # take the first string
    if "integer function " in fun_name:
      fun_name   = re.sub("integer function ", "", fun_name) # return function
    elif "logical function " in fun_name:
      fun_name   = re.sub("logical function ", "", fun_name) # return function

    if fun_name.endswith("&"):
      fun_name = fun_name + ")"

    if fun_name.startswith("!"):
      fun_name = 0

  elif len(function) == 0:
    fun_name = 0

  return fun_name

#===============================================================================
# Function to search through .f90 file and returns program name
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - prog_name:     name of the function, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_prog(file_name_with_path):

  program = []                                 # initialize
  pattern    = re.compile(".+?(?=program)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          program.append(( line.rstrip("\n")))     # add line with patt. to list
  program = [s.strip() for s in program if s.strip()] # remove whitespaces

  if len(program) != 0:                      # if program is not empty
    fun_string = program[0]                  # take the first string

    prog_name   = re.sub("program ", "", fun_string) # return program

    if prog_name.endswith("&"):
      prog_name = prog_name + ")"

    if prog_name.startswith("!"):
      prog_name = 0

  elif len(program) == 0:
    prog_name = 0

  return prog_name

#===============================================================================
# Function to search through .f90 file and returns function type
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - fun_type:      type of the function, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_fun_type(file_name_with_path):

  function = []                                 # initialize
  pattern    = re.compile(".+?(?=function)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          function.append(( line.rstrip("\n")))    # add line with patt. to list
  function = [s.strip() for s in function if s.strip()] # remove whitespaces

  if len(function) != 0:                      # if function is not empty
    fun_string = function[0]                  # take the first string

    fun_type = fun_string.split(" function")[0] # split by "function" and
                                                # take only part before phrase
    fun_type = "type " + fun_type

    if fun_type.endswith("&"):
      fun_type = fun_type + ")"

    if fun_type.startswith("!"):
      fun_type = 0

  elif len(function) == 0:
    fun_type = 0

  return fun_type

#===============================================================================
# Function to search through .f90 file and returns call statements
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - call_list:     list of call statements, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_call(file_name_with_path):

  call_name = []
  pattern   = re.compile("(call)\s", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          call_name.append(( line.rstrip("\n")))   # add line with patt. to list

  call_name = [s.strip() for s in call_name if s.strip()] # remove whitespace

  # If you only want to take name of call statement without "type" or "only"
  call_name_list = [i.split()[1] for i in call_name]           # take call name
  call_name_list = ([s.strip("(") for s in call_name_list])    # remove ","
  call_name_list = [i.rsplit("(",1)[0] for i in call_name_list]

  if call_name_list != []:                # call_name for whole line
    call_list = call_name_list            # call_name_list - take only name
    call_list = list(set(call_list))

  else:
    call_list = 0

  return call_list

#===============================================================================
# Function to search through .f90 file and returns type statements
#
# Parameters:
#   - file_name_with_path:   fortran file with full path in front
# Returns:
#   - type_list:   list of type statements, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_type(file_name_with_path):

  type_name = []
  pattern   = re.compile("^\s+(?=type\s+)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          type_name.append(( line.rstrip("\n")))   # add line with patt. to list

  type_name = [s.strip() for s in type_name if s.strip()] # remove whitespace

  # If you only want to take name of type statement without "type" or "only"
  type_name_list = [i.split()[1] for i in type_name]           # take type name
  type_name_list = ([s.strip("(") for s in type_name_list])    # remove ","
  type_name_list = [i.rsplit("(",1)[0] for i in type_name_list]

  # Solve problem with having "!" in strings
  type_list = []
  for i in range(len(type_name)):
    string = type_name[i]
    string = string.split('!')[0]
    type_list.append(string)

  if type_list != []:           # type_list      - whole string
    type_list = type_list       # true_type_list - take only name
    type_list = list(set(type_list))

  else:
    type_list = 0

  return type_list

#===============================================================================
# Function to search through .f90 file and returns use statements
#
# Parameters:
#   - file_name_with_path:    fortran file with full path in front
# Returns:
#   - use_list:     list of use statements, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_use(file_name_with_path):

  use_name = []

  pattern   = re.compile("(use)\s", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          use_name.append(( line.rstrip("\n")))    # add line with patt. to list

  use_name = [s.strip() for s in use_name if s.strip()] # remove whitespace

  # If you only want to take name of use statement without "type" or "only"
  use_name_list = [i.split()[1] for i in use_name]           # take use name
  use_name_list = ([s.strip(",") for s in use_name_list])    # remove ","
  use_name_list = ["use " + x for x in use_name_list]

  # Solve problem with having "!" in strings
  use_list = []
  for i in range(len(use_name_list)):
    string = use_name_list[i]
    string = string.split('!')[0]
    use_list.append(string)

  if use_list != []:                # use_name for whole line
    use_list = use_list             # use_name_list - take only name
  else:
    use_list = 0

  return use_list

#===============================================================================
# Function to search through .f90 file and returns all variables
#
# Parameters:
#   - file_name_with_path:    fortran file with full path in front
# Returns:
#   - var_list:     list of all variables
# Used by:
#   - Function for deciding which variables to print
#-------------------------------------------------------------------------------
def get_all_var(file_name_with_path):

  # Find all var names

  vars = []
  with open(file_name_with_path) as file:         # open file
    for line in file:                             # read line by line
      vars_help = re.findall("(?<=:: ).*$", line) # looking for line with ::
      vars.append(vars_help)                      # list of lists of vars
  vars2 = [x for x in vars if x != []]            # remove empty lists

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

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          var_type.append(( line.rstrip("\n")))    # add line with patt. to list

  var_type      = [s.strip() for s in var_type if s.strip()] # remove whitespace
  var_type_list = [i.split()[0] for i in var_type]           # take first string
  var_type_list = ([s.strip(",") for s in var_type_list])    # remove ","

  # Merge var names and var types into one var list
  var_list = [var_type_list[i] + var_name_list2[i] \
             for i in range(len(var_type_list))]

  return var_list

#===============================================================================
# Function to decide number of printing variables (to print only global)
#
# Parameters:
#   - file_name_with_path:        fortran file with full path in front
# Returns:
#   - sub_var_list:     list of global variables in subroutines
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_var(file_name_with_path):

  var_list    = get_all_var(file_name_with_path)
  sub_name    = get_sub(file_name_with_path)
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

  if sub_var_list == []:
    sub_var_list = ["No variables defined"]

  return sub_var_list

#===============================================================================
# Function to search through .f90 file and returns all methods(module functions)
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - meth_list:     list of all methods(module functions)
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_meth(file_name_with_path):
  module_name = get_mod(file_name_with_path)

  methods = []

  with open(file_name_with_path) as file:                # open file
    for line in file:                                    # read line by line
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
    meth_list = ["No methods defined"]
  elif flat_meth_list != []:
    meth_list = [i.split()[0] for i in flat_meth_list]
    mod = get_mod(file_name_with_path)                     # get module name
    meth_list = [mod + "_" + x for x in meth_list]         # add module name

  return meth_list

#===============================================================================
# Function to get only names of methods without module names as "prefix"
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - meth_list:     list of methods without module names (e.g. Fetch_Profile)
# Used by:
#   - Function in browse.py for checking directories
#-------------------------------------------------------------------------------
def get_only_meth(file_name_with_path):
  module_name = get_mod(file_name_with_path)

  methods = []

  with open(file_name_with_path) as file:                # open file
    for line in file:                                    # read line by line
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
    meth_list = ["No methods defined"]
  elif flat_meth_list != []:
    meth_list = [i.split()[0] for i in flat_meth_list]

  return meth_list

#===============================================================================
# Function to delete spaces in all strings in a list
#
# Parameters:
#   - list_item:     list that needs to bo "cleaned" of spaces in strings
# Returns:
#   - list_item:     list without spaces in all strings
# Used by:
#   - Function "get_all_var"
#-------------------------------------------------------------------------------
def clean_list(list_item):
  if isinstance(list_item, list):
    for index in range(len(list_item)):
      if isinstance(list_item[index], list):
        list_item[index] = clean_list(list_item[index])
      if not isinstance(list_item[index], (int, tuple, float, list)):
        list_item[index] = list_item[index].strip()
  return list_item
