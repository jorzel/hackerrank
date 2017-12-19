#!/bin/python3

"""
Objective 
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Task 
Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: n x i = result.

Input Format

A single integer, .

Constraints

Output Format

Print  lines of output; each line  (where ) contains the  of  in the form: 
n x i = result.
"""

import sys


n = int(input().strip())

for i in range(1, 11):
    print('{0} x {1} = {2}'.format(n, i,  i*n))