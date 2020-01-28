import re

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

