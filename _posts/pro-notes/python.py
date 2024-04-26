matrix = [
    [1,2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [
    [row[colIndex] for row in matrix] 
    for colIndex in range(len(matrix))
]
print(transpose)