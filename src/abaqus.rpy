# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-12.49.31 163176
# Run by simon on Tue May 23 09:25:41 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=99.6614532470703, 
    height=106.430557250977)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('build_model.py', __main__.__dict__)
#* IOError: (2, 'No such file or directory', 'liner.csv')
#* File "build_model.py", line 19, in <module>
#*     from routines import thickness, create_part, cut_face, assemble_parts, 
#* create_sets_surfs, assign_property, \
#* File "C:\Users\simon\codebase\hydrotank\src\routines\thickness.py", line 36, 
#* in <module>
#*     liner = np.loadtxt(open(alt_filename), delimiter=",", skiprows=1)