import sys
from collections import deque
input = sys.stdin.readline

N = int(input())  # N x N 정사각형 지도 입력 

graph = []  # 지도를 저장할 2차원 리스트 초기화 
result = []  # 각 단지별 집의 수를 저장할 리스트 초기화 

for _ in range(N):
    # 한 줄씩 입력받아 '0'과 '1'로 이루어진 리스트 지도 변환
    # rstrip()으로 오른쪽 개행 제거
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]  
dy = [1, -1, 0, 0] 
# 상하좌우 이동 

# BFS 함수 정의
def bfs(graph, a, b):
    """
    (a, b) 위치에서 BFS를 시작하여 연결된 모든 집을 탐색하고
    탐색한 집의 수를 반환
    """
    queue = deque()  # BFS용 큐 생성
    queue.append([a, b])  # 시작 좌표를 큐에 추가
    graph[a][b] = 0  # 시작 집 방문 처리 (0으로 바꿔서 다시 세지 않도록)
    count = 1  # 시작 집 방문했으므로 count = 1

    while queue:
        x, y = queue.popleft()  # 큐에서 좌표 꺼내기
        graph[x][y] = 0        

        # 현재 좌표에서 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]  # 이동 후 행 좌표
            ny = y + dy[i]  # 이동 후 열 좌표

            # (1) 지도 범위를 벗어나면 무시
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            # (2) 다음 좌표에 집이 있고 아직 방문하지 않았다면
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0          # 방문 처리
                queue.append([nx, ny])     # 큐에 추가하여 다음에 탐색
                count += 1                 # 단지 내 집 수 증가

    return count  # BFS가 끝나면 해당 단지 집 수 반환


for i in range(N):     
    for j in range(N):  
    # 지도 전체의 모든 행과 열 순회하면서 단지 탐색
        if graph[i][j] == 1:      # 집 발견 시
            count = bfs(graph, i, j)  # BFS로 단지 탐색
            result.append(count)       # 단지 집 수 저장

result.sort()          
print(len(result))      
for k in result:       
    print(k)
