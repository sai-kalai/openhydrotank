#This is the main loop. It calls all the required

#global packages

#my packages

import sys, os, time

sys.path.append('E:\\Current Workspace\\Codebase\\hydrotank\\src')

sys.path.append('E:\\Current Workspace\\Codebase\\hydrotank\\src\\modbui')

sys.path.append('E:\\Current Workspace\\Codebase\\hydrotank\\src\\modbui\\routines')

#TODO shift routines to lowest level actions eg ger surface cut from list of curves or assign material to set

from routines import create_part, cut_face, assemble_parts, create_sets_surfs, assign_property, trivial, mesher

def main():

    start_time = time.time()

    create_part.main()
    print(time.time()-start_time, ' --- Created')

    cut_face.main()
    print(time.time() - start_time, ' --- Cut')

    assemble_parts.main()
    print(time.time() - start_time, ' --- Assembled')

    create_sets_surfs.main()
    print(time.time() - start_time, ' --- Sets and Surfaces')

    assign_property.main()
    print(time.time() - start_time, ' --- Properties')

    trivial.main()
    print(time.time() - start_time, ' --- Step, Load, Interaction')

    mesher.main()
    print(time.time() - start_time, ' --- Mesh')


if __name__ == '__main__':
    main()