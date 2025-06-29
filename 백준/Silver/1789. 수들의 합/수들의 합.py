n = int(input())
sum = 0

result = 0

for i in range(1, n + 1): # 1부터 n까지 
    sum += i       # 현재 숫자 i를 sum에 더함 (누적합)
    result += 1    # 숫자 하나를 사용했으므로 개수(result) 증가
    
    if sum > n:    # 누적합이 입력값 n을 초과하면
        result -= 1  # 마지막에 더한 숫자는 초과했으므로 개수에서 제외
        break        # 반복문 종료 

print(result)
