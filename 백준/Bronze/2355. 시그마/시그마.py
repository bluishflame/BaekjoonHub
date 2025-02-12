'''
두 정수 A, B가 주어지고 A와 B 사이에 있는 모든 정수의 합을 구하기
A와 B 또한 포함 
A와 B의 순서는 상관 X 
'''

a, b = map(int, input().split()) # a, b 입력받아서 두 정수로 변환 

max_value = max(a, b) # a, b 중 더 큰 값 
min_value = min(a, b) # a, b 중 더 작은 값 

sum = (a + b) * (max_value - min_value +1) / 2 # 등차수열의 합 
print(int(sum)) # 정수형 변환 후 출력 
