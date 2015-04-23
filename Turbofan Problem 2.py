import math
import matplotlib.pyplot as plt
import numpy as np
import xlwt
import sys

book = xlwt.Workbook()
sheet1 = book.add_sheet('Thermal Efficiency at B=10', cell_overwrite_ok=True)

# Conditions given in the problem
Pa = 26.5
Ta = 223.252
To4_max = 1500
gamma1 = 1.4
gamma2 = 1.35
R = 287
Cp1 = (gamma1/(gamma1-1))*R/1000
Cp2 = (gamma2/(gamma2-1))*R/1000
M=0.8
Fst=0.06
hc=43000
B=1

#Efficiencies
nd=0.94
nc=0.87
#rc=24
nb=0.98
rb=0.97
nt=0.85
ncn=0.97
nf=0.92
nfn=0.98
#rf=2.0

rclist = np.linspace(20.0, 28.0, num=30, endpoint=True)
rflist = np.linspace( 1.5,  2.2, num=30, endpoint=True)

#Flow Conditions
Toa = Ta*(1 + ((gamma1-1)/2)*M**2)
print 'Toa '
print Toa
Poa = Pa*(1 + ((gamma1-1)/2)*M**2)**(gamma1/(gamma1-1))
print 'Poa '
print Poa
u = M*math.sqrt(gamma1*R*Ta) 
print 'u '
print u

#Inlet/Diffuser
To2=Toa
To2s=nd*(To2-Ta)+Ta
print 'To2s '
print To2s
Po2=Pa*(To2s/Ta)**(gamma1/(gamma1-1))
print 'Po2 '
print Po2

i = 0 
for rc in rclist:
    j=0
    #Compressor
    To3s=To2*rc**((gamma1-1)/gamma1)
    Po3=rc*Po2
    To3 = ((To3s-To2)/nc)+To2
    wc_in = Cp1*(To3-To2)

    #Combustor
    To4=To4_max
    Fb=(((To4/To3)-1)/((nb*hc/(Cp2*To3))-(To4/To3)))
    if Fb >= Fst:
        Fb = Fst
        To4 = (Fb*nb*hc/(Cp2)+Toa)/(1+Fb)
    Po4=rb*Po3

    for rf in rflist:
        #Fan
        Po8=rf*Po2
        To8s=To2*(rf**((gamma1-1)/gamma1))
        To8 = ((To8s-To2)/nf)+To2
        wf_in = B*Cp1*(To8-To2)
            
        #Turbine
        wt_out=wc_in+wf_in
        To5=To4-(wt_out/(Cp2*(1+Fb)))
        To5s=To4-((To4-To5)/nt)
        Po5=Po4*(To5s/To4)**(gamma2/(gamma2-1))
            
        #Core Nozzle
        To6=To5
        To7=To6
        Po6=Po5
        P7=Pa
        T7as=(To6/((Po6/P7)**((gamma2-1)/gamma2)))
        T7=To6-ncn*(To6-T7as)
        M7=math.sqrt(((To7/T7)-1)*(2/(gamma2-1)))
        u7 = M7*math.sqrt(gamma2*R*T7)

        #Fan Nozzle
        To8=Toa
        To9=To8
        T9as=(To8/((Po8/Pa)**((gamma1-1)/gamma1)))
        T9=To8-nfn*(To8-T9as)
        M9=math.sqrt(((To9/T9)-1)*(2/(gamma1-1)))
        u9 = M9*math.sqrt(gamma1*R*T9)
                    
        I = B*(u9-u)+((1+Fb)*u7-u)
        TSFC = Fb/I
        Pav=((1+Fb)*(u7**2)/2 + B*(u9**2)/2 - (B+1)*(u**2)/2)
        Pin=Fb*hc*1000
        wp=I*u
        nth=Pav/Pin
        np=wp/Pin
        no=nth*np

        print '-----------------'
        print rc
        print rf
        print no
        sheet1.write(i+1,j+1,no)
        sheet1.write(i+1,0,rc)
        sheet1.write(0,j+1,rf)
        j = j+1
    i = i+1

book.save('Overall Efficiency Matrix.xls')
raw_input('Press any Key to Exit')
sys.exit(-1)
