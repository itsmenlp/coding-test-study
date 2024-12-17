# 소요시간 : 10분
# 시간복잡도 : O(N)
# 풀이: 투포인터, 골드 5
# https://www.acmicpc.net/problem/2467

N=int(input())

liquid=list(map(int,input().split()))

s,e=0,N-1
answer_s, answer_e=liquid[s],liquid[e]
answer=abs(liquid[s]+liquid[e])

while s<e:
    if abs(liquid[s]+liquid[e])<answer:
        answer=abs(liquid[s]+liquid[e])
        answer_s, answer_e=liquid[s],liquid[e]

        if answer==0: break
    
    if liquid[s]+liquid[e]<0:
        s+=1
    elif liquid[s]+liquid[e]>0:
        e-=1

print(answer_s, answer_e)
