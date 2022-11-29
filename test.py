# author: TheOwl77

from enum import IntEnum


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
class te(IntEnum):
    n = 0
    s = 1
    g = 2
    b = 3

# CREATE THE BOARDS
if bd == 9:
    goban = [[0 for _ in range(bd+1)] for _ in range(bd+1)]
    for i in range(bd+1):
        for i2 in range(bd+1):
            if (i == 0 or i == bd+1) or (i2 == 0 or i2 == bd+1):
                goban[i][i2] = te.b

    lib = [[[False for _ in range(bd)] for _ in range(bd)] for _ in range(2)] # Liberties, array3d, cycle reset

    group = [[[0 for _ in range(bd)] for _ in range(bd)] for _ in range(2)] # numerating each existing group of stones, array3d, cycle reset

# FUNCTIONS 

def count(n): # doing range(1, n+1) is terrible to see
    return range(1, n+1, 1)

def printf(*n):
    print(*n, end="")

def printBoard():
    for i in count(bd):
        if i == 1:
            printf("    ")
            for i2 in count(bd):
                if i2 <= 9:
                    printf("%d.  " % i2)
                else:
                    printf("%d. " % i2)

        printf("\n%d.  " % (i))

        for i2 in count(bd):
            if goban[i][i2] == te.n:
                printf("+")
            elif goban[i][i2] == te.s:
                printf("◉")
            elif goban[i][i2] == te.g:
                printf("○")

            if i2 < bd:
                printf(" - ")
            else:
                printf("\n")
        
        if i < bd:
            printf("    |")
            for i2 in range(bd-1):
                printf("   |")

printBoard()


