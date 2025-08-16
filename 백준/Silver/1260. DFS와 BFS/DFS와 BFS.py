from collections import deque

# DFS (재귀 방식으로 구현)
def dfs(graph, v, visited):
    visited[v] = True        # 현재 정점 방문 처리
    print(v, end=' ')        # 방문한 정점 출력
    for i in graph[v]:       # 현재 정점과 연결된 다른 정점들 확인
        if not visited[i]:   # 아직 방문하지 않은 정점이면
            dfs(graph, i, visited)  # 재귀적으로 DFS 수행

# BFS (큐 방식으로 구현)
def bfs(graph, start, visited):
    queue = deque([start])   # 시작 정점을 큐에 넣음
    visited[start] = True    # 시작 정점 방문 처리
    while queue:             # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 하나 꺼내기
        print(v, end=' ')    # 방문한 정점 출력
        for i in graph[v]:   # 현재 정점과 연결된 다른 정점들 확인
            if not visited[i]:       # 아직 방문하지 않은 정점이면
                queue.append(i)      # 큐에 추가
                visited[i] = True    # 방문 처리

# 입력 처리
N, M, V = map(int, input().split())  # 정점 수 N, 간선 수 M, 시작 정점 V
graph = [[] for _ in range(N + 1)]   # 인접 리스트 초기화 (1번부터 사용)

# 간선 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a와 b는 연결되어 있음 (양방향)
    graph[b].append(a)

# 각 정점의 인접 리스트 정렬 (작은 번호부터 방문하기 위해)
for i in range(1, N + 1):
    graph[i].sort()

# DFS 실행
visited = [False] * (N + 1)  # 방문 기록 초기화
dfs(graph, V, visited)
print()  # 줄 바꿈

# BFS 실행
visited = [False] * (N + 1)  # 방문 기록 다시 초기화
bfs(graph, V, visited)
