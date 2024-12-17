# 소요시간 : 20분
# 시간복잡도 : O(N^2)
# 난이도 실버 4, 레벨 2
# https://www.acmicpc.net/problem/18110
# 오래 걸린 이유 : n=0일 때 고려 X (경계값 주의), 추가 python에서의 round()함수 주의
# 주의!!! round() : 사사오입이 아니라, 오사오입(5 미만의 숫자는 내림, 5 초과의 숫자는 올림, 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림)



import sys
input=sys.stdin.readline

def round_r(num):
    if num - int(num)>=0.5:
        return int(num)+1
    else:
        return int(num)

n=int(input())


if n:
    data=[int(input()) for _ in range(n)]
    data.sort()

    if round_r(n*0.15):
        data=data[round_r(n*0.15):-round_r(n*0.15)]

    print(round_r(sum(data)/len(data)))

else:
    print(0)
