# https://www.acmicpc.net/problem/14003

import bisect

def longest_increasing_subsequence(A):
    D = [None] * len(A) # listof length of LIS ends with element at corresponding index
    prev = [None] * len(A)
    mins_idx = []
    mins_val = []
    max_d_idx = 0
    max_d_val = 0

    for i, ele in enumerate(A):

        # find D[i]
        k = bisect.bisect_left(mins_val, ele) - 1
        if len(mins_val) <= k+1:
            D[i] = max_d_val + 1
            mins_idx.append(i)
            mins_val.append(A[i])
        elif k < 0:
            D[i] = 1
            mins_idx[0] = i
            mins_val[0] = A[i]
        else:
            D[i] = D[mins_idx[k]] + 1
            if (A[mins_idx[D[i] - 1]] > A[i]):
                mins_idx[D[i] - 1] = i
                mins_val[D[i] - 1] = A[i]

        # update max_d, max_d_idx
        if max_d_val < D[i]:
            max_d_val = D[i]
            max_d_idx = i

        # update prev
        prev[i] = mins_idx[k]

    sol = [None] * max_d_val
    i = max_d_idx
    for n in range(max_d_val):
        sol[max_d_val - n - 1] = A[i]
        i = prev[i]
    return (max_d_val, sol)


n = input()
A = list(map(int, input().split(" ")))
length, sol = longest_increasing_subsequence(A)
print(length)
print(*sol)
