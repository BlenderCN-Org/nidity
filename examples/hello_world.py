import sys

import nidity


pp = nidity.pp

print('hello_world example')
nidity.reset()

pp(sys.version)
pp(dir())
pp(sys.path)
