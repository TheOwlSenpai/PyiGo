# author: TheOwl77

from enum import Enum

# GLOBAL
bd = 9
none = 0
sente = 0
gote = 0

move = [0, 0]
i_move = "\0\0"

tegoma = [181, 180]
captured = [0, 0]

# ENUMS
class te(Enum):
    none = 0
    s = 1
    g = 2
    b = 3

# CREATE THE BOARDS
if bd == 9:
    goban = [[0 for _ in range(bd+1)] for _ in range(bd+1)]
    for i in range(bd+1):
        for i2 in range(bd+1):
            if (i == 0 or i == bd) or (i2 == 0 or i2 == bd):
                goban[i][i2] = te.b

    lib = [[[False for _ in range(bd)] for _ in range(bd)] for _ in range(2)] # Liberties, array3d, cycle reset

    group = [[[0 for _ in range(bd)] for _ in range(bd)] for _ in range(2)] # numerating each existing group of stones, array3d, cycle reset

# FUNCTIONS 
def printBoard():
    for i=1 in range(bd):
        if i == 1:
            print("\t")
            for i2=1 in range(bd):
                if i2 <= 9:
                    print(i2 + ".  ")
                else:
                    print(i2 + ". ")

        print(i + ".\t")

        for i2=1 in range(bd):
            match goban[i][ii2]:
                case te.none:
                    print
            if i2 < d:
                print(" - ")
            else:
                print("\n")
        
        if i < bd:
            print("\t|")
            for i2 in range(bd-1):
                print("   |")