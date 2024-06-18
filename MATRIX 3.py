#Matrix 3

def diagonal_sum(matrix):
    n = len(matrix)
    diagonal1 = 0     #(from top-left to the bottom-right)
    diagonal2 = 0     #(from the top-right to the bottom-left)
    for i in range(n):
        diagonal1 += matrix[i][i]
        diagonal2 += matrix[i][n - 1 - i]
    return diagonal1, diagonal2

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diagonal1, diagonal2 = diagonal_sum(matrix)

print("Sum of diagonal elements (diagonal1): ", diagonal1)
print("Sum of diagonal elements (diagonal2): ", diagonal2)