import sys

import nidity


inspect = nidity.inspect
pp = nidity.pp

print('hello_world example')

inspect()
nidity.reset()
inspect()

pp(sys.version)
pp(dir())
pp(sys.path)
