test = int(input()) # 테스트 케이스 입력 받기 
    
for _ in range(test) : # test번 반복 
    floor = int(input()) # 층 수 입력 
    room = int(input()) # 호 수 입력 
    
    residents = [i for i in range(1, room+1)] # 0층 초기화 
    '''
    0층의 i호에는 i명이 살고 있음 -> ex. 5호까지면 1호:1명/2호:2명../5호:5명 이런 식이다 
    그걸로 리스트를 만들었다
    '''
    
    for _ in range(floor) : # 1층부터 floor층까지 반복 
        for i in range(1, room) : 
            residents[i]+=residents[i-1] # 현재 i 호에는 이전 사람 수+이전 후까지 누적해서 더하기
    '''
    매층의 i호의 거주민 수를 계산하는 방법은
    아래층 1호부터 i호까지 사람 수를 모두 합한 것 
    즉 현재 i호의 거주민 수 = 바로 앞(i-1)호까지의 누적+현재 i호의 기존 거주민 수 
    '''
            
    print(residents[room-1]) # floor층 room호 에 사는 사람 수 출력 
            
       
    
        