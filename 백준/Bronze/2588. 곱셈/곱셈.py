'''
나눗셈(//)과 나머지(%) 연산이 나오는 이유는 곱셈 과정에서 자리수를 분리하기 위해서 
곱셈의 원리 -> 각 자리 별로 곱셈을 수행하고 그 결과를 자리값에 맞춰 더하는 방식 

472
× 385
-----
2360  (472 × 5)  ← 1의 자리
3776  (472 × 8)  ← 10의 자리
1416  (472 × 3)  ← 100의 자리
-----
181720  (최종 결과)

이 과정을 코드로 구현하려면 각 자리 숫자를 추출해야 한다 

'''


# 1) 나머지를 구하는 %을 이용하여 값을 바로 출력하는 방법

num1 = int(input())
num2 = int(input()) 

# 입력된 숫자 num2를 나머지 연산 %과 정수 나눗셈 // 을 통해 각 자리 숫자를 분리 
print(num1 * (num2%10)) # 1의 자리 숫자 
print(num1 * ((num2%100)//10)) # 10의 자리 숫자 
print(num1 * (num2//100)) # 100의 자리 숫자 
print(num1 * num2) # 각 자리 숫자와 num1을 곱한 결과를 한 줄씩 출력 


# 2) range(시작, 마지막, 순서) 함수를 이용해 마지막부터 시작까지 역순으로 출력하는 방법

num1 = int(input()) 
num2 = input() 

# num2를 문자열로 처리해 각 자리 숫자에 접근 
for i in range(len(num2), 0, -1):	# range를 사용해 len(num2)부터 1까지 역순으로 반복 
    print(num1 * int(num2[i-1])) # num2[i-1] 을 사용해 오르쪽에서 왼쪽으로 각 자리 숫자를 차례로 가져옴 

print(num1 * int(num2)) # 각 자리 숫자와 num1을 곱한 결과를 한 줄씩 출력 


# 3) 결과값을 list 변수에 담고, 출력하는 방법

num1 = int(input())
num2 = list(map(int, input()))

result = []

for i in range(len(num2), 0, -1):
  result.append(num1 * num2[i-1])

print(result[0], result[1], result[2], sep='\n')
print(result[0]+(result[1]*10)+result[2]*100)

