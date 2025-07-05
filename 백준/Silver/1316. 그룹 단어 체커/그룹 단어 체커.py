N = int(input()) # 단어 개수 입력 

group_word = N # 처음엔 모든 단어가 그룹 단어라고 가정하고, 카운터 초기값을 N으로 설정

for i in range(N): # N개의 단어를 차례로 검사
    word = input()  # 한 단어 입력 받기

    # 단어 내에서 문자 인덱스 j를 0부터 끝에서 두 번째까지 순회
    for j in range(len(word) - 1):
        # 만약 현재 문자와 바로 다음 문자가 같으면
        if word[j] == word[j + 1]:
            # 연속된 문자이므로 문제없음, 계속 검사
            continue

        # 만약 현재 문자가 다음 문자 이후에도 다시 나온다면 (즉, 떨어져서 또 나타나면)
        elif word[j] in word[j + 1:]:
            # 그룹 단어 조건 위반이므로 카운터에서 1 빼고 검사 종료
            group_word -= 1
            break  # 이 단어는 그룹 단어가 아니므로 다음 단어로 넘어감

# 모든 단어 검사 후, 그룹 단어 개수 출력
print(group_word)
