'''
1. 아홉 난쟁이의 키를 입력받기
2. 아홉 명 중 일곱 명을 선택하는 모든 경우를 탐색해 키의 합이 100 이 되는 경우 찾기
3. 찾은 경우 오름차순으로 출력 
'''

shortMen = [int(input())for _ in range(9)] # 아홉 난쟁이의 키 입력
sevenShort = [] # 7명을 뽑아 합을 조사할 새로운 리스트 선언

def dfs(depth, start) : 
    if depth == 7 : # 7명을 뽑았다면 
        if sum(sevenShort) == 100 : # 7명 키의 합이 100이면 정답 
            for j in sorted(sevenShort) : # 정답 오름차순 출력 
                print(j) 
            exit()
        else:
            return 
    
    # 백트래킹 : 9명 중 7명을 뽑는 모든 조합 찾기 
    for i in range(start, len(shortMen)) : # 난쟁이 9명 중 7명 뽑는 조합 찾기
        sevenShort.append(shortMen[i]) # 난쟁이 한 놈 추가
        dfs(depth+1, i+1) # 다음 난쟁이 선택을 위해 dfs 호출
        sevenShort.pop() # 탐색 후 원래 상태로 되돌리기(cuz 백트래킹)
        
dfs(0, 0)
