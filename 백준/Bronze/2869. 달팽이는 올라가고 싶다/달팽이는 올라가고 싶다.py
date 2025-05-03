# 시간 제한이 0.15초 -> 반복문을 사용하면 안 됨 
'''
달팽이는 하루에 A - B 만큼 올라감.
(V - A) 높이까지는 밤에 미끄러지는 것까지 고려해야 함.
따라서 (V - A)를 하루에 오르는 A - B로 나눠서 며칠이 걸리는지 계산하고,
마지막 날 한 번 더 올라가서 정상 도달 -> 이때 마지막 날에는 미끄러지지 않으니 1번만 A미터 올라가면 됨 
'''

# A = 올라갈 수 있는 거리 , B = 미끄러지는 거리 , V= 나무막대 높이
# 올라가야 하는 거리 = V-B
# 달팽이는 낮에만 올라갈 수 있기 때문에 하루에 갈 수 있는 거리 = A - B
    
A, B, V = map(int, input().split()) # map 함수로 A, B, V 입력 

# (V - A): 마지막 날은 미끄러지지 않으므로, 이 높이까지만 반복
upperDay = A - B
target = V - A

# 올림 처리: 나누어떨어지지 않으면 +1

if target % upperDay == 0:
    days = target//upperDay
else:
    days = (target//upperDay) + 1

# 마지막 날 정상까지 올라가는 하루 추가
print(days + 1)
            
            
            
'''
# 올림처리 해서 나머지를 날려버리는 math.ceil 함수 
            
import math

A, B, V = map(int, input().split())

days = math.ceil((V - A) / (A - B)) + 1
print(days)
'''