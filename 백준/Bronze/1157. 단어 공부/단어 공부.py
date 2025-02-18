word = list(input().upper())
letter = {}
for i in word:
    if i in list(letter.keys()):
        letter[i] += 1
    else:
        letter[i] = 1

key = list(letter.keys())
num = list(letter.values())
max_num = max(num)
if num.count(max_num) > 1:
    print("?")
else:
    print(key[num.index(max_num)])
