#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue # fanhui xunhuan kaishi zhixingchu
    elif n == 0:
        break
    print("Square is ",n ** 2)
print("Goodbye")
