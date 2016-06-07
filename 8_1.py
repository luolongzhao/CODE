'''
Created on 6 Jun 2016

@author: Luo Long Zhao Mars
'''
import math
from test.test_enum import Answer

#Calculation of the convection-radiation heat transfer equilibrium of a single pipe in a quasi-boundless space
Re=[]#Reynold Number
Nu=[]#Nusselt Number
Pr=[]
C=[]#流出系数
n=[]
h=[]
sigma= ? #Stephen-Bolzmann Constant
Qradiation=[]
Qconvection=[]
Qepsilon=0.01
Nu = 
function = 1

Nu =
function = 2

def heat_transfer_iteration(v,mu,rho,Cp,lambda,d,Tcurrent,Twall,P,length):
#velocity of current,ynamic viscosity,density of fluid,specific heat(pressure static),pipe diameter,wall temperature,power exerted to the heat pipe, pipe length
    Re=rho*v*d/mu
    print('Reynolds Number=',Re)
    Pr=Cp*mu/lambda
    print('Prandtl Number=',Pr)
    Qpipe=P/length
    if Re>0.4
    C=0.989 , n=0.330
    else if 
    Nu=C*(Re**n)*(Pr**0.333)
    print('Nusselt Number',Nu)
    h=Nu*lambda/d
    

    Qconvection=h*3.14*(d**2)*(Tpipe=Tcurrent) #Newton's Cooling Theory
    Qradiation=sigma*(Tpipe**4-Twall**4)
    Tpipe = Twall   #It is unlikely the pipe temperature is lower than that of the radiated wall
     for i in range(1,1000) #Define a maximum numeration of steps of 1000
         print('Estimating the pipe temperature, the pipe temperature of this step is',Tpipe)
         Tpipe += 1
         Qconvection=h*3.14*(d**2)*(Tpipe=Tcurrent) #Newton's Cooling Theory
         Qradiation=sigma*(Tpipe**4-Twall**4)
         if (Qconvection+Qradiation> Qinput)
             LowerThreshold= Tpipe - 1
             HigherThreshold= Tpipe
             print('Estimation finished, estimated pipe temperature is between',LowerThreshold,'and',HigherThreshold,'Celcius')
             print('Qconvection =',Qconvection,'Qradiation=',Qradiation)
             print('Times of test',i)

         answer=(LowerThreshold+HigherThreshold)/2
     while abs((Qconvection+Qradiation-Qinput)/Qinput)>Qepsilon
         print 'Pipe temperature under current iteration is', Tpipe
         numberIteration += 1
         if (Qconvection+Qradiation>Q)
             HigherThreshold= Answer
         else
             LowerThreshold= Answer
         answer=(LowerThreshold+HigherThreshold)/2
         
         Qconvection=h*3.14*(d**2)*(Tpipe-Tcurrent) #Newton's Cooling Theory
         Qradiation=sigma*(Tpipe**4-Twall**4)
     print 'Answer of wall temperature T=', answer

heat_transfer_iteration(150.37e-3,95.911e-3,0.63783,1,118600,855.69,126.93e-6)