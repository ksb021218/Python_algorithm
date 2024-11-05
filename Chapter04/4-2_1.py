## 이진 탐색(순환구조) ##
def binary_search(A, key, low, high) :
    if (low <= high) :
        mid = (low + high) // 2
        if key == A[mid] :
            return mid
        elif key < A[mid] :
            return binary_search(A, key, low, mid-1)
        else :
            return binary_search(A, key, mid+1, high)
    return -1