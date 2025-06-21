N = int(input()) # 거스름돈 금액 입력

count = 0 # 사용한 동전 개수 초기화

while N >= 0:
    # 현재 금액이 5로 나누어 떨어지는 경우 → 5원 동전으로 모두 거슬러 줄 수 있음
    if N % 5 == 0:
        count += N // 5  # 5원 동전 개수 추가
        print(count)     # 총 동전 개수 출력
        break
    # 그렇지 않으면 2원 동전 하나 사용
    N -= 2
    count += 1
else:
    print(-1)
