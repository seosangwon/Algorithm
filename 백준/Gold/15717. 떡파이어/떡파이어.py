n=int(input())-1
a=2
c=int(1e9) + 7

def power(a,n,c):
    if n<2:
        return (a**n) % c
    else:
        d=n//2
        return((pow(a,d,c)) ** 2 )% c if n%2==0 else (a*(pow(a,d,c))**2)%c

if n!= -1:
    print(power(a,n,c))

else:
    print(1)