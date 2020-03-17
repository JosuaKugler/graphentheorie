# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:40:28 2018

@author: DELL
"""

while True:
    try:
        n=int(input("n:"))
        if n<2:
            print("n muss größer sein als 2")
        else:
            break
    except:
        print("n muss ein integer sein")
    
p=364/365
x=p**n
x=1-x
print("Die Wahrscheinlichkeit, dass bei {} Personen 2 davon am gleichen Tag Geburtstag haben, beträgt {}".format(n,x))
