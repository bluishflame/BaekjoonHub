L, P = map(int, input().split())  
num = list(map(int, input().split()))  

diff = []  

for i in range(5):  
    diff.append(num[i] - (L * P))

print(*diff)
