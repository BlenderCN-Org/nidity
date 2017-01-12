import os

import bpy


def sandbox_dirpath():
    here = os.path.dirname(os.path.realpath(__file__))
    proj = os.path.join(here, '..')
    sdbx = os.path.join(proj, 'sandbox')
    sdbx = os.path.normpath(sdbx)
    return sdbx


###############################################################################
# export
###############################################################################

def export_to_sandbox(filename_without_ext):
    path = sandbox_dirpath()
    export_dae(path, filename_without_ext)
    export_x3d(path, filename_without_ext)
    export_3ds(path, filename_without_ext)
    export_fbx(path, filename_without_ext)


def export_dae(path, filename):
    bpy.ops.wm.collada_export(
        'EXEC_DEFAULT',
        filepath=os.path.join(path, filename + '.dae'),
    )


def export_x3d(path, filename):
    bpy.ops.export_scene.x3d(
        'EXEC_DEFAULT',
        filepath=os.path.join(path, filename + '.x3d'),
        name_decorations=False,
    )


def export_3ds(path, filename):
    bpy.ops.export_scene.autodesk_3ds(
        'EXEC_DEFAULT',
        filepath=os.path.join(path, filename + '.3ds'),
    )


def export_fbx(path, filename):
    bpy.ops.export_scene.fbx(
        'EXEC_DEFAULT',
        filepath=os.path.join(path, filename + '.ascii.fbx'),
        version='ASCII6100',
    )
    bpy.ops.export_scene.fbx(
        'EXEC_DEFAULT',
        filepath=os.path.join(path, filename + '.fbx'),
        version='BIN7400',
    )


###############################################################################
# import
###############################################################################

IMPORTERS = {
    '.dae': bpy.ops.wm.collada_import,
    '.x3d': bpy.ops.import_scene.x3d,
    '.3ds': bpy.ops.import_scene.autodesk_3ds,
    '.fbx': bpy.ops.import_scene.fbx,
}


def import_from_sandbox(filename):
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    importer = IMPORTERS.get(ext)
    if not importer:
        raise RuntimeError('unknown file extension: %s' % ext)
    importer(
        'EXEC_DEFAULT',
        filepath=os.path.join(sandbox_dirpath(), filename),
    )
