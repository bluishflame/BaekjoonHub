'''
JOI 시는 HxW 크기
각 구역(i,j)는 구름이 있거나 없거나
구름은 매 1분마다 1칸씩 동쪽(오른쪽)으로 이동
각 구역에 구름이 있는지 주어졌을 때 몇 분 뒤 처음으로 구름이 오는지 출력
1. 구름이 이미 있으면 0
2. 구름이 절대 오지 않으면 -1
3. 구름이 오면 처음 오는 시간 출력

구름은 처음 위치->동쪽
한 행에서 구름은 오른쪽으로만 이동 -> 구름이 없는 칸은 구름이 지나갈 때까지 기다리기
'''

H, W = map(int, input().split()) # 행과 열 입력 
arr = [input() for _ in range(H)] # 각 행 마다 구름 상태 입력 

for a in arr:
    lst = [-1] * W  # 결과 리스트를 -1로 초기화, -1은 구름이 절대 오지 않는 곳 표시
    
    for i in range(W): # 현재 위치에 구름이 있으면 0으로 표시 (현재부터 구름 존재)
        if a[i] == 'c':
            lst[i] = 0
            
    for i in range(1, W): # 왼쪽에서 오른쪽으로 한 칸씩 이동하며 구름 도착 시간 계산
        # 현재 칸에 구름이 없고, 왼쪽 칸에 구름 도착 시간이 있다면
        if lst[i] != 0 and lst[i - 1] != -1:
            # 왼쪽 칸 도착 시간에 1분 더해 현재 칸에 저장
            lst[i] = lst[i - 1] + 1

    print(*lst) 
    
'''
*lst 는 리스트를 풀어서 각각의 원소를 공백으로 구분해 출력하는 문법 
'''

            
     