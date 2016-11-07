import os
import sys

here_dir = os.path.dirname(os.path.realpath(__file__))
base_dir = os.path.join(here_dir, '..')
base_dir = os.path.normpath(base_dir)
sys.path.insert(0, base_dir)
import nidity  # noqa
assert nidity
