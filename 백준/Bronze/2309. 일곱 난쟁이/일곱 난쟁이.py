'''
1. 아홉 난쟁이의 키를 입력받기
2. 아홉 명 중 일곱 명을 선택하는 모든 경우를 탐색해 키의 합이 100 이 되는 경우 찾기
3. 찾은 경우 오름차순으로 출력 

1) 백트래킹 방법
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

'''
2) 브루트포스 방법

from itertools import combinations

short_men = [int(input()) for _ in range(9)]

# 9명 중에서 7명을 뽑는 모든 조합을 확인
for seven in combinations(short_men, 7):
    if sum(seven) == 100:  # 합이 100이면 정답
        for height in sorted(seven):  # 오름차순 정렬 후 출력
            print(height)
        break  # 종료


3) 9명 중에서 2명을 제거하는 방법 
1. 원래는 9명 중 7명을 선택하는 조합을 찾는 방식
2. 반대로, 9명의 총합에서 특정 2명을 빼면 합이 100이 되는 경우를 찾으면 됨 


# 1. 아홉 난쟁이의 키를 저장할 리스트 생성
arr = []
for _ in range(9):  # 9명의 난쟁이 키를 입력
    f = int(input())  # 입력값을 정수로 변환하여 저장
    arr.append(f)  # 리스트에 추가

# 2. 난쟁이 키를 오름차순 정렬
arr.sort()

# 3. 난쟁이 9명의 키 합을 구하기
sum_ = sum(arr)  # 전체 9명의 난쟁이 키 합
fake = []  # 가짜 난쟁이 2명을 저장할 리스트

# 4. 9명 중에서 2명을 골라서 합이 100이 되는지 확인
for i in range(9):  # 첫 번째 난쟁이 선택
    for j in range(i + 1, 9):  # 두 번째 난쟁이 선택 (중복 방지)
        if len(fake) == 2:  # 이미 가짜 난쟁이를 찾았다면 더 이상 탐색하지 않음
            continue

        if sum_ - arr[i] - arr[j] == 100:  # 두 명을 제외하면 합이 100이 되는지 확인
            fake.append(arr[i])  # 가짜 난쟁이 1명 추가
            fake.append(arr[j])  # 가짜 난쟁이 2명 추가

# 5. 가짜 난쟁이를 제외한 7명의 난쟁이를 출력
for i in arr:  # 9명의 난쟁이를 하나씩 확인
    if i in fake:  # 가짜 난쟁이에 포함된 경우 제외
        continue  # 출력하지 않고 넘어감
    print(i)  # 진짜 난쟁이만 출력 


'''
