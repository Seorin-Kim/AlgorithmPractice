h, w, n, m = map(int, input().split())

garo = w // (m + 1) + 1
if w % (m + 1) == 0:
    garo -= 1

sero = h // (n + 1) + 1
if h % (n + 1) == 0:
    sero -= 1

print(garo * sero)