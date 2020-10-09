#!/usr/bin/env python3
days = int(input("Enter days:"))
mouths = days // 30
days = days % 30
print("Months = {} Days = {}".format(mouths,days))

#days = int(input("Enter days:"))
#print("Mouths = {} Days = {}".format(*divmod(day,30)))
