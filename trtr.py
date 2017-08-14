#!/usr/bin/env python2.7
# -*- coding: ascii -*-
'''Running module'''

import sys
from ranges import CustomRange
try:
    rng = CustomRange(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    for i in rng:
        print i
except IndexError:
    if len(sys.argv) == 1:
        print 'Input error: Missing arguments!\n' +\
              '\t(expression, var, start, stop)\n' +\
              '\t     ^        ^     ^      ^'
    elif len(sys.argv) == 2:
        print 'Input error: Missing arguments!\n' +\
              '\t(expression, var, start, stop)\n' +\
              '\t              ^     ^      ^'
    elif len(sys.argv) == 3:
        print 'Input error: Missing arguments!\n' +\
              '\t(expression, var, start, stop)\n' +\
              '\t                    ^      ^'
    elif len(sys.argv) == 4:
        print 'Input error: Missing arguments!\n' +\
              '\t(expression, var, start, stop)\n' +\
              '\t                           ^'
    sys.exit(2)
    