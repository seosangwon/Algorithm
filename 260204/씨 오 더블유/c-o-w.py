import sys
input = sys.stdin.readline

N = int(input().strip())
s = input().strip()

c_count = 0
co_count = 0
cow_count = 0

for ch in s:
    if ch == 'C':
        c_count += 1
    elif ch == 'O':
        co_count += c_count
    elif ch == 'W':
        cow_count += co_count

print(cow_count)
