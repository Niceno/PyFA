
#===============================================================================
# Function for determining and importing levels of modules (iterate 8 times)
#
# Parameters:
#   - modules_list:    list of module objects
# Returns:
#   - modules_list:    list of module objects with imported correct levels
# Used by:
#   - Function for appending module objects into a list
#-------------------------------------------------------------------------------
def mod_lvl(modules_list):

  n = 0
  while n<8:
    n += 1
    for i in range(len(modules_list)):

      if modules_list[i].N_Uses() > 0:         # if there are use statements
        mod_use_list = modules_list[i].uses     # get use list of modules
        mod_use_list = [i.split()[1] for i in mod_use_list]   # only take name
        mod_use_list = ([s.strip(",") for s in mod_use_list]) # modules without
                                                              # other info
        mod_lvl      = []
        for k in range(len(mod_use_list)):      # for every use in module
          for z in range(len(modules_list)):
            if modules_list[z].name == mod_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              mod_lvl.append(lvl) # add level
        if mod_lvl == []:         # if mod_lvl is empty, level is 0
          mod_lvl = [0]
        else:
          mod_lvl = mod_lvl
        mod_lvl = max(mod_lvl)    # take the max used module level from list
        modules_list[i].level = mod_lvl + 1     # add 1 level to max level
  return modules_list

