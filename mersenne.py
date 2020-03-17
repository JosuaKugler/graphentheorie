# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:57:22 2018

@author: DELL
"""


while True:
    try:
        n=int(input("n:"))
        break
    except:
        print("n muss ein integer sein")
        
import matplotlib.pyplot as plt
xlist=range(n)
mlist=[]
for i in xlist:
    mlist.append(2**(2**i)+1)
try:
    plt.plot(xlist,mlist)
    plt.show()
except:
    print("{} ist leider zu groß, python kann die entsprechende mersenne-primzahl {} nicht plotten.".format(n,mlist[n-1]))
