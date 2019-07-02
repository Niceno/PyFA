from os import listdir
from os.path import isfile, isdir, join
import os
#root = "/home/simcic/Development/Synthetic-Eddies"
#root = "."
#dirs = [f for f in listdir(root) if isdir (join(root, f))] # finds directories

#dirs.append(root)                                   # adds root to directories


#for d in dirs:
 # print("Enter directory %s" % d)

  # List current directory
  #files = listdir(join(root, d))            # All files and folders in directory

  #for f in files:
   # if isfile(join(root, d, f)):
    #  print("  File: %s" % f)


#===============================================================================
# List of all fortran files in root
#-------------------------------------------------------------------------------
def source_files(root):

  fortran_files = []
  for f_name in os.listdir(root):                  # looks for all .f90 files
    if f_name.endswith(".f90"):
      fortran_files.append(f_name)
  unused = source_unused(root)

  return fortran_files


#===============================================================================
# List of all fortran modules in root
#-------------------------------------------------------------------------------

def source_mods(root):

  source_mod = []

  for f_name in os.listdir(root):
    if f_name.endswith("_Mod.f90"):
      source_mod.append(f_name)

  return source_mod

#===============================================================================
# List of all fortran files except modules in root
#-------------------------------------------------------------------------------

def source_others(root):

  source_other = []
  source_mod = source_mods(root)

  for f_name in os.listdir(root):                  # looks for all .f90 files
    if f_name.endswith(".f90"):
      source_other.append(f_name)

  source_other = list(set(source_other) - set(source_mod))  # removes _Mod.f90 from list

  return source_other

#===============================================================================
# List of all directories in root
#-------------------------------------------------------------------------------

def source_mod_dirs(root):

  source_mod_dir = []

  for f_name in os.listdir(root):
    if f_name.endswith("_Mod"):
      source_mod_dir.append(f_name)

  return source_mod_dir


#===============================================================================
# Prints all unused files and directories in root
#-------------------------------------------------------------------------------

def source_unused(root):


  source_mod_dir = source_mod_dirs(root)
  source_mod = source_mods(root)
  source_other = source_others(root)


  directories = [f for f in listdir(root) if isdir (join(root, f))]
  source_unused_dir = list(set(directories) - set(source_mod_dir))

  source_unused_file = []
  for f_name in os.listdir(root):
    source_unused_file.append(f_name)

  source_unused_file = list(set(source_unused_file)    \
                          - set(source_mod)            \
                          - set(source_mod_dir)        \
                          - set(source_other)          \
                          - set(source_unused_dir))

  print("\nUnused directories:\n",sorted(source_unused_dir), \
        "\n\nUnused files:\n",sorted(source_unused_file))

  return source_unused_file
