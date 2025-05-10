'''
준현이랑 성민이가 주식투자하는 어쩌구

2021년 1월 1일부터 14일까지 주식 가격이 주어지고 
두 사람 중 1월 14일 기준으로 자산이 더 많은 사람이 이김 

BNP 전략 
- 매일 주식 살 수 있다면 가능한 한 많이 매수
- 절대 팔지 않음
- 보유 현금보다 주가가 낮으면 최대한 매수
- 장기 보유 -> 14일 마지막 날에 자산 계산

Timing 전략
- 매수 또는 매도는 전량
- 3일 연속 하락하면 주가가 오를 것으로 예상해서 전량 매수
- 3일 연속 상승하면 주가가 떨어질 것으로 예상해서 전량 매도
- 같은 가격은 상승/하락이 아님
- 매수 시 살 수 있을만큼만 매수 (현금부족하면 못 사)
    
자산은 현금+(보유 주식 수*14일차 주가)로 계산 
현재 가진 돈으로 살 수 있는 만큼의 주식을 사고 남은 돈을 갱신하는 코드 구현 
'''

n = int(input().rstrip())  # 초기 현금 입력
chart = list(map(int, input().rstrip().split()))  # 2021년 1월 1일부터 14일까지의 주가 입력

# BNP 전략 (Buy and Pray): 살 수 있을 때 무조건 최대한 매수하고 남은 돈 갱신 
bnp_cash = n       # 초기 현금
bnp_stock = 0      # 보유 주식 수

for price in chart:
    # 현재 현금으로 살 수 있는 만큼 주식 매수
    if bnp_cash >= price:
        bnp_stock += bnp_cash // price  # 주식 수 증가
        bnp_cash -= (bnp_cash // price) * price  # 사용한 돈 차감

# TIMING 전략
timing_cash = n     # 초기 현금
timing_stock = 0    # 보유 주식 수

# 3일 연속 가격 추이를 확인해야 하므로 4번째 날부터 시작
for i in range(3, 14):
    # 3일 연속 상승한 경우: 다음 날 하락을 예측하고 전량 매도
    if chart[i-3] < chart[i-2] < chart[i-1]:
        timing_cash += timing_stock * chart[i]  # 전량 매도
        timing_stock = 0  # 보유 주식 없음

    # 3일 연속 하락한 경우: 다음 날 상승을 예측하고 전량 매수
    elif chart[i-3] > chart[i-2] > chart[i-1]:
        if timing_cash >= chart[i]:  # 살 수 있는 경우에만 매수
            timing_stock += timing_cash // chart[i]  # 전량 매수
            timing_cash -= (timing_cash // chart[i]) * chart[i]

# 1월 14일 기준 총 자산 계산 (현금 + 보유 주식 × 마지막 날 주가)
final_price = chart[-1]
bnp_total = bnp_cash + bnp_stock * final_price
timing_total = timing_cash + timing_stock * final_price

# 결과 출력
if bnp_total > timing_total:
    print("BNP")
elif bnp_total < timing_total:
    print("TIMING")
else:
    print("SAMESAME")
