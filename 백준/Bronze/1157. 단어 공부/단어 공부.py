word = input().upper()  # 문자열 입력받아 대문자로 변환
wordlist = list(set(word))  # 중복 제거하여 알파벳 리스트 생성
cnt = []  # 알파벳 등장 횟수 저장하는 리스트

# 각 알파벳 등장 횟수를 계산
for char in wordlist:
    count = word.count(char)  # 특정 알파벳 등장 횟수를 세기
    cnt.append(count)  # cnt 리스트에 추가

maxcount = max(cnt)  # 등장 횟수가 가장 많은 값 찾기

# 등장 횟수가 같은 최댓값이 여러 개 있는지 확인
if cnt.count(maxcount) > 1:  # 최댓값이 2개 이상이면
    print('?')  # '?' 출력
else:
    # 가장 많이 등장한 알파벳 출력
    print(wordlist[cnt.index(maxcount)])
