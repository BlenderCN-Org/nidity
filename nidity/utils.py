from pprint import pprint as pp

import bpy
from bpy.types import bpy_prop_collection


assert(pp)


def _iterate_props(obj):
    names = dir(obj)
    names = filter(lambda name: not name.startswith('_'), names)
    names = sorted(names)
    name_prop_tuples = map(lambda name: (name, getattr(obj, name)), names)
    return name_prop_tuples


def reset():
    for _, prop in _iterate_props(bpy.data):
        if isinstance(prop, bpy_prop_collection) and hasattr(prop, 'remove'):
            collection = prop
            if len(collection) == 1 and \
                    isinstance(collection[0], bpy.types.Scene):
                continue
            _remove_all(collection)


def _remove_all(collection):
    while collection:
        obj = collection[0]
        collection.remove(obj, do_unlink=True)


INDENT = '    '


def inspect(obj=bpy.data, label='@@@', depth=0, history=set()):
    print(INDENT * depth, end='')

    print('* %s: %s' % (label, obj))

    if obj in history:
        print(INDENT * (depth + 1), end='')
        print('* ...')
        return

    history.add(obj)
    if isinstance(obj, bpy.types.BlendData):
        for name, prop in _iterate_props(obj):
            inspect(prop, name, depth + 1, history)
    elif isinstance(obj, bpy.types.bpy_prop_collection):
        collection = obj
        index = 0
        for item in collection:
            inspect(item, '[%d]' % index, depth + 1, history)
            index += 1
    else:
        pass
    history.remove(obj)
