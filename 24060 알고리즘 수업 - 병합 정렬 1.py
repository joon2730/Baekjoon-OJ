def merge_sort(A, p, r, cnt, k): # A[p..r]을 오름차순 정렬한다.
    if p < r:
        q = (p + r) // 2;       # q는 p, r의 중간 지점
        cnt = merge_sort(A, p, q, cnt, k);      # 전반부 정렬
        cnt = merge_sort(A, q + 1, r, cnt, k);  # 후반부 정렬
        cnt = merge(A, p, q, r, cnt, k);        # 병합
    return cnt

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r, cnt, k):
    # print(A, p, q, r)
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i]) # tmp[t] <- A[i]; t++; i++;
            i += 1
        else:
            tmp.append(A[j]) # tmp[t] <- A[j]; t++; j++;
            j += 1
    
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j += 1
    i = p; t = 0
    while i <= r:  # 결과를 A[p..r]에 저장
        cnt += 1
        # print(cnt)
        if k == cnt:
            print(tmp[t])
        A[i] = tmp[t]
        i += 1
        t += 1
    return cnt

n, k = list(map(int, input().split()))
# lst = [4, 5, 1, 3, 2]
# print(lst)

lst = list(map(int, input().split()))
cnt = merge_sort(lst, 0, len(lst)-1, 0, k)
if cnt < k:
    print(-1)
# print(*lst)