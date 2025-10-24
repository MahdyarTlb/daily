import random


def matrix_recursive(matrix):
    
    ## O(n!)
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    det = 0
    
    for j in range(n):
        minor = []
        
        for i in range(1, n):
            row = []
            
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
                    
            minor.append(row)
        sign = 1 if j % 2 == 0 else -1
        det += sign * matrix[0][j] * matrix_recursive(minor)
    
    return det

def matrix_gaussian(matrix):
    
    # O(n^3)
    n = len(matrix)
    
    mat = [row[:] for row in matrix]
    det = 1
    swaps = 0
    
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(mat[k][i]) > abs(mat[max_row][i]):
                max_row = k
        
        if max_row != i:
            mat[i], mat[max_row] = mat[max_row], mat[i]
            swaps += 1
            det *= -1
        
        if abs(mat[i][i]) < 1e-10:
            return 0
        
        det *= mat[i][i]
        
        for k in range(i + 1, n):
            factor = mat[k][i] / mat[i][i]
            for j in range(i + 1, n):
                mat[k][j] -= factor * mat[i][j]
    
    return det

def matrix_lu(matrix):

    # O(n^3)
    n = len(matrix)
    
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for k in range(i, n):
            sum_val = 0.0
            for j in range(i):
                sum_val += L[i][j] * U[j][k]
            U[i][k] = matrix[i][k] - sum_val
        
        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_val = 0.0
                for j in range(i):
                    sum_val += L[k][j] * U[j][i]
                if abs(U[i][i]) < 1e-10:
                    return 0
                L[k][i] = (matrix[k][i] - sum_val) / U[i][i]
    
    det = 1.0
    for i in range(n):
        det *= U[i][i]
    
    return det

def test_specific_matrix():
    print("test")
    print("=" * 40)
    
    test_matrix = [
        [2, -3, 1],
        [2, 0, -1],
        [1, 4, 5]
    ]
    
    for row in test_matrix:
        print(row)
    
    print(f"recursive: {matrix_recursive(test_matrix)}")
    print(f"gussian:   {matrix_gaussian(test_matrix)}")
    print(f"LU:      {matrix_lu(test_matrix)}")
    
if __name__ == '__main__':
    test_specific_matrix()