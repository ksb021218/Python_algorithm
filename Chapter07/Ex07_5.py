def edit_distance(S, T, m, n):
    if m == 0: return n  # S가 공백이면 T의 모든 문자를 삽입
    if n == 0: return m  # T가 공백이면 S의 모든 문자를 삭제

    if S[m-1] == T[n-1]:  # 마지막 문자가 같으면 이 문자는 무시
        return edit_distance(S, T, m-1, n-1)

    # 세 연산을 모두 적용하여 최소값을 계산
    return 1 + min(edit_distance(S, T, m, n-1),  # 삽입
                   edit_distance(S, T, m-1, n),  # 삭제
                   edit_distance(S, T, m-1, n-1))  # 대체


def edit_distance_mem(S, T, m, n, mem):
    if m == 0: return n  # S가 공백이면 T의 모든 문자를 삽입
    if n == 0: return m  # T가 공백이면 S의 모든 문자를 삭제

    if mem[m-1][n-1] is None:  # 아직 계산되지 않았다면
        if S[m-1] == T[n-1]:  # 마지막 문자가 같으면
            mem[m-1][n-1] = edit_distance_mem(S, T, m-1, n-1, mem)
        else:
            mem[m-1][n-1] = 1 + min(
                edit_distance_mem(S, T, m, n-1, mem),  # 삽입
                edit_distance_mem(S, T, m-1, n, mem),  # 삭제
                edit_distance_mem(S, T, m-1, n-1, mem)  # 대체
            )
        print(f"mem[{m-1}][{n-1}] = {mem[m-1][n-1]}")  # 저장되는 값 출력

    return mem[m-1][n-1]  # 계산된 값 반환

# "HELLO WORLD" -> "GAME OVER" 변환
S = "HELLO WORLD"
T = "GAME OVER"
m = len(S)
n = len(T)
print("문자열: ", S, "->", T)

# 메모이제이션 테이블 초기화
mem = [[None for _ in range(n)] for _ in range(m)]

# 편집 거리 계산
result = edit_distance_mem(S, T, m, n, mem)
print("최소 편집 거리:", result)
