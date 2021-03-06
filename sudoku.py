#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from csp import Csp

def readints():
    ''' read integer input as format [x1x2x3x4x5...]
    '''
    return list(map(int, sys.stdin.readline().strip()))

def init_from_stdin():
    ''' read sudoku grid from stdin and return its CSP
    '''
    grid = [readints() for _ in range(9)]
    # variables[position] : domain
    variables = {(i, j): (range(1, 10) if grid[i][j] == 0 else [
        grid[i][j]]) for i in range(9) for j in range(9)}
    # constraints[position] : neq in rows / columns / block
    constraints = {(i, j): [(i2, j2) for i2 in range(9) for j2 in range(9) if (i != i2 or j != j2) and (
        i == i2 or j == j2 or ((i2 // 3 == i // 3) and (j2 // 3 == j // 3)))] for i in range(9) for j in range(9)}
    return Csp(variables, constraints)


def main():
    ''' read sudoku from stdin and stdout the solution
        - 81 variables in 9x9 problem with legal values domain
        - 81 variables with 20 constraints -> 1600 constraints (810 different edges)
    '''
    csp = init_from_stdin()
    csp.print_variables(csp.solve())

if __name__ == '__main__':
    main()
