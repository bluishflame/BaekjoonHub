'''
1. M부터 N까지 모든 수를 범위 순회
2. 각 숫자 i에 대해 2부터 √i(제곱근)까지 나누어떨어지는 수가 있는지 확인 
   이때 나누어떨어지는 수가 없다면 소수로 판정 
3. 소수인 수만 리스트에 저장 
4. 소수 없으면 -1 출력, 있으면 합계(sum)과 최소값(min) 출력 
'''
m = int(input())  # 시작
n = int(input())  # 끝 

sosuList = []  # 소수 저장하는 sosuList 

# m부터 n까지 반복하면서 소수 판별
for i in range(m, n + 1):
    if i > 1:  # 1은 소수가 아니니까 제외하고 
        is_prime = True  # 소수 여부 판별용 변수 

        j = 2
        # 제곱근까지만 검사 (j * j <= i)
        '''
        어떤 수 n이 소수가 아니라면 반드시 n=aXb 형태이고 a와 b는 1과 n 사이의 자연수 
        a와 b 모두가 √n 보다 클 수는 없음 따라서 하나는 반드시 √n 이하이고 
        약수가 존재한다면 그 중 하나는 반드시 √n 이하에 있기에 √n까지만 확인하면 충분 
        '''
        while j * j <= i:
            if i % j == 0:    # 나누어 떨어지면 소수 아님 
                is_prime = False
                break         # 중단 
            j += 1

        if is_prime:  # 소수이면 리스트에 추가
            sosuList.append(i)


if len(sosuList) < 1:  # 소수가 하나도 없는 경우
    print(-1)
else:            # 소수가 하나라도 있는 경우
    print(sum(sosuList))  # 소수의 합 출력
    print(min(sosuList))  # 소수 중 최솟값 출력
