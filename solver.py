#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mo Aug 10 12:42:22 2020

backtracking to solve sudoku

@author: jiahuali1991
"""

import numpy as np
'''
board1 = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

board2 = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]
'''




# 0 print board
# print(np.matrix(board1))

def print_board(bo):
    for i in range(len(bo)): # every 3 rows, print a horizontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])): # every 3 columns, print a vertical line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# print_board(board2)

# 1 pick empty
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None



# 2 try all numbers 

# 3 find one that works
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# 4 repeat

# 5 backtrack

def solve(bo):
    #print_board(bo) # print board everytime it calls the solve() function
    #print("___________________")
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)): # if a number is valid, plug in the nunmber into the board
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0 # if we cannot finish the solution by the numbers set already, change it back to 0 and go back to the last loop try another number

    return False
'''
print(np.matrix(board2))
solve(board2)
print("___________________")
print(np.matrix(board2))



# GUI


def possible(y,x,n):
    global board
    for i in range (9): # 
        if board[y][i] == n:
            return False
    for i in range (9):
        if board[i][x] == n:
            return False  
    x0 = (x//3)*3
    y0 = (x//3)*3
    for i in range (0,3):
        for j in range (0,3):
            if board[y0+i][x0+j] == n:
                return False      
    return True


def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] ==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print(np.matrix(board))
    input('More?')


solve() 

'''