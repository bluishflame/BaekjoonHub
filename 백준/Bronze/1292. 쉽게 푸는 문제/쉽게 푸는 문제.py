'''
1. A, B 입력받기
2. B까지 필요한 수열 생성
3. 슬라이싱으로 A~B 부분 합산 
'''
A, B = map(int, input().split())

sequence = []

# B번째 숫자까지 수열 생성
# ex. 1 → 1번, 2 → 2번, 3 → 3번 ...
for i in range(1, B + 1):
    # i를 i번 반복해서 리스트에 추가
    sequence += [i] * i
    # 이미 B번째 이상까지 수열을 만들었다면 더 만들 필요 없음 → 중단
    if len(sequence) >= B:
        break

# A번째(A-1인덱스)부터 B번째까지 합산
result = sum(sequence[A - 1:B])

print(result)
