#!/usr/bin/env python2.7
# -*- coding: ascii -*-
'''Running module'''

import sys
from ranges import CustomRange

if len (sys.argv) > 1 and sys.argv[1] == '--help':
    print "Usage: ./trtr.py EXPRESSION VARIABLE START" +\
          " STOP\n" +\
          "./trtr.py computing defined range for EXPRESSION with" +\
          " custom VARIABLE from START value for variable to" +\
          " STOP.\n\n" +\
          "Example:\n" +\
          "  ./trtr.py '2n+1' n 0 10\t#Computing range for" +\
          " 2n+1 with variable n from 0 to 10 including.\n\n" +\
          "Options:\n  --help - shows help"
    sys.exit(0)
if len (sys.argv) != 5:
    if len(sys.argv) == 1:
        print 'Missing arguments: expression, variable name,' +\
              ' start and stop values for variable.'
    elif len(sys.argv) == 2:
        print 'Missing arguments: variable name, start' +\
              ' and stop values for variable.'
    elif len(sys.argv) == 3:
        print 'Missing arguments: start and stop values for variable.'
    elif len(sys.argv) == 4:
        print 'Missing arguments: stop value for variable.'
    elif len(sys.argv) > 5:
        print 'Too many arguments.'
    print '\nType \'./trtr.py --help\' to get more information' +\
          ' about usage.'
    sys.exit(2)
rng = CustomRange(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
if '.' in sys.argv[1] or '.' in sys.argv[3]:
    tp = float
else:
    tp = int
for i in rng:
    if tp == float:
        print '%0.3f' % i
    else:
        print '%d' % i