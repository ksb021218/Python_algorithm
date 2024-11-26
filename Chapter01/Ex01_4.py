def union(A, B):
    """두 리스트 A와 B의 합집합을 구하는 함수"""
    return list(set(A) | set(B))  # 합집합: A ∪ B

def intersection(A, B):
    """두 리스트 A와 B의 교집합을 구하는 함수"""
    return list(set(A) & set(B))  # 교집합: A ∩ B

def difference(A, B):
    """두 리스트 A와 B의 차집합을 구하는 함수 (A - B)"""
    return list(set(A) - set(B))  # 차집합: A - B

# 예시 집합 A와 B
A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

# 합집합, 교집합, 차집합 계산
union_result = union(A, B)
intersection_result = intersection(A, B)
difference_result = difference(A, B)

# 결과 출력
print("A와 B의 합집합:", union_result)
print("A와 B의 교집합:", intersection_result)
print("A와 B의 차집합 (A - B):", difference_result)