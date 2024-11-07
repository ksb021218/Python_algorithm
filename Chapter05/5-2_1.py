def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid - 1)
        quick_sort(A, mid + 1, right)

def partition(A, left, right):
    low = left + 1  # 왼쪽 부분 리스트의 인덱스 (오른쪽으로 이동)
    high = right    # 오른쪽 부분 리스트의 인덱스 (왼쪽으로 이동)
    pivot = A[left] # 피벗 설정

    while low <= high:  # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
        
        if low < high:  # 선택된 두 요소를 교환
            A[low], A[high] = A[high], A[low]
    
    A[left], A[high] = A[high], A[left]  # 피벗과 high 요소 교환
    return high  # 피벗의 위치 반환

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("원래 배열:", data)
quick_sort(data, 0, len(data) - 1)
print("퀵 정렬된 배열:", data)
