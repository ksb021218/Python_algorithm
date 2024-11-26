def insertion_sort2(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        # A[j]와 A[j+1]를 비교하여 더 큰 값일 경우 스왑하면서 왼쪽으로 이동
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]  # A[j]와 A[j+1]을 스왑
            j -= 1


data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original  :", data)
insertion_sort2(data)
print("Insertion :", data)