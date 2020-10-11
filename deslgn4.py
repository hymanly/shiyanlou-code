#!/usr/bin/env python3
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x = "*" * (n * 2 - 1)
    y = " " * (row - n)
    print(y + x)
    n -= 1
