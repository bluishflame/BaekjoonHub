a, b = map(int, input().split())  # 두 개의 자연수를 입력

# 최대공약수(GCD, Greatest Common Divisor)를 구하는 함수
# 유클리드 호제법을 사용
def gcd(a, b):
    while b > 0:  # b가 0이 될 때까지 반복
        a, b = b, a % b  # a를 b로 나눈 나머지를 새로운 b로 설정
    return a  # b가 0이 되면 a가 최대공약수(GCD)

# 최소공배수(LCM, Least Common Multiple)를 구하는 함수
# 두 수의 곱을 최대공약수(GCD)로 나누면 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)  # (a × b) ÷ gcd(a, b)

print(gcd(a, b))  # 최대공약수 출력
print(lcm(a, b))  # 최소공배수 출력
