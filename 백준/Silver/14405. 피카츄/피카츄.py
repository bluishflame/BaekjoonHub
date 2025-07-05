s = input() # 문자열 입력 

# replace를 이용하여 pi, ka, chu를 공백으로 변경 
s = s.replace("pi", " ")
s = s.replace("ka", " ")
s = s.replace("chu", " ")

# strip을 이용하여 문자열 길이가 0이면 yes, 아니면 no 출력 
if len(s.strip()) == 0:
    print("YES")
else:
    print("NO")