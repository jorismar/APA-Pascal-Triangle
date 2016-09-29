#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, PascalTriangle

if __name__ == '__main__':
    if len(sys.argv) == 3:
        l = int(sys.argv[1])
        c = int(sys.argv[2])
    elif len(sys.argv) > 1:
        print "Incorrect argument."
        quit()
    else:
        l = int(raw_input("Line: "))
        c = int(raw_input("Column: "))

    print PascalTriangle.pascalTriangle(l, c)
else:
	print "This class can not be imported."
