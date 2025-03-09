'''
join 함수 
.join 리스트를 이용하면 매개변수로 들어온 리스트를 하나의 문자열로 합쳐서 반환 하는 함수 
'''

n = int(input())  # 파일 수 입력

dirname = list(input())  # 첫 번째 파일명 입력
dirname_len = len(dirname)  # 파일명 길이

for i in range(n - 1):  # 남은 파일 개수만큼 반복
    newname = list(input())  # 새로운 파일명 입력
    for j in range(dirname_len):  # 기존 파일명과 한 자리씩 비교
        if dirname[j] != newname[j]:  # 다르면 '?'로 변경
            dirname[j] = '?'

print(''.join(dirname))  # 리스트를 문자열로 변환 후 출력
