# def factorial(N):
#     if N == 1:
#         return 1
#     else:
#         return factorial(N - 1) * N
    
def factorial(N):
    res = 1
    for i in range(1, N+1):
        res *= i
    return res

n = int(input())
print(factorial(n))



