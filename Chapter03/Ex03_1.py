def sort_balls(A):
    n = len(A)
    swaps = 0
    for i in range(n):
        for j in range(n - 1):
            # 흰 구슬(0)이 검은 구슬(1)보다 오른쪽에 있으면 교환
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps += 1
    return A, swaps

# 예제 리스트
A = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]

# 함수 실행
sorted_A, total_swaps = sort_balls(A)
print("정렬된 리스트:", sorted_A)
print("총 교환 횟수:", total_swaps)
