from itertools import combinations

# 모음 리스트
vowels = set('aeiou')

# 입력 받기
L, C = map(int, input().split())
characters = input().split()

# 주어진 문자를 사전식으로 정렬
characters.sort()

# 가능한 모든 조합을 구하고, 조건을 만족하는지 확인
for combo in combinations(characters, L):
    # 모음과 자음 개수 세기
    vowel_count = sum(1 for c in combo if c in vowels)
    consonant_count = L - vowel_count  # 자음 개수는 전체에서 모음 개수를 뺀 값
    
    # 모음이 최소 1개, 자음이 최소 2개인 경우만 출력
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(combo))
