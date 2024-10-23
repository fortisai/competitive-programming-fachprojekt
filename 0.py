n = int(input())
h, b = list(map(int, input().split())), list(map(int, input().split()))
res = 0
for i in range(n):
    if h[i] + res > b[i]:
        print(res)
        break
    elif h[i] + res == b[i]:
        continue
    else:
        if res > 0:
            print(res + 1)
            break
        res = b[i] - h[i]
else:
    print(res + 1)
