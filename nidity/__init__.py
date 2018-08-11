import bpy

from . import files
from . import meshes
from . import utils

bpy.context.user_preferences.view.show_splash = False
assert files
assert meshes
assert utils

inspect = utils.inspect
pp = utils.pp
reset = utils.reset
