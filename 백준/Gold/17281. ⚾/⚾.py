from itertools import permutations
N=int(input())
cnt=0
inning=[]
for _ in range(N):
    inning.append(list(map(int,input().split())))


for taja in permutations(range(1,9),8):
    taja=list(taja[:3])+[0]+list(taja[3:])


    hitter=0
    result=0
    for i in range(N):
        out=0
        base=[0,0,0,0]

        while out<3:
            hit=inning[i][taja[hitter]] # i는 이닝수를 의미 , taja는 엔트리를 의미

            if hit==0:
                out+=1

            elif hit==1:
                result+=base[3]
                base=[0,1,base[1],base[2]]

            elif hit==2:
                result+=base[2]+base[3]
                base=[0,0,1,base[1]]

            elif hit==3:
                result+=base[1]+base[2]+base[3]
                base=[0,0,0,1]
            elif hit==4:
                result+=1+base[1]+base[2]+base[3]
                base=[0,0,0,0]

            hitter=(hitter+1)%9

    if result>cnt: # 최대값 저장
        cnt=result

print(cnt)
