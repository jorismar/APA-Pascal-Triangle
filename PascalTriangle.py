#!/usr/bin/python
# -*- coding: utf-8 -*-

def pascalTriangle(line, column):
    l = line + 1
    c = column + 1

    triang = [[0 for x in range(c)] for y in range(l)]

    for i in range(l):
        for j in range(c):
            if i == j or j == 0:
                triang[i][j] = 1
                if i == j:
                    break
            else:
                triang[i][j] = triang[i-1][j-1] + triang[i-1][j]

    return triang[l-1][c-1]
