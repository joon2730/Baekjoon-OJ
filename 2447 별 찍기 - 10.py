# https://www.acmicpc.net/problem/2447

# prints NxN blank cube on i_th row
def print_blank(N, i, canvas):
    if N == 1:
        canvas[i] += " "
    else:
        q = N // 3
        for j in range(3):
            for k in range(3):
                print_blank(q, i + (q * j), canvas)

# prints NxN star cube 
# N is a power of 3
# i <= len(canvas)
def print_star(N, i, canvas):
    if N == 1:
        canvas[i] += "*"
    else:
        q = N // 3
        for j in range(3):
            print_star(q, i, canvas)
        print_star(q, i + q, canvas)
        print_blank(q, i + q, canvas)
        print_star(q, i + q, canvas)
        for j in range(3):
            print_star(q, i + (q * 2), canvas)

N = int(input())
canvas = ["" for row in range(N)]
print_star(N, 0, canvas)

for i in range(len(canvas)):
    print(canvas[i])
