#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

This test compares all the terms of Pascal's Triangle, 
starting the term (0, 0) to the end (50, 50). The terms 
have been generated on the site http://mathforum.org/dr.cgi/pascal.cgi and 
stored in the file "50th_terms_list.txt".

The test is to run the implemented function and compare each 
value returned by the corresponding value in the list.

'''

import PascalTriangle

triangle = [[0 for x in range(51)] for y in range(51)]

i = 0

# Read list and storage the values
for value in open("50th_terms_list.txt"):
    line = value.rstrip('\n')

    if '#' in line:
        continue

    values = line.split(' ')

    for j in range(len(values)):
        if values[j] != '':
            triangle[i][j] = int(values[j])

    i += 1

# Execute function and compare results
for l in range(51):
    for c in range(l+1):
        res = PascalTriangle.pascalTriangle(l, c)
        if res == triangle[l][c]:
            #print str(res) + " = " + str(triangle[l][c])
            continue
        else:
            print "[ERROR] INCORRECT RESULT: Expected(" + str(triangle[l][c]) + ") Function Retorned(" + str(res) + ")"
            quit()

print "TEST FINISH SUCESSFULLY!"