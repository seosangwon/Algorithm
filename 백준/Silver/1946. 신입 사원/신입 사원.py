import sys
case=int(input())
for i in range(case):
    count=1
    people=[]
    tester=int(input())
    for i in range(tester):
        paper,interview=map(int,sys.stdin.readline().split())
        people.append([paper,interview])
    people.sort()
    max=people[0][1]
    for i in range(1,tester):
        if max>people[i][1]:
            count+=1
            max=people[i][1]
    print(count)
