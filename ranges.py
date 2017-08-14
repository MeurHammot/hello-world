# -*- coding: ascii -*-
'''Range module

Special module for computing different ranges.
'''

import sys

class CustomRange(object):
    '''Class for parsing and computing simple ranges from string.'''
    def __init__(self, *args):
        """Initialize class with following parameters.

            @param expression (str): Users expression which will be
                parsed.
            @param var (str): Name of variable, which used in the
                expression.
            @param start (int): First value for variable with name
                stored in var.
            @param stop (int): Last value for variable with name
                stored in var.
        """
        if len(args) != 4:
            print "Incorrect argument quantity: You arguments" +\
                  " should be (expression, var, start, stop)."
            sys.exit(2)
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        try:
            self.start = float(args[2])
        except ValueError:
            print 'ValueError: Start must be number!' +\
                  '(expression, var, *start*, stop)'
            sys.exit(1)
        try:
            self.stop = int(args[3])
        except ValueError:
            print 'ValueError: Stop must be number!' +\
                  '(expression, var, start, *stop*)'
            sys.exit(1)
        if self.start > self.stop:
            print 'ValueError: Stop must be higher than start!' +\
                  '(expression, var, *start*, *stop*)'
            sys.exit(1)
        if len(args[1]) != 1:
            print 'ValueError: Var must be 1 charachter length!' +\
                  '(expression, *var*, start, stop)'
            sys.exit(1)
        self.expression = ''
        self.var = args[1]
        prev = ''
        ## Parsing expression
        for char in args[0]:
            try:
                self.expression = self.expression + str(int(char))
                prev = char
            except ValueError:
                if char == '^':
                    self.expression = self.expression + '**'
                elif char == self.var and prev in self.numbers:
                    self.expression = self.expression + '*self.' + char
                elif char == self.var:
                    self.expression = self.expression + 'self.' + char
                else:
                    self.expression = self.expression + char
                prev = char

    @staticmethod
    def awesome(is_awesome):
        '''Print if you are awesome.
            @param isawesome (bool): True, if you're awesome. False, if not.
        '''
        if is_awesome:
            print "You're awesome!"
        else:
            print "Someone can say that you are not awesome," \
                  " but it's %s!" % is_awesome

    def __iter__(self):
        '''Initializing iterator.'''
        self.__setattr__(self.var, self.start)
        return self

    def next(self):
        '''Returns next element in range.'''
        if self.__getattribute__(self.var) <= self.stop:
            try:
                result = eval(self.expression)
            except SyntaxError:
                print 'ValueError: Wrong expression!' +\
                  '(*expression*, var, start, *stop*)'
                sys.exit(1)
            self.__setattr__(self.var, self.__getattribute__(self.var) + 1)
            return result
        else:
            raise StopIteration
