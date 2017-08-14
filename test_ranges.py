# -*- coding: ascii -*-
'''Unit test module for module "ranges".'''

import unittest
from ranges import CustomRange

class TestCustomRange(unittest.TestCase):
    '''Class for unit testing CustomRange'''
    def testIteration(self):
        '''Comparing expected result with iteration result.'''
        values = []
        custom_range = CustomRange('(2.3n+n^(n+1))/2', 'n', 0, 3)
        for i in custom_range:
            values.append(i)
        self.assertEqual(values, [0.0, 1.65, 6.3, 43.95])

if __name__ == '__main__':
    unittest.main()
    