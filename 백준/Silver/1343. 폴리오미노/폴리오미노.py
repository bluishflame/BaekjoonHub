board = input()

result = []

count = 0 # 연속된 'X'의 개수를 세는 변수

# 보드 문자열을 한 글자씩 확인
for ch in board:
    if ch == 'X':
        count += 1  # 연속된 X 개수 증가
    else:
        # 'X'가 끝나고 '.'을 만난 경우, 앞의 X 덩어리를 처리
        if count % 2 != 0:
            print(-1)  # 덮을 수 없는 경우
            exit()
        # AAAA 블록으로 가능한 만큼 채우고, 남은 2칸은 BB로 채움
        result.append('AAAA' * (count // 4) + 'BB' * ((count % 4) // 2))
        result.append('.')  # '.'은 그대로 유지
        count = 0  # X 덩어리 길이 초기화

# 반복이 끝났는데 남은 X가 있는 경우 처리
if count:
    if count % 2 != 0:
        print(-1)
        exit()
    result.append('AAAA' * (count // 4) + 'BB' * ((count % 4) // 2))

# 결과 리스트를 문자열로 합쳐 출력
print(''.join(result))
