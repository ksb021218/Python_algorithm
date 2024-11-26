def topological_sort(graph) :
    inDeg = {}              	# { 정점:진입차수 } 저장을 위한 공백 딕셔너리
    for v in graph :        	# 그래프의 모든 정점에 대해
        inDeg[v] = 0        	# 0으로 초기화. inDeg = { "A":0, "B":0, ... }
    for v in graph :        	# 모든 정점 v 에 대해
        for u in graph[v]:  	# v에 인접한 모든 정점 u에 대해
            inDeg[u] += 1   	# 진입차수를 1 증가시킴

    vlist = []              	# 진입차수가 0인 정점 리스트를 만듦
    for v in graph :
        if inDeg[v]==0 :		# 진입차수가 0이면 vlist에 추가
            vlist.append(v)
            
    while vlist :			 	# 리스트가 공백이 아닐 때 까지
        v = vlist.pop()     	# 진입차수가 0인 정점을 하나 꺼냄
        print(v, end=' ')   	# 화면 출력

        for u in graph[v] :	    # 연결된 정점의 진입차수 감소
            inDeg[u] -= 1		# 진입차수 감소
            if inDeg[u]==0 :	# 진입차수가 0이면 vlist에 추가
                vlist.append(u)

mygraph = {
    'A': ['D', 'E'],
    'B': ['D', 'F'],
    'C': ['F', 'G'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

print('topological_sort: ')
topological_sort(mygraph)
print()