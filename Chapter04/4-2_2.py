## 이진 탐색(반복구조) ##
def binary_search_iter(A, key, low, high) :
    while(low <= high) :
        mid = (low + high) // 2
        if key == A[mid] :
            return mid
        elif key > A[mid] :
            low = mid + 1
        else :
            high = mid -1
    return -1