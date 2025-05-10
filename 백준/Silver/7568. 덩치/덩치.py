'''
각 사람은 (몸무게, 키)의 쌍으로 표현됨
A의 덩치가 B보다 크다는 조건은 A.몸무게 > B.몸무게 그리고 A.키 > B.키일 때만 성립.
자신의 덩치보다 더 큰 사람이 몇 명인지를 세고, 그 수에 1을 더한 것이 자신의 등수가 됨.
서로 비교할 수 없는 경우(한 쪽은 키가 크고 다른 쪽은 몸무게가 큰 경우)는 등수에 영향을 주지 않음

이중 반복문을 사용해서 모든 사람들끼리 덩치 비교를 함
자신보다 덩치가 더 큰 사람의 수를 세고 그 수에 +1을 해서 등수를 구함
등수는 1부터 시작하고 중복될 수 없음 
'''


# 사람들의 덩치 정보를 저장할 리스트
people = []

# 결과를 저장할 리스트
ranks = []

# 사람 수 입력
N = int(input())

# 각 사람의 몸무게와 키 입력받아 people 리스트에 튜플 혀태로 저장
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 각 사람마다 등수를 계산
for i in range(N):
    rank = 1  # 처음엔 모두 1등으로 시작

    for j in range(N):
        # 자기 자신은 비교하지 않음
        if i == j:
            continue

        # 나보다 몸무게와 키 모두 큰 사람이 있다면 등수 +1 (등수 내려감) 
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1

    # 계산된 등수를 결과 리스트에 추가
    ranks.append(rank)

# 결과 출력 (공백으로 구분)
print(" ".join(map(str, ranks)))
