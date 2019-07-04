#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
from os import listdir
from os.path import isfile, isdir, join
import os
import finder
import re
#===============================================================================
# Browse through directories and subdirectories
#-------------------------------------------------------------------------------
def check_directories(root):

  # Get module files
  mod_files     = sorted(source_mods(root))
  mod_names     = []
  mod_dirs      = sorted(source_mod_dirs(root))
  mod_file_name = sorted([re.sub(".f90$", '', i) for i in mod_files])

  # Check if module names are same as their subdirectory names
  if mod_file_name == mod_dirs:
    print("\nNo errors. Modules have their corresponding directories.\n")

    for i in range(len(mod_files)):
      mod_name = finder.get_mod(mod_files[i])
      mod_names.append(mod_name)
    mod_names = sorted(mod_names)

    print("Modules: ", mod_names)

  # Check if files in subdirectories match methods of their modules
    for d in range(len(mod_names)):
      print("\nEntering directory: %s" % mod_names[d])

      files = listdir(join(root, mod_names[d]))
      files = sorted([re.sub(".f90$", '', i) for i in files])
      print("Files in module directory: ",files)

      methods = sorted(finder.get_only_meth(mod_files[d]))
      print("Methods of module:         ",methods)

      if files == methods:
        print("\n", mod_names[d], "is looking fine.")

      else:
        print("\n Found ERROR in module directory: ",mod_names[d])

  # If module names are not the same as their subdirectory names
  else:
    print("Module files or directories missing!")

#===============================================================================
# List of all fortran files in root
#-------------------------------------------------------------------------------
def source_files(root):

  fortran_files = []
  for f_name in os.listdir(root):                 # looks for all .f90 files
    if f_name.endswith(".f90"):
      fortran_files.append(f_name)

  return fortran_files

#===============================================================================
# List of all fortran modules in root
#-------------------------------------------------------------------------------
def source_mods(root):

  source_mod = []

  for f_name in os.listdir(root):
    if f_name.endswith("_Mod.f90"):               # looks for all _Mod.f90 files
      source_mod.append(f_name)

  return source_mod

#===============================================================================
# List of all fortran files except modules in root
#-------------------------------------------------------------------------------
def source_subs(root):

  source_sub = []
  source_mod = source_mods(root)

  for f_name in os.listdir(root):
    if f_name.endswith(".f90"):                   # looks for all .f90 files
      source_sub.append(f_name)

  source_sub = list(set(source_sub) - set(source_mod))  # removes _Mod.f90

  return source_sub

#===============================================================================
# List of all _Mod directories in root
#-------------------------------------------------------------------------------
def source_mod_dirs(root):

  source_mod_dir = []

  for f_name in os.listdir(root):
    if f_name.endswith("_Mod"):                # looks for all _Mod directories
      source_mod_dir.append(f_name)

  return source_mod_dir

#===============================================================================
# Prints all unused files and directories in root
#-------------------------------------------------------------------------------
def source_unused(root):

  source_mod_dir = source_mod_dirs(root)
  source_mod = source_mods(root)
  source_sub = source_subs(root)


  directories = [f for f in listdir(root) if isdir (join(root, f))]
  source_unused_dir = list(set(directories) - set(source_mod_dir))

  source_unused_file = []
  for f_name in os.listdir(root):
    source_unused_file.append(f_name)

  source_unused_file = list(set(source_unused_file)    \
                          - set(source_mod)            \
                          - set(source_mod_dir)        \
                          - set(source_sub)            \
                          - set(source_unused_dir))

  print("\nUnused directories:\n",sorted(source_unused_dir), \
        "\n\nUnused files:\n",sorted(source_unused_file),"\n")

  return source_unused_file
