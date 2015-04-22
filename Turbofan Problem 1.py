#Turbojet Engine Problem 1

import math
import matplotlib.pyplot as plt
import numpy as np

# Conditions given in the problem
Pa = 26.5
Ta = 223.252
To4_max = 1500
gamma1 = 1.4
gamma2 = 1.35
R = 287
Cp1 = 
Cp2 = 
M=0.8
Fst=0.06
hc=43000

#Efficiencies
nd=0.94
nc=0.87
rc=24
nb=0.98
rb=0.97
nt=0.85
ncn=0.97
nf=0.92
nfn=0.98
rf=2.0
 

Mlist = []
Ilist = []
TSFClist = []
nthlist = []
nplist = []
nolist = []
rclist = []
A_ratiolist = []

#Flow Conditions
Toa = Ta*(1 + ((gamma1-1)/2)*M**2)
print Toa
Poa = Pa*(1 + ((gamma1-1)/2)*M**2)**(gamma1/(gamma1-1))
print Poa
u_in = M*math.sqrt(gamma1*R*Ta) 
print u_in

#Inlet/Diffuser
To2=Toa
To2s=nd*(To2-Ta)+Ta
print 'To2s '
print 'To2s '
Po2=Pa*(To2s/Ta)**(gamma1/(gamma1-1))
print 'Po2 '
print Po2

#Compressor
To3s=To2*rc**((gamma1-1)/gamma1)
print 'To3s '
print To3s
Po3=rc*Po2
print 'Po3 '
print Po3
To3 = ((To3s-To2)/nc)+To2
print 'To3 '
print To3
wc_in = Cp1*(To3-To2)
print 'wc_in '
print wc_in
	
#Combustor
Fb=(((To4/To3)-1)/((nb*hc/(Cp2*To3))-(To4/To3)))
if Fb >= Fst:
    Fb = Fst
    To4 = (Fb*nb*hc/(Cp2)+Toa)/(1+Fb)
Po4=rc*Po2
print 'Fb '
print Fb

#NEED TO CREATE BYPASS RATIO LOOP FROM HERE DOWN!!
#Fan
Po8=rf*Po2
To8s=To2*(rf**((gamma1-1)/gamma1))
To8 = ((To8s-To2)/nf)+To2
wf_in = B*Cp1*(To8-To2)
	
#Turbine
wt_out=wc_in+wf_in
To5=To4-(wt_out/(Cp2*(1+Fb)))
print 'To5 '
print To5
To5s=To4-((To4-To5)/nt)
print 'To5s '
print To5s
Po5=Po4*(To5s/To4)**(gamma2/gamma2-1)
print 'Po5 '
print Po5
    
#Core Nozzle
To6=To5
To7=To6
Po6=Po5
P7=Pa
T7as=(To6/((Po6/P7)**(gamma2-1/gamma2)))
print 'T7as '
print T7as
T7=To6-ncn*(To6-T7as)
print 'T7 '
print T7
M7=math.sqrt(((To7/T7)-1)*(2/(gamma2-1)))
print 'M7 '
print M7
u7 = M7*math.sqrt(gamma2*R*T7)
print 'u7 '
print u7

#Fan Nozzle
To8=Toa
To9=To8
T9as=(To8/((Po8/Pa)**(gamma1-1/gamma1)))
print 'T9as '
print T9as
T9=To8-nfn*(To8-T9as)
print 'T9 '
print T9
M9=math.sqrt(((To9/T9)-1)*(2/(gamma1-1)))
print 'M9 '
print M9
u9 = M9*math.sqrt(gamma1*R*T9)
print 'u9 '
print u9
		
I = (1+Fb)*u7-u_in
TSFC = Fb/I
nth=(((1+Fb)*u7**2-u_in**2)/(2*Fb*hc*1000))
np=(2*u_in/(u7+u_in))
no=nth*np
A_ratio = (1/M7)*((2/2.3)*(1+(0.3/2)*M7**2))**(2.3/0.6)
	
Ilist.append([I])
TSFClist.append([TSFC])
A_ratiolist.append([A_ratio])
nthlist.append([nth])
nplist.append([np])
nolist.append([no])
rclist.append([rc])
	
    
# Now to plot everything!
plt.figure(1)
plt.plot(rclist, Ilist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Specific Thrust, I')
plt.title('I vs r_c')

plt.figure(2)
plt.plot(rclist, TSFClist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('TSFC')
plt.title('TSFC vs r_c')

plt.figure(3)
plt.plot(rclist, nthlist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Thermal Efficiency, nth')
plt.title('Thermal Efficiency vs r_c')

plt.figure(4)
plt.plot(rclist, nplist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Propulsive Efficiency, np')
plt.title('Propulsive Efficiency vs r_c')

plt.figure(5)
plt.plot(rclist, nolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Overall Efficiency, no')
plt.title('Overall Efficiency vs r_c')

plt.figure(6)
plt.plot(rclist, A_ratiolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Area Ratio, A/A*')
plt.title('Area Ratio vs r_c')

plt.show()
