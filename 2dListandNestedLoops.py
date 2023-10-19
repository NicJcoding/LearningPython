# 2d list
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# [][] means Index- 0,1,2,3 - row then column when there are multiple list in a list
print(grid[1][1])

# Nested for loops - a for loop in a for loop
for row in grid:
    for col in row:
        print(col)


lists = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17,18,19,20],
    [21,22,23,24,25,26,27,28,29,30],
    [31,32,33,34,35,36,37,38,39,40]
]
for row in lists:
    print("This is the row: ")
    print(row)
    for col in row:
        print("this is the col: ")
        print(col)

# Can you get more numbers in a col?  If so, how?