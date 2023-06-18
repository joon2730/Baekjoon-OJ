# https://www.acmicpc.net/problem/14003

def longest_increasing_subsequence(A):
    dp = [] # listof length of LIS ends with element at corresponding index
    prev = [] # listof index of previous element in LIS ends with element at corresponding index
    max_dp_i = 0 # index of element with maximum dp[i]
    min_val_is = [] # listof index of elements with minimum value for correspoinding value of dp
    for i in range(len(A)):
        dp.append(1)
        prev.append(0)

        # find dp[i]
        for min_i in reversed(min_val_is):
            if A[min_i] < A[i] and dp[i] < dp[min_i]+1:
                dp[i] = dp[min_i]+1
                prev[i] = min_i
                break

        # update min_val_is
        if len(min_val_is) <= dp[i]:
            min_val_is.append(i)
        elif A[min_val_is[dp[i]]] > A[i]:
            min_val_is[dp[i]] = i
    
        if dp[i] > dp[max_dp_i]:
            max_dp_i = i

        # print(min_val_is)
        # print(dp)
        # print(prev)
        # print("---------")
    # print(min_val_is)
# 5 0 5 2 3 5 1 2 3 4 1 2 3 0 4 5 1 2 4 2 5 9 0
    sol = []
    i = max_dp_i
    for n in range(dp[max_dp_i]):
        sol.append(A[i])
        i = prev[i]
    sol.reverse()
    return (dp[max_dp_i], " ".join([str(i) for i in sol]))

n = input()
A = list(map(int, input().split(" ")))
length, sol = longest_increasing_subsequence(A)
print(length)
print(sol)
