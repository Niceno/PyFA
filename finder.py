#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import re
import xfig
import os
import attribute
import sys

#===============================================================================
# Function to search through .f90 file and returns module name
#
# Parameters:
#   - file_name_with_path:     fortran file with full path in front
# Returns:
#   - module_name:             name of the module, return [] if none
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
            if not pattern2.search(line) != None:     # skip line with use
              if not "::" in line:
                module.append(( line.rstrip("\n")))   # add lines to list

  module = [s.strip() for s in module if s.strip()]   # remove whitespaces

  if len(module) != 0:                                # if module is not empty
    mod_string  = module[0]                           # take the first string
    module_name = re.sub("module ", "", mod_string)   # return module name

  elif len(module) == 0:
    module_name = []

  if "!" in module_name:
    module_name = []

  return module_name

#===============================================================================
# Function to search through .f90 file and returns subroutine name
#
# Parameters:
#   - file_name_with_path:  fortran file with full path in front
# Returns:
#   - sub_name:             name of the subroutine, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_sub(file_name_with_path):

  subroutine = []
  pattern    = re.compile(".+?(?=subroutine)", re.IGNORECASE)
  pattern2   = re.compile("(.*)[&]\s*$", re.IGNORECASE)
  pattern3   = re.compile(".+?(?=end)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          if "!" in line:
            line = line.split("!")[0]
          subroutine.append(( line.rstrip("\n")))  # add line with patt. to list

          if pattern2.search(line) != None:           # if "&" is found
            for line in myfile:
              if "!" in line:
                line = line.split("!")[0]

              if not pattern3.search(line) != None:   # if "end" is not found
                new_subroutine = subroutine[0]
                line = line.rstrip("\n")
                line = ''.join(line)
                new_subroutine = new_subroutine + line

                # Editing of string
                new_subroutine = new_subroutine.replace(" ", "")
                new_subroutine = re.sub("subroutine", "", new_subroutine)
                new_subroutine = re.sub("&", "", new_subroutine)
                subroutine[0]  = new_subroutine

                if not pattern2.search(line) != None: # if "&" is not found
                  break                               # stop this inner for loop
                                                      # outer loop continues

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
#   - fun_name:                name of the function, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_fun(file_name_with_path):

  function   = []
  pattern    = re.compile(".+?(?=function)", re.IGNORECASE)
  pattern2   = re.compile("^(.*[^&])\&$", re.IGNORECASE)
  pattern3   = re.compile(".+?(?=end)", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          if "!" in line:
            line = line.split("!")[0]
          if not "print" in line:
            function.append(( line.rstrip("\n")))    # add line with patt. to list

          if pattern2.search(line) != None:           # if "&" is found
            for line in myfile:
              if not pattern3.search(line) != None:   # if "end" is not found

                new_function = function
                new_function.append(( line.rstrip("\n"))),
                new_function = list(new_function)
                new_function = ''.join(new_function)
                new_function = new_function.replace(" ", "")
                new_function = re.sub("&", "", new_function)
                function[0]  = new_function

                if not pattern2.search(line) != None: # if "&" is not found
                  break                               # stop this inner for loop
                                                      # outer loop continues

  function = [s.strip() for s in function if s.strip()] # remove whitespaces

  if len(function) != 0:                      # if function is not empty
    fun_name = function[0]                    # take the first string

    if "function" in fun_name:
      fun_name = fun_name.split("function",1)[1]
    else:
      fun_name = 0

    if fun_name != 0:
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
#   - prog_name:               name of the function, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_prog(file_name_with_path):

  program = []                                 # initialize
  pattern    = re.compile("^\s*.program", re.IGNORECASE)

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
#   - fun_type:                type of the function, return 0 if none
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
#   - call_list:               list of call statements, return 0 if none
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
  call_name_list = [i.rsplit("(")[0] for i in call_name_list]

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
#   - type_list:             list of type statements, return 0 if none
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

  if type_list != []:
    type_list = type_list
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
#   - use_list:               list of use statements, return 0 if none
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_use(file_name_with_path):

  use_name = []

  pattern    = re.compile("(use)\s", re.IGNORECASE)
  pattern2   = re.compile("!.*(use)\s", re.IGNORECASE)

  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        if not line.startswith("!"):               # skip line starting with "!"
          if not line.split(maxsplit=1)[0] == "!": # skip line start with "!"
            if not pattern2.search(line) != None:
              use_name.append(( line.rstrip("\n")))# add line with patt. to list

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

  if use_list != []:
    use_list = use_list
  else:
    use_list = 0

  return use_list

#===============================================================================
# Function to search through .f90 file and returns all variables
#
# Parameters:
#   - file_name_with_path:    fortran file with full path in front
# Returns:
#   - var_list:               list of all variables
# Used by:
#   - Function for deciding which variables to print
#-------------------------------------------------------------------------------
def get_all_var(file_name_with_path):

  # Find all var names
  var_name_list   = []
  pattern        = re.compile("::(.*)", re.IGNORECASE)
  pattern2       = re.compile("(.*)[&]\s*$", re.IGNORECASE)

  # Find names of variables
  with open (file_name_with_path, 'rt') as myfile: # open file
    for line in myfile:                            # read line by line
      if pattern.search(line) != None:             # search for pattern
        line = line.split("::")[1]                 # split line by "::"
        if not line.startswith("!"):               # skip line starting with "!"
          if "!" in line:                          # if "!" is found
            line = line.split("!")[0]              # split by "!" and take 1st
          var_name = line.rstrip("\n")

          if not pattern2.search(var_name) != None:  # if "&" is not found
            var_name_list.append(var_name)           # append var to list

          if pattern2.search(var_name) != None:      # if "&" is found
            long_vars = []                           # list with vars with &
            long_vars.append(var_name)               # append to new list

            for new_line in myfile:                  # read line by line
              if "::" in new_line:                   # if "::" is found in line
                new_line = new_line.split("::")[1]   # split and take 2nd
              if "!" in new_line:                    # if "!" is found in line
                new_line = new_line.split("!")[0]    # split and take 1st

              new_line = new_line.rstrip("\n")
              new_var  = new_line.lstrip()
              long_vars.append(new_var)              # append to long var list

              if not pattern2.search(new_var) != None:   # if "&" is not found
                break                                    # stop inner for loop

            # Put long vars into 1 string and edit
            var_name = ''.join(long_vars)
            var_name = var_name.replace("&","")
            var_name = var_name.replace(" ","")
            var_name = var_name.replace(",",", ")
            var_name = var_name.replace("%"," % ")
            var_name = var_name.replace(":",": ")
            var_name_list.append(var_name)

  var_name_list = [s.strip() for s in var_name_list if s.strip()]
  var_name_list = [":: " + name for name in var_name_list]

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
  var_list = [var_type_list[i]  + var_name_list[i] \
             for i in range(len(var_type_list))]

  return var_list

#===============================================================================
# Function to decide number of printing variables (to print only global)
#
# Parameters:
#   - file_name_with_path:        fortran file with full path in front
# Returns:
#   - sub_var_list:               list of global variables in subroutines
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
#   - meth_list:               list of all methods(module functions)
# Used by:
#   - Functions for assigning attributes to objects
#-------------------------------------------------------------------------------
def get_meth(file_name_with_path):
  module_name = get_mod(file_name_with_path)

  methods = []

  with open(file_name_with_path) as file:                # open file
    for line in file:                                    # read line by line
      meths = re.findall("(?<=_Mod/)(.*)(?=.f90)", line) # search _Mod and .f90
      methods.append(meths)                              # add lines to list
  methods2 = [x for x in methods if x != []]             # remove empty lists

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
      methods.append(meths)                              # add lines to list
  methods2 = [x for x in methods if x != []]             # remove empty lists

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
#  Function for updating use statements
#
# Parameters:
#   - file_paths:    fortran files with full paths in front
#   - obj_list:      list of all objects
# Returns:
#   - obj_list:      list of all objects updated
# Used by:
#   - Main program
#===============================================================================
def get_new_calls(file_paths,obj_list):

  # Get all functions names from obj_list into a list
  fun_list_names = []
  for i in range(0,len(obj_list)):
    if obj_list[i].type == "Function":
      name = obj_list[i].name
      if "(" in name:
        name = name.split("(")
        fun_list_names.append(name[0])
      else:
        fun_list_names.append(name[0])

  # Get all subroutine names from obj_list into a list
  sub_list_names = []
  for i in range(0,len(obj_list)):
    if obj_list[i].type == "Subroutine":
      name = obj_list[i].name
      if "(" in name:
        name = name.split("(")
        sub_list_names.append(name[0])
      else:
        sub_list_names.append(name[0])

  # Put all subroutine and function names in list
  full_list_names = [*fun_list_names,*sub_list_names]

  # Search through files and look for used functions and subroutines
  for i in range(0,len(file_paths)):
    for l in range(0,len(full_list_names)):
      with open(file_paths[i]) as file:
        for line in file:
          if full_list_names[l] in line:
            for o in range(0,len(obj_list)):
              if file_paths[i] == obj_list[o].path:
                calls = obj_list[o].call
                if full_list_names[l] not in obj_list[o].name:
                  if calls == 0:
                    calls = []
                    calls.append(full_list_names[l])
                  else:
                    calls.append(full_list_names[l])
                if calls != 0:
                  calls = list(set(calls))
                  obj_list[o].call = calls

  return obj_list

#===============================================================================
# Function for searching coordinates in file and update them
#
# Parameters:
#   - file_with_names:  file with names and coordinates
#   - obj_list:         list of objects
# Returns:
#   - obj_list:         list of objects with updated placements in grid
# Used by:
#   - Main program (function for changing object placement in grid)
#===============================================================================
def find_coordinates(file_with_names, obj_list):

  list = obj_list
  try: myfile = open(file_with_names, 'rt')
  except:
    print("File", file_with_names, "can't be found!  Exiting")
    sys.exit()

  with myfile:
    for line in myfile:
      if not line.startswith("#"):
        line = "".join(line.split())
        data = line.split(",",2)
        obj_list = attribute.update_box_pos(list,          \
                                            data[2],       \
                                            int(data[0]),  \
                                            int(data[1]))
  myfile.close()

  return obj_list

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
def clean_whitespaces(list_item):
  if isinstance(list_item, list):
    for index in range(len(list_item)):
      if isinstance(list_item[index], list):
        list_item[index] = clean_whitespaces(list_item[index])
      if not isinstance(list_item[index], (int, tuple, float, list)):
        list_item[index] = list_item[index].strip()
  return list_item
