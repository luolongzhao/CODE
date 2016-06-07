'''
Created on 6 Jun 2016

@author: Luo Long Zhao Mars
'''
import math
import numpy as NP

import xlrd    

def average(excel_list):  #���Լ������ݵ�ƽ��ֵ
    sum=0
    j=0                    #����j�Լ���һ���ж���������
    for i in excel_list:
        sum+=i
        j+=1
    return (float(sum)/j)
   
def variance(excel_list):
    mean=average(excel_list)
    tot=0
    k=0                    #����k�Լ���һ���ж���������
    for i in excel_list:
        tot+=(i-mean)**2
        k+=1
    return (float(tot)/k)**0.5

def r(x,y):        #���Լ���Ƥ��ѷ���ϵ��r
    if len(x)!=len(y):
        print ('�޷�����')
    tot1=0
    tot2=0
    tot3=0   
    for i in range(len(x)):
        sum1=x[i]-average(x)
        sum2=y[i]-average(y)
        tot1+=(sum1*sum2)
        sum3=(x[i]-average(x))**2
        sum4=(y[i]-average(y))**2
        tot2+=sum3
        tot3+=sum4
    return tot1/((tot2*tot3)**0.5)            
        
excel = xlrd.open_workbook('test.xlsx')  
sheet = excel.sheets()[0]     #��ȡ��һ��sheet    
ncols = sheet.ncols
l=[average(sheet.col_values(x)) for x in range(0,8)] #��������б�ķ�ʽ��ñ��и��е����ݲ������еľ�ֵ���
print ('��һ���������ݵ�ƽ��ֵ�ֱ�Ϊ��',l)
m=[variance(sheet.col_values(x)) for x in range(0,8)]
print ('��һ���������ݵķ���ֱ�Ϊ��',m) 
n=[r(sheet.col_values(2*x),sheet.col_values(2*x+1)) for x in range(0,4)]
print('���ϵ����r1��r2��r3��r4�ֱ�Ϊ',n)

import matplotlib.pyplot as t1
import numpy as np
t1.figure(1) #����ͼ1
t1.title('figure')
ax1 = t1.subplot(221)
ax2 = t1.subplot(222)
ax3 = t1.subplot(223)
ax4 = t1.subplot(224)
t1.sca(ax1)
t1.xlabel('x')     #����x��
t1.ylabel('y')     #����y��
t1.plot(sheet.col_values(0), sheet.col_values(1),'bo')   #��ɢ��ͼ 1
x1 = np.array(sheet.col_values(0))          #pylab.array�������Խ�������ת�������б�ת��Ϊ��������
y1 = np.array(sheet.col_values(1))
m1,n1 = np.polyfit(x1, y1, 1)
predict_y1 = m1*np.array(x1) + n1
t1.plot(x1, predict_y1)                     #�������ֱ��

t1.sca(ax2)
t1.xlabel('x')     #����x��
t1.ylabel('y')     #����y��
t1.plot(sheet.col_values(2), sheet.col_values(3),'bo')   #��ɢ��ͼ 2
x2 = np.array(sheet.col_values(2))          #pylab.array�������Խ�������ת�������б�ת��Ϊ��������
y2 = np.array(sheet.col_values(3))
m2,n2 = np.polyfit(x2, y2, 1)
predict_y2 = m2*np.array(x2) + n2
t1.plot(x2, predict_y2)                     #�������ֱ��

t1.sca(ax3)
t1.xlabel('x')     #����x��
t1.ylabel('y')     #����y��
t1.plot(sheet.col_values(4), sheet.col_values(5),'bo')   #��ɢ��ͼ 3
x3 = np.array(sheet.col_values(4))          #pylab.array�������Խ�������ת�������б�ת��Ϊ��������
y3 = np.array(sheet.col_values(5))
m3,n3 = np.polyfit(x3, y3, 1)
predict_y3 = m3*np.array(x3) + n3
t1.plot(x3, predict_y3)                     #�������ֱ��

t1.sca(ax4)
t1.xlabel('x')     #����x��
t1.ylabel('y')     #����y��
t1.plot(sheet.col_values(6), sheet.col_values(7),'bo')   #��ɢ��ͼ 4
x4 = np.array(sheet.col_values(6))          #pylab.array�������Խ�������ת�������б�ת��Ϊ��������
y4 = np.array(sheet.col_values(7))
m4,n4 = np.polyfit(x4, y4, 1)
predict_y4 = m4*np.array(x4) + n4
t1.plot(x4, predict_y4)                     #�������ֱ��

t1.show()            #����ͼ��





for i in range(len(xygroups)):
        xsta,ysta,r=satData(xygroups[i]['x'], xygroups[i]['y'])
        a,b,predictedY=fitData(xygroups[i]['x'], xygroups[i]['y'])

        fig.add_subplot(figrow, figcol,i+1)     #��ͼ
        
        plotData(xygroups[i]['x'],xygroups[i]['y'],
                 a,b,predictedY,i)


        table.add_row(["file" "%.0f" % i,
                   "%.3f" % xsta['avg'],
                   "%.3f" % xsta['stdev'],"%.3f" %xsta['pstdev'],
                   "%.3f" % xsta['var'],"%.3f" % xsta['pvar'],
                   "%.3f" % ysta['avg'],
                   "%.3f" % ysta['stdev'],"%.3f" % ysta['pstdev'],
                   "%.3f" % ysta['var'],"%.3f" % ysta['pvar'],
                   "%.3f" % r])


print(table)

plt.show()  