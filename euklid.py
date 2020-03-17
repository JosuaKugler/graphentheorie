# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:38:56 2018

@author: DELL
"""

def euklid(A,B):
    x=0
    while B>0 and x<100:
        x+=1
        if A<=B:
            B=B-A
        else:
            A=A-B
    return A
#print(euklid(1001,7000))

while True:
    print("Bin ich ein Algorithmus?")
    