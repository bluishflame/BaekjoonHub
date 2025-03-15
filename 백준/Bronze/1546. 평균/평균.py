n = input()
subjectList = list(map(int, input().split()))

subjectMax = max(subjectList)
sum = sum(subjectList)

print(sum*100/subjectMax/int(n))