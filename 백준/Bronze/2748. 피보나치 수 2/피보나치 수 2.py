n = int(input()) # 정수 n 입력받기 
    
fibo = [0,1] # 피보나치 수열 처음 두 항을 fibo 리스트에 저장 

for i in range(2, n+1) : # 2번째부터 n번째까지 for문 돌려서 fibo 리스트에 추가
    fibo.append(fibo[i-1]+fibo[i-2]) # 현재 항은 바로 앞 두 항의 합 

print(fibo[n]) # n번째 피보나치 수 출력 