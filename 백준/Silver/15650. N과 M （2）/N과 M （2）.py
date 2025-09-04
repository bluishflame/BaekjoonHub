'''
N과 M(1) -> 순서가 다른 순열 
N과 M(2) -> 순서가 달라도 같은 경우로 취급하는 조합 
1부터 N까지 자연수 중에서 M개를 고르는 모든 조합을 구하기 
'''

import sys

N, M = map(int, sys.stdin.readline().strip().split())
# N = 전체 숫자의 범위 (1부터 N까지)
# M = 뽑을 숫자의 개수

seq = [] # 현재까지 선택한 순열을 저장할 리스트 
output = [] # 최종 출력용 결과를 저장할 리스트 

def dfs(start) : 
    if len(seq) == M :
        output.append(' '.join(map(str, seq)))
        return 
    
    for i in range(start, N+1) : 
        # start 부터 N까지 순회, start 이상부터만 고르면 자동으로 오름차순
        seq.append(i) # 숫자 선택
        dfs(i+1) # 다음 재귀에서는 그 다음 숫자부터 선택 (중복 방지)
        seq.pop() # 선택 해제(백트래킹) 

dfs(1) # 처음에는 1부터 선택 가능하게 탐색 시작 

print('\n'.join(output))


'''
정리 

순열 -> 순서 중요, 모든 경우를 탐색 -> visited 필요 
조합 -> 순서 무시, 오름차순 강제 -> 이번 자리에서 선택 가능한 최소 숫자인 start로 다음 선택 제한 

'''