import sys, os

# import abaqus modules
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

import time

# import own modules
import routine_util as ru
import routine_constants as rc


def main():
    start_time = time.time()

    # ----- Step -----
    mdb.models[rc.MODEL].StaticStep(name=rc.STEP, previous='Initial',
                                    maxNumInc=rc.MAX_NUM_INC, initialInc=rc.INITIAL_INC, maxInc=rc.MAX_INC)

    # ----- Load & BC -----

    asm = mdb.models[rc.MODEL].rootAssembly

    if rc.LINER_TOGGLE == True:
        region = asm.instances[rc.LINER_INSTANCE].surfaces[rc.LOAD_SURF]
    elif rc.LINER_TOGGLE == False:
        region = asm.instances[rc.LAYUP_INSTANCE].surfaces[rc.LAYUP_INTERACTION_SURF]

    mdb.models[rc.MODEL].Pressure(name=rc.LOAD, createStepName=rc.STEP,
                                  region=region, distributionType=UNIFORM, field='', magnitude=rc.LOAD_MAG,
                                  amplitude=UNSET)

    asm = mdb.models[rc.MODEL].rootAssembly
    region = asm.sets[rc.SYM_BC_SET]
    mdb.models[rc.MODEL].YsymmBC(name=rc.BC, createStepName=rc.STEP,
                                 region=region, localCsys=None)

    region = asm.instances[rc.LAYUP_INSTANCE].sets[rc.LAYUP_SET]
    mdb.models[rc.MODEL].ZsymmBC(name=rc.BC2, createStepName=rc.STEP,
                                 region=region, localCsys=None)

    # ----- Interaction -----

    if rc.LINER_TOGGLE:
        mdb.models[rc.MODEL].ContactProperty('IntProp-1')
        mdb.models[rc.MODEL].interactionProperties['IntProp-1'].TangentialBehavior(
            formulation=FRICTIONLESS)
        mdb.models[rc.MODEL].interactionProperties['IntProp-1'].NormalBehavior(
            pressureOverclosure=HARD, allowSeparation=ON,
            constraintEnforcementMethod=DEFAULT)

        a = mdb.models[rc.MODEL].rootAssembly
        region1 = a.instances[rc.LAYUP_INSTANCE].surfaces[rc.LAYUP_INTERACTION_SURF]
        a = mdb.models[rc.MODEL].rootAssembly
        region2 = a.instances[rc.LINER_INSTANCE].surfaces[rc.LINER_INTERACTION_SURF]
        mdb.models[rc.MODEL].SurfaceToSurfaceContactStd(name='Int-1',
                                                        createStepName=rc.STEP, master=region1, slave=region2,
                                                        sliding=SMALL,
                                                        thickness=OFF, interactionProperty='IntProp-1',
                                                        adjustMethod=OVERCLOSED, initialClearance=OMIT, datumAxis=None,
                                                        clearanceRegion=None, tied=OFF)

    # ----- Job -----

    a = mdb.models[rc.MODEL].rootAssembly
    a.regenerate()
    mdb.Job(name='Job-1', model=rc.MODEL, description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
            scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=8,
            numDomains=8, numGPUs=2)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)





if __name__ == '__main__':
    main()
