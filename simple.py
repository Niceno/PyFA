#===============================================================================
# Import libraries
#-------------------------------------------------------------------------------
import xfig
import finder
import browse
#===============================================================================
# Lists
#-------------------------------------------------------------------------------
root = "/home/simcic/Development/PyFA"
#filename = "Eddy_Mod.f90"
#filename = "Save_Vtk.f90"
files = browse.source_files(root)
#x0        = list(range(1, 1+len(files))) # upper left corner position on x axis
y0        = list(range(1, 1+len(files)))  # upper left corner position on y axis

box_widths = []
for i in range(len(files)):                    # box widths of all files
  box = xfig.choose_width(files[i])
  box_widths.append(box)

print(box_widths[:])

#===============================================================================
# Obviously the main function
#-------------------------------------------------------------------------------

print("\nGreat program for extracting UML from Fortran.\n")

# Open Xfig file
xf = open("flow.fig", "w")

# Write header out
xfig.write_header(xf)

# Plot module box
#xfig.plot(xf, X0, Y0, filename)

for i in range(len(files)):                    # plot all files in directory
  xfig.plot(xf, box_widths[i], y0[i], files[i])

#End
xf.close()
