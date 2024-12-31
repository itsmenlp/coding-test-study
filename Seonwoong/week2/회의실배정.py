import sys
input=sys.stdin.readline

n=int(input())
dict=[]
for i in range(n):
    s, e=map(int, input().split())
    dict.append([s,e])

dict1=sorted(dict, key=lambda x: (x[1], x[0]))

cnt=1
end=dict1[0][1]
for i in range(1,n):
    if dict1[i][0]>=end:
        end=dict1[i][1]
        cnt+=1

print(cnt)
