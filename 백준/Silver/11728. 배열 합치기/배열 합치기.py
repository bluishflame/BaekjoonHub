N, M = map(int, input().split()) #배열 A의 크기 N과 배열 B의 크기 M을 입력받아 정수로 변환

A = list(map(int, input().split())) # 배열 A 입력받아 정수 리스트로 변환
B = list(map(int, input().split())) # 배열 B 입력받아 정수 리스트로 변환

C = A + B # 배열 A와 B를 합치기
C.sort() # 합쳐진 배열을 오름차순 정렬

result = ' '.join(map(str, C)) # 공백으로 구분된 문자열로 변환 

# 결과 출력
print(result)
