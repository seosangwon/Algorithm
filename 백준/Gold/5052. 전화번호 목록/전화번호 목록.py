t=int(input())

def solutions(phone_book):
    hash_map={}
    for i in phone_book:
        hash_map[i]=1
    for phone_number in phone_book:
        temp=''
        for i in phone_number:
            temp+=i
            if temp in hash_map and temp!=phone_number:
                return "NO"
    return "YES"


for _ in range(t):
    n=int(input())
    book=[]
    for _ in range(n):
        book.append(input())
    print(solutions(book))
