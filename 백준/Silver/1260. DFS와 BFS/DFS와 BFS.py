'''
# DFS (Depth-First Search)
- 깊이 우선 탐색
- 한 방향으로 끝까지 내려간 후 더 이상 갈 수 없으면 되돌아옴 (재귀적/스택적 탐색)
- 주로 재귀 함수 또는 스택(Stack) 으로 구현

개념 흐름:
1. 시작 노드 방문
2. 방문하지 않은 인접 노드 중 가장 작은 번호로 이동
3. 더 이상 이동할 곳이 없으면 직전 노드로 되돌아감
4. 모든 노드를 방문할 때까지 반복

# BFS (Breadth-First Search)
- 너비 우선 탐색
- 시작 노드에서 가까운 노드부터 차례차례 방문 (레벨 탐색)
- 주로 큐(Queue)로 구현 (FIFO)

개념 흐름:
1. 시작 노드 방문, 큐에 넣기
2. 큐에서 하나 꺼내고, 인접한 노드를 큐에 차례대로 넣음
3. 큐가 빌 때까지 반복
'''

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
