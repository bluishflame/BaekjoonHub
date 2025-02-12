'''
입력되는 연산식을 계산
소수점이 나올 경우 버림 연산 (floor division, //)을 사용 

eval() 함수 -> 문자열을 실제 파이썬 코드처럼 실행하는 함수
즉 문자열로 된 수식이나 코드를 입력받아서 실행 가능 
'''

if __name__ == '__main__':
    equation = '' # 수식을 저장하는 문자열 
    n = int(input()) # 수의 개수 N개 입력
    for _ in range(n + n - 1): # 총 2n-1 개의  입력
        equation += input() # 하나씩 문자열에 추가 
    equation = equation.replace('/', '//') # 나눗셈을 정수 나눗셈(버림 나눗셈)으로 변환 
    print(eval(equation)) # 수식 결과 출력 
