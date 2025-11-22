T = int(input())
nums = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
 
for test_case in range(1, T + 1):
    N, num_list = input().split()
    result = []
 
    for num in num_list:
        stack = []
        if num in nums:
            num = nums[num]
        else:
            num = int(num)
 
        for _ in range(4):
            stack.append(num % 2)
            num = num // 2
 
        result.append(stack[::-1])
 
    result_str = ''
    for i in result:
        result_str += ''.join(map(str, i))
    print(f"#{test_case} {result_str}")