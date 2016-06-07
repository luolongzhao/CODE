'''
Created on 5 Jun 2016

@author: Luo Long Zhao Mars
'''

# FIXME: TEST TASK Tag
def Applytoeach (L,f):
    for i in range(len(L)):
    L(i)=f(L(i))
L=[]
Applytoeach(L, abs)
Applytoeach(L, int)
Applytoeach(L, fact)
Applytoeach(L, deviaiton)