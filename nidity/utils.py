from pprint import pprint as pp

import bpy
from bpy.types import bpy_prop_collection


assert(pp)


def reset():
    props = dir(bpy.data)
    props = filter(lambda p: not p.startswith('_'), props)
    props = filter(lambda p: p != 'scenes', props)
    for prop in props:
        datum = getattr(bpy.data, prop)
        if isinstance(datum, bpy_prop_collection) and hasattr(datum, 'remove'):
            collection = datum
            _remove_all(collection)


def _remove_all(collection):
    while collection:
        obj = collection[0]
        collection.remove(obj, do_unlink=True)
