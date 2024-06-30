def solution(n, tops):
    answer = 0
    MOD=10007
    dp1=[0] * (n+1)
    dp2=[0] * (n+1)
    dp1[0]=0
    dp2[0]=1
    
    for k in range(1,n+1):
        if tops[k-1]: # top이 있으면 
            dp1[k]=(dp1[k-1]+dp2[k-1]) % MOD
            dp2[k]=(2*dp1[k-1] + 3*dp2[k-1]) % MOD
            
        else:
            dp1[k]=(dp1[k-1] + dp2[k-1])%MOD
            dp2[k]=(dp1[k-1] + 2 * dp2[k-1]) % MOD
        
    return (dp1[n]+dp2[n]) % MOD
            
            
    
    
                

