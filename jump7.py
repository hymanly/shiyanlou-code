a = range(1,101)
for b in a:
    if b%7 == 0:
        continue
    elif b%10 == 7:
        continue
    elif b // 10 == 7:
        continue

    print(b)
