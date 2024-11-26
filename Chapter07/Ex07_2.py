def knapSack_dp(W, wt, val, n):
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]  # A 테이블 초기화
  
    for i in range(1, n + 1):  # 물건 번호
        for w in range(1, W + 1):  # 배낭의 용량
            if wt[i-1] > w:  # 물건 i가 배낭 용량을 초과하는 경우
                A[i][w] = A[i-1][w]  # 물건 i를 넣을 수 없으므로 이전 값 사용
            else:  # 물건 i를 넣을 수 있는 경우
                valWith = val[i-1] + A[i-1][w-wt[i-1]]  # 물건 i를 넣은 경우
                valWithout = A[i-1][w]  # 물건 i를 넣지 않은 경우
                A[i][w] = max(valWith, valWithout)  # 더 큰 값을 선택
  
    return A[n][W]  # 최종 결과 반환

# 물건 정보와 배낭 용량 설정
wt = [3, 2, 1, 4, 5]  # 물건들의 무게
val = [26, 20, 14, 40, 50]  # 물건들의 가치
W = 6  # 배낭의 용량
n = len(wt)  # 물건의 개수

# 동적 계획법 수행
result = knapSack_dp(W, wt, val, n)
print(f"최대 가치: {result}")