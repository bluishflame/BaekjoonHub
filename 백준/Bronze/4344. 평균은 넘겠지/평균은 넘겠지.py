C = int(input()) # 테스트 케이스 개수 입력받기 

# 테스트 케이스 수만큼 반복
for _ in range(C):
    data = list(map(int, input().split())) # 한 줄의 입력을 정수 리스트로 변환
    N = data[0] # 첫 번째 값은 학생 수 N
    scores = data[1:] # 학생들 점수 리스트 슬라이싱...

    avg = sum(scores) / N  # 평균 점수 계산

    count = 0
    for score in scores: # 평균을 넘는 학생 수 세기 (조건에 맞는 점수만 세기)
        if score > avg:
            count += 1

    ratio = (count / N) * 100     # 비율 계산: 평균 넘는 학생 수 / 전체 학생 수 × 100

    print(f"{ratio:.3f}%")     # 결과를 소수점 셋째 자리까지 반올림해서 출력 
    
'''
1. 리스트 슬라이싱 scores = data[1:]
- 리스트에서 인덱스 1부터 끝까지 잘라서 새로운 리스트로 만든다 
- data[1:]은 첫 번째 (0번째 아님) 값을 제외하고 나머지를 가져옴 
- 입력 줄에 학생 수와 점수가 같이 들어오므로, data[0]은 학생 수 N, data[1:]은 학생 점수 리스트가 되게끔 분리

data = [5, 50, 50, 70, 80, 100]
scores = data[1:]
print(scores)  # 출력: [50, 50, 70, 80, 100]

2. 파이썬의 f-string (formatted string literal) 
- f"" 안에서 중괄호 {}로 변수를 넣고, 형식(format) 지정
- :.3f는 소수점 아래 3자리까지 보여주는 고정 소수점 형식(fixed-point) 이라는 뜻

ratio = 33.333333
print(f"{ratio:.3f}%")  # 출력: 33.333%

'''