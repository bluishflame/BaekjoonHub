# N번째 종말의 수를 찾는 함수 정의

def find_end_number(n):
    cnt = 0       # 종말의 수를 찾은 개수 0으로 초기화 
    num = 666       # 종말의 수는 666부터 시작

    while True:
        # 현재 숫자에 '666'이라는 연속된 문자열이 포함되어 있는지 확인
        if '666' in str(num):
            cnt += 1  # 조건을 만족하면 카운트 증가

            # 원하는 N번째 종말의 수를 찾았으면 해당 숫자 반환
            if cnt == n:
                return num

        # 다음 숫자로 넘어감
        num += 1

n = int(input())

print(find_end_number(n))