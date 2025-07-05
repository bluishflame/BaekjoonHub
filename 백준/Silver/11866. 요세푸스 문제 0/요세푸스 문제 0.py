'''
원형 순환 구조를 표현하기 위해 큐(deque) 사용 
리스트의 요소를 앞에서 꺼내고 뒤로 보내는 작업 
'''

from collections import deque

N, K = map(int, input().split()) # N명의 사람, 제거하는 K번째 입력 
queue = deque(range(1, N + 1)) # 1부터 N까지 사람의 번호를 큐에 저장
result = [] # 결과 저장하는 리스트 result

# 요세푸스 순열 구하기 (큐를 이용해 원형 순회하면서 k번째 사람 제거 )
while queue:
    
    for _ in range(K - 1): 
        # k번째 사람을 제거하려면 앞에 있는 k-1명을 지나쳐야 하므로
        # k-1명을 큐 앞에서 꺼내서 뒤로 보내고 그 다음 사람(맨 앞사람)을 제거 
        queue.append(queue.popleft())
    
    result.append(queue.popleft()) # K번째 사람 제거

print("<" + ", ".join(map(str, result)) + ">")