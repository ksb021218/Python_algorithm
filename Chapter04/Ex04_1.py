def recursive_insertion_sort(A, n):
    # Base case: 리스트의 크기가 1인 경우 이미 정렬된 상태
    if n <= 1:
        return
    
    # n-1까지 재귀적으로 정렬
    recursive_insertion_sort(A, n - 1)
    
    # n번째 요소를 적절한 위치에 삽입
    key = A[n - 1]
    j = n - 2
    
    # key를 정렬된 부분에 삽입
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key
    
    printStep(A, n - 1)

def printStep(arr, val):
    print("  Step %2d = " % val, end='')
    print(arr)

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original  :", data)
recursive_insertion_sort(data, len(data))
print("Insertion :", data)