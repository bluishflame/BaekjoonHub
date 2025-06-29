test = int(input())  # 테스트 케이스 수

for _ in range(test):
    A = list(map(int, input().split()))
    A_sorted = sorted(A, reverse=True)  # 내림차순 정렬
    print(A_sorted[2])  # 세 번째 큰 값 출력 (인덱스 2)