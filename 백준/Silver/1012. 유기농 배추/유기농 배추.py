import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1]  # 왼쪽, 오른쪽

# BFS 탐색 함수 정의
def bfs(x, y):
    """
    (x, y) 위치에서 시작해, 연결된 모든 배추를 방문 처리
    연결된 배추 무리 하나를 처리하면 지렁이 1마리가 필요함
    """
    queue = deque()          # BFS 탐색을 위한 Queue 생성
    queue.append((x, y))     # 시작 좌표 Queue에 추가
    matrix[x][y] = 0         # 시작 좌표 방문 처리 (0으로 바꾸어 다시 세지 않도록)

    while queue:
        x, y = queue.popleft()   # Queue에서 가장 먼저 들어온 좌표 꺼내기
        for i in range(4):       # 상, 하, 좌, 우 4방향 탐색
            nx = x + dx[i]       # 다음 탐색할 행 좌표
            ny = y + dy[i]       # 다음 탐색할 열 좌표

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
            # (1) 좌표가 밭 범위를 벗어나면 무시
                continue

            if matrix[nx][ny] == 1:
            # (2) 다음 위치에 배추가 있고 아직 방문하지 않았다면
                queue.append((nx, ny))  # 큐에 추가하여 나중에 탐색
                matrix[nx][ny] = 0      # 방문 처리 (0으로 바꿈)

T = int(input()) 
# 테스트 케이스 개수 입력

for _ in range(T):
    # M: 가로길이(열 개수), N: 세로길이(행 개수), K: 배추 개수
    M, N, K = map(int, input().split())

    # 밭 초기화: N행 M열, 모두 0으로 시작
    matrix = [[0] * M for _ in range(N)]

    # 배추 위치 입력
    # x = 열, y = 행이므로 matrix[y][x]에 1 표시
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    cnt = 0  # 필요한 지렁이 수 (배추 무리 개수)
    for i in range(N):
     # 모든 행과 열 탐색 
        for j in range(M):  
            if matrix[i][j] == 1:  # 배추 발견 시
                bfs(i, j)          # 연결된 배추 무리 모두 방문 처리
                cnt += 1           # 지렁이 한 마리 필요하므로 cnt 1증가 

    # 해당 테스트 케이스의 결과 출력
    print(cnt)
