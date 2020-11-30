matrix = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
            [0, 6, 2, 0, 5, 0, 0, 9, 0],
            [0, 7, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 6, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 2, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 5, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 2, 0, 0, 1, 0, 7, 5, 0],
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

sector = {0:[0,1,2],1:[3,4,5],2:[6,7,8]}


def validate(val,i,j,grid):
    for x in range(0,9):
        if grid[x][j] == val and i!=x:
            return False
    for x in range(0,9):
        if grid[i][x] == val and j!=x:
            return False
    p_i = (i//3)
    p_j = (j//3)
    for p in sector[p_i]:
        for q in sector[p_j]:
            if grid[p][q] == val and (i,j) != (p,q):
                return False
    return True

def construct(grid):
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] == 0:
                for k in range(1,10):
                    if validate(k,i,j,grid):
                        grid[i][j] = k
                        if construct(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True


def display(matrix):
    for i in range(9):
        if i%3 == 0 and i!=0:
            print("- - - - - - - - - -")
        for j in range(9):
            if j%3 == 0 and j!=0:
                print("|",end='')
            if j == 8:
                print(matrix[i][j])
            else:
                print(str(matrix[i][j]) + " ",end="")

if __name__ == "__main__":
    construct(matrix)
    display(matrix)
