import os

import bpy


def sandbox_dirpath():
    here = os.path.dirname(os.path.realpath(__file__))
    proj = os.path.join(here, '..')
    sdbx = os.path.join(proj, 'sandbox')
    sdbx = os.path.normpath(sdbx)
    return sdbx


def export_to_sandbox(filename):
    bpy.ops.wm.collada_export(
        'EXEC_DEFAULT',
        filepath=os.path.join(sandbox_dirpath(), filename),
    )
