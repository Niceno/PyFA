#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
import attribute
#===============================================================================
# Lists
#-------------------------------------------------------------------------------
root = "/home/simcic/Development/Synthetic-Eddies"

files = browse.source_files(root)      # list of all fortran files in root

x0    = xfig.x_pos(root)               # upper left corner positions on x axis
y0    = 1                              # upper left corner positions on y axis

#===============================================================================
# Collecting classes into lists
#-------------------------------------------------------------------------------
subroutines_list = []                     # initialize list
modules_list     = []                     # initialize list

for i in range(len(files)):
  module_name = finder.get_mod(files[i])  # find all modules from imported files

# If it is module then append to modules list
  if module_name != []:
    modules_list.append(attribute.module_class(files[i]))

# If it isn't module then append to subroutines list
  else:
    subroutines_list.append(attribute.subroutine_class(files[i]))

# Determine levels
mod_list = attribute.mod_lvl(modules_list)
sub_list = attribute.sub_lvl(subroutines_list,modules_list)

# Printing mods and subs
for i in range(len(mod_list)):
  print("\nModule name: ", mod_list[i].name,        \
        "\nLevel: ", mod_list[i].level,             \
        "\nModules used: ", mod_list[i].use)        \

for i in range(len(sub_list)):
  print("\nSubroutine name: ", sub_list[i].name,    \
        "\nLevel: ", sub_list[i].level,             \
        "\nModules used: ", sub_list[i].use)        \

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.")

# Check directories for errors
#browse.check_directories(root)

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot all fortran files in root
for i in range(len(files)):
  xfig.plot(xf, x0[i], y0, files[i])

# Print all unused files and subdirectories
#browse.source_unused(root)

#End
xf.close()
