from Objects.mod_list_fun import mod_list_fun

#===============================================================================
# Function for determining and importing levels of subroutines (iterate 8 times)
#
# Parameters:
#   - subroutines_list: list of subroutine objects
#   - file_paths:       list of all paths to .f90 files
# Returns:
#   - subroutines_list: list of subroutine objects with imported correct levels
# Used by:
#   - Function for appending subroutine objects into a list
#-------------------------------------------------------------------------------
def sub_lvl(subroutines_list,file_paths):

  modules_list = mod_list_fun(file_paths)

  n = 0
  while n<8:
    n += 1
    for i in range(len(subroutines_list)):

      if subroutines_list[i].use != "None":       # if there are use statements
        sub_use_list = subroutines_list[i].use    # get use list of subroutines
        sub_use_list = [i.split()[1] for i in sub_use_list]    # only take name
        sub_use_list = ([s.strip(",") for s in sub_use_list])  # modules without
                                                               # other info
        sub_lvl      = []
        for k in range(len(sub_use_list)):        # for every use in subroutine
          for z in range(len(modules_list)):
            if modules_list[z].name == sub_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              sub_lvl.append(lvl)   # add level
        if sub_lvl == []:           # if sub_lvl is empty, level is 0
          sub_lvl = [0]
        else:
          sub_lvl = sub_lvl

        sub_lvl = max(sub_lvl)      # take the biggest used sub level from list
        subroutines_list[i].level = sub_lvl + 1   # add 1 level to max level

  return subroutines_list

