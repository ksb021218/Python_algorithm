def dfs(adjMat, vertex, start):
    n = len(vertex)  # 정점의 수
    visited = [False] * n  # 방문 여부 확인
    result = []  # 방문한 정점을 저장할 리스트

    # 재귀적으로 DFS 수행
    def dfs_recursive(v):
        visited[v] = True  # 현재 정점 방문 처리
        result.append(vertex[v])  # 방문 순서 기록
        # 인접 정점 탐색 (알파벳 순서로 탐색하기 위해 작은 인덱스부터)
        for i in range(n):
            if adjMat[v][i] == 1 and not visited[i]:  # 인접하고 방문하지 않은 정점
                dfs_recursive(i)

    # 시작 정점에서 DFS 시작
    start_index = vertex.index(start)
    dfs_recursive(start_index)
    return result

# 정점 리스트와 인접 행렬
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

# A를 시작 정점으로 DFS 실행
dfs_result = dfs(adjMat, vertex, 'A')
print("DFS 방문 순서:", dfs_result)