from collections import deque

## BFS function
def bfs(matrix, N, M):
    need_visited = deque([]) 
    # 방문해야 하는 노드를 저장하는 Queue 선언 
    
    visited = [[False for _ in range(M)] for i in range(N)] 
    # NxM matrix에서 이미 방문한 노드에 대해 표시하기 위한 matrix
    # 방문한 곳에는 True 저장 
    
    distance = [[1 for _ in range(M)] for i in range(N)]
    # NxM matrix에서 해당 노드까지의 거리를 표시하는 matix
    # 이전까지의 노드와 distance를 합해 해당 노드의 distance를 계산 
    
    visited[0][0] = True
    # 시작 노드 방문 여부를 True로 변경 
    
    need_visited.append((0, 0))
    # 방문해야 하는 노드 Queue에 시작 노드를 입력 
    
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    # 상/하/좌/우로 이동하기 위한 dx, dy
    
    while need_visited: 
        # 방문해야 하는 노드를 dequeue하기
        # 이때, python의 경우, popleft를 사용해 가장 먼저 입력된 왼쪽부터 요소를 가져오기 
        x, y = need_visited.popleft()
        
        for i in range(4): 
        # 현재 위치 (x, y)에서 상/하/좌/우 확인 
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
            # (1) 나아갈 노드가 벽에 닿거나 범위를 넘지 않는지 확인 -> 무시 
                continue
                
            if visited[nx][ny] == False and matrix[nx][ny] == 1:
            # (2) 범위 내에 있는 노드라면 이미 방문했는지와 이동 가능한 노드인지 확인 
                need_visited.append((nx, ny))
                # 다음 방문할 좌표를 큐에 넣기 
                visited[nx][ny] = True
                # 방문 표시
                distance[nx][ny] += distance[x][y]
                # 거리 갱신 (현재 거리+1)
                
            if visited[nx][ny] == True and nx == N-1 and ny == M-1 :
            # (3) 범위 내에 있지만, 이미 방문한 경우 (예를 들어, 최종 도착까지의 경로가 n개 이상일 때)를 대비해 더 작은 distance가 저장되기
            # 여러 경로가 있을 수 있으므로 더 작은 값이 최종 거리 값으로 갱신 
                origin = distance[nx][ny]
                distance[nx][ny] = (distance[x][y]+1) if (distance[x][y]+1) < origin else origin 
                # 현재 경로가 더 짧으면 바꿔주기 
                
    return distance[N-1][M-1]
    # BFS 끝나면 도착점 (N-1, M-1)의 거리를 반환
    
N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input()))) 
    # 붙어서 입력되는 숫자들 int로 변환 
    
print(bfs(matrix, N, M))