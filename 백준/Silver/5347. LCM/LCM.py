''' 
두 수의 최소공배수(LCM) -> 두 수의 배수 중 가장 작은 수
최소공배수를 구할 때 두 수의 최대공약수를 이용하기
유클리드 호제법 -> 최대공약수 -> 최소공배수 

유클리드 호제법 -> a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수 
'''

# 두 수의 최대공약수(GCD) 구하기 (유클리드 호제법)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # a, b를 갱신: a는 b, b는 a를 b로 나눈 나머지로 바꿈
    return a  # b가 0이 되면 a가 최대공약수

# 두 수의 최소공배수(LCM) 구하기 
def lcm(a, b):
    # a와 b의 곱을 최대공약수로 나누면 최소공배수
    return a * b // gcd(a, b)

n = int(input())

for _ in range(n):
    line = input()
    a_str, b_str = line.strip().split()
    a = int(a_str)
    b = int(b_str)

    print(lcm(a, b))
