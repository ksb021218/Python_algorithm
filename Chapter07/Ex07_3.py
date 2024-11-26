def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for _ in range(m + 1)]  # 테이블 생성

    for i in range(m + 1):  # X의 길이
        for j in range(n + 1):  # Y의 길이
            if i == 0 or j == 0:
                L[i][j] = 0  # LCS가 없으면 0
            elif X[i - 1] == Y[j - 1]:  # X와 Y의 문자가 같으면
                L[i][j] = L[i - 1][j - 1] + 1
            else:  # X와 Y의 문자가 다르면
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L 테이블 출력
    for i in range(m + 1):
        print(L[i])

    print("LCS = ", lcs_dp_traceback(X, Y, L))

    return L[m][n]

def lcs_dp_traceback(X, Y, L):
    lcs = ""
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        v = L[i][j]
        if v > L[i][j - 1] and v > L[i - 1][j] and v > L[i - 1][j - 1]:
            i -= 1
            j -= 1
            lcs = X[i] + lcs  # 공통 부분문자열을 LCS에 추가
        elif v == L[i][j - 1] and v > L[i - 1][j]:
            j -= 1
        else:
            i -= 1
    return lcs

# 문제 풀이
X = "DATA STRUCTURE"
Y = "PYTHON ALGORITHM"
print("LCS Length:", lcs_dp(X, Y))
