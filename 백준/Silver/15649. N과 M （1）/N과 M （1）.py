'''
N개의 자연수 중 M개를 선택해 만들 수 있는 모든 순열을 출력 
출력은 사전 순(오름차순 정렬된 순서)

백트래킹 -> 모든 가능한 경우를 탐색하되, 조건에 맞지 않으면 되돌아가는 것 
-> 1...N까지 중복없이 M개를 뽑는 순열이기 때문에 백트래킹 가능 
'''

import sys 
input = sys.stdin.readline 

N, M = map(int, input().split()) 
# N = 전체 숫자의 범위(1부터 N까지)
# M = 선택할 수열의 길이 

visited = [False] * (N+1) 
# 중복 방지용으로 방문 여부 체크 

seq = []
# 현재까지 만든 수열을 저장하는 리스트

output = [] 
# 최종 출력할 결과 모아두는 리스트 

# dfs 함수 -> 현재까지 만든 수열 seq를 바탕으로 남은 M자리까지 채워가기 
def dfs() : 
    if len(seq) == M : # 수열 길이가 M이 되면 출력용 리스트에 추가 
        output.append(' '.join(map(str, seq))) 
        return 
    
    for i in range(1, N+1) : # 1부터 N까지 숫자를 차례대로 확인 
        if not visited[i] : # 아직 사용하지 않은 숫자면 선택 가능 
            visited[i] = True # 숫자 사용 표시
            seq.append(i) # 수열에 숫자 추가 
            
            dfs() # 재귀 호출 -> 다음 자리에 숫자 넣기 
            
            seq.pop() # 백트래킹으로 마지막에 넣은 수자 제거하고 
            visited[i] = False # 다시 사용 가능하게 표시
            
dfs() # 탐색 시작하고

print('\n'.join(output)) # 결과 출력 