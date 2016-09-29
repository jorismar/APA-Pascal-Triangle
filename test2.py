#!/usr/bin/python
# -*- coding: utf-8 -*-

import PascalTriangle

MAX_TERM = 100

# <<<---------------
    # Example of <http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/>

# A Dynamic Programming based Python Program that uses table C[][]
# to calculate the Binomial Coefficient
 
# Returns value of Binomial Coefficient C(n, k)
def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
 
            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
# --------------->>>

for i in range(MAX_TERM+1):
    for j in range(i+1):
        # Execute example
        ex = binomialCoef(i, j)

        # Execute my implementation
        my = PascalTriangle.pascalTriangle(i, j)

        if ex == my:
            #print str(res) + " = " + str(triangle[l][c])
            continue
        else:
            print "[ERROR] INCORRECT RESULT: Expected(" + str(ex) + ") Function Retorned(" + str(my) + ")"
            quit()

print "TEST FINISH SUCESSFULLY!"