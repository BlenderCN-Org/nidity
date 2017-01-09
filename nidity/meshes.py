import bpy


def add_mesh(name):
    mesh = bpy.data.meshes.new(name=name)
    return mesh
