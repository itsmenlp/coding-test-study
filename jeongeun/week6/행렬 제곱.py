def matrix_mul(A, B, mod=1000):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod
                
    return result

def matrix_pow(A, B, mod=1000):
    n = len(A)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = A
    
    while B > 0:
        if B % 2 == 1:
            result = matrix_mul(result, base, mod)
        base = matrix_mul(base, base, mod)
        B //= 2
        
    return result

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = matrix_pow(A, B)

for row in result:
    print(*row)
