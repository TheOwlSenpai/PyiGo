# PyiGO test 1
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
class te(enum):
    n = 0
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

