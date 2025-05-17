'''
배열 x에서 서로 다른 두 수를 선택해 곱하고 그걸 모두 더한 값을 구해야 함 

result = 0
for i in range(n):
    for j in range(i + 1, n):
        result += x[i] * x[j]

단순 2중 for문은 시간 복잡도가 O(n²) 이기 때문에 시간초과가 뜸 
따라서 누적합 방식 (각 숫자*본인 뒤에 있는 모든 숫자의 합)의 구조로 해결해야 함 
'''

n = int(input())  # 원소 개수 입력
numbers = list(map(int, input().split()))  # 원소 리스트 입력

prefix_sum = []  # 누적합을 저장할 리스트
prefix_sum.append(numbers[0])  # prefix_sum[0] = numbers[0] 으로 초기화

total = 0  # 정답을 저장할 변수

# 누적합 배열 만들기
# prefix_sum[n-1] = 전체 합 
# prefix_sum[i] = numbers[0] + numbers[1] + ... + numbers[i]
# prefix_sum[n-1] - prefix[i] = i+1부터 n-1까지의 합, 즉 i 뒤에 있는 값들의 합 
for i in range(1, n):
    prefix_sum.append(prefix_sum[i-1] + numbers[i])

# 각 원소에 대해, 그 이후의 원소들과의 곱의 합을 계산
# numbers[i] * (numbers[i+1] + ... + numbers[n-1]) 를 누적
for i in range(n):
    total += numbers[i] * (prefix_sum[n-1] - prefix_sum[i])

# 최종 정답 출력
print(total)



