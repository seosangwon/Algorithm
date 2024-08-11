#분할 정복
#1.divide : len_==1이 될 때 까지 자른다
#2.
def recursion(start,len_):
    if len_==1:
        return
    for i in range(start+len_//3 ,start+ len_//3 * 2 ):
        value[i]=" " # 가운데 비워주기
    recursion(start,len_//3) # 분할정복 왼쪽
    recursion(start+len_//3*2 , len_//3) # 분할정복 오른쪽



while True:
    try:
        n=int(input())
        value=['-'] * (3**n) #원본
        recursion(0,3**n)
        print(''.join(value))

    except:
        exit()

