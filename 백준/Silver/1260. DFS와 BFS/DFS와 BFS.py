from collections import deque


N, M, V = map(int, input().split())  # 정점 개수 N, 간선 개수 M, 시작 정점 V
graph = [[] for _ in range(N + 1)]   # 인접 리스트 (정점 번호 1부터 시작하므로 N+1)

# 간선 입력 처리 (양방향)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트를 오름차순 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS (재귀 함수 사용)

visited_dfs = [False] * (N + 1)   # 방문 여부 체크
dfs_result = []                   # 방문 순서 기록

def dfs(v):
    visited_dfs[v] = True         # 현재 노드 방문 표시
    dfs_result.append(v)          # 방문 순서 기록
    
    for nxt in graph[v]:          # 인접 노드 탐색
        if not visited_dfs[nxt]:  # 방문하지 않은 노드만 재귀 탐색
            dfs(nxt)


# BFS (큐 사용)

visited_bfs = [False] * (N + 1)   # 방문 여부 체크
bfs_result = []

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    
    while queue:
        node = queue.popleft()    # 큐에서 꺼내기
        bfs_result.append(node)   # 방문 순서 기록
        
        for nxt in graph[node]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)


# DFS, BFS 실행
dfs(V)
bfs(V)


print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))
