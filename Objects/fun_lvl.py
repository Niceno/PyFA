from Objects.mod_list_fun import mod_list_fun

#===============================================================================
# Function for determining and importing levels of functions (iterate 8 times)
#
# Parameters:
#   - functions_list:   list of function objects
#   - file_paths:       list of all paths to .f90 files
# Returns:
#   - functions_list:   list of function objects with imported correct levels
# Used by:
#   - Function for appending function objects into a list
#-------------------------------------------------------------------------------
def fun_lvl(functions_list,file_paths):

  n = 0
  modules_list = mod_list_fun(file_paths)

  while n < 8:
    n += 1

    for i in range(len(functions_list)):

      if functions_list[i].use != "None":       # if there are use statements
        fun_use_list = functions_list[i].use    # get use list of functions
        fun_use_list = [i.split()[1] for i in fun_use_list]    # only take name
        fun_use_list = ([s.strip(",") for s in fun_use_list])  # modules without
                                                               # other info
        fun_lvl      = []
        for k in range(len(fun_use_list)):        # for every use in function
          for z in range(len(modules_list)):
            if modules_list[z].name == fun_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              fun_lvl.append(lvl)   # add level
        if fun_lvl == []:           # if fun_lvl is empty, level is 0
          fun_lvl = [0]
        else:
          fun_lvl = fun_lvl

        fun_lvl = max(fun_lvl)      # take the biggest used fun level from list
        functions_list[i].level = fun_lvl + 1   # add 1 level to max level

  return functions_list

