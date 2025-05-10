'''
반드시 모음(a, e, i, o, u)이 하나 이상 포함되어야 한다.
모음 3개 또는 자음 3개가 연속으로 오면 안 된다.
같은 글자가 두 번 연속으로 오면 안 된다.
단, 'ee', 'oo'는 허용된다.   
'''


def is_acceptable(password):
    vowels = 'aeiou'  # 모음 목록 정의

    # [조건 1] 모음이 하나라도 포함되어야 함
    if not any(char in vowels for char in password):
        # password 안에 모음이 하나도 없으면 False 반환
        return False

    # 모음과 자음의 연속 개수를 추적할 변수 초기화
    vowel_count = 0
    consonant_count = 0

    # 패스워드의 각 문자를 순회하면서 검사
    for i in range(len(password)):
        char = password[i]  # 현재 문자

        # 현재 문자가 모음인 경우
        if char in vowels:
            vowel_count += 1      # 모음 연속 개수 증가
            consonant_count = 0   # 자음 연속 개수는 초기화
        else:
            consonant_count += 1  # 자음 연속 개수 증가
            vowel_count = 0       # 모음 연속 개수는 초기화

        # [조건 2] 모음이나 자음이 3개 이상 연속되면 안 됨
        if vowel_count == 3 or consonant_count == 3:
            return False

        # [조건 3] 같은 글자가 연속으로 두 번 오면 안 됨
        # 단, 'ee'와 'oo'는 허용 예외
        if i > 0:  # 첫 문자는 이전 문자가 없으므로 제외
            if char == password[i - 1] and char not in ('e', 'o'):
                return False

    # 모든 조건을 만족하면 True 반환
    return True


while True:
    password = input().strip()  # 사용자로부터 입력받고 공백 제거

    # 입력이 'end'이면 종료
    if password == 'end':
        break

    # 비밀번호의 품질을 판별한 결과에 따라 출력
    if is_acceptable(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')

            
'''
any() 함수는 여러 개의 조건 중 하나라도 참(True)이면 참을 반환
all() 함수는 모든 조건이 참일 때만 참을 반환
'''
            