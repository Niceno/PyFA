from Objects.mod_list_fun import mod_list_fun

#===============================================================================
# Function for determining and importing levels of programs (iterate 8 times)
#
# Parameters:
#   - program_list:   list of program objects
#   - file_paths:     list of all paths to .f90 files
# Returns:
#   - program_list:   list of program objects with imported correct levels
# Used by:
#   - Function for appending program objects into a list
#-------------------------------------------------------------------------------
def prog_lvl(program_list, file_paths):
  n = 0
  modules_list = mod_list_fun(file_paths)
  while n<8:
    n += 1

    for i in range(len(program_list)):

      if program_list[i].N_Uses() > 0:          # if there are use statements
        prog_use_list = program_list[i].uses    # get use list of program
        prog_use_list = [i.split()[1] for i in prog_use_list]  # only take name
        prog_use_list = ([s.strip(",") for s in prog_use_list])# modules without
                                                               # other info
        prog_lvl      = []
        for k in range(len(prog_use_list)):        # for every use in program
          for z in range(len(modules_list)):
            if modules_list[z].name == prog_use_list[k]: # if module matches use
              lvl = modules_list[z].level
              prog_lvl.append(lvl)   # add level
        if prog_lvl == []:           # if prog_lvl is empty, level is 0
          prog_lvl = [0]
        else:
          prog_lvl = prog_lvl

        prog_lvl = max(prog_lvl)   # take the biggest used prog level from list
        program_list[i].level = prog_lvl + 1   # add 2 levels to max level
  return program_list

