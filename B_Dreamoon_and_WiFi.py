from math import comb

s1 = input().strip()
s2 = input().strip()

target = s1.count('+') - s1.count('-')
current = s2.count('+') - s2.count('-')
q = s2.count('?')

diff = target - current

if (diff + q) % 2 != 0:
    print("0.0")
else:
    k = (diff + q) // 2
    if k < 0 or k > q:
        print("0.0")
    else:
        ways = comb(q, k)
        total = 2 ** q
        print(ways / total)