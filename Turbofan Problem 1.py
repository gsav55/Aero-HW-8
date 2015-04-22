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
Cp1 = (gamma1/(gamma1-1))*R/1000
Cp2 = (gamma2/(gamma2-1))*R/1000
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
Blist = []

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
To4=To4_max
Fb=(((To4/To3)-1)/((nb*hc/(Cp2*To3))-(To4/To3)))
if Fb >= Fst:
    Fb = Fst
    To4 = (Fb*nb*hc/(Cp2)+Toa)/(1+Fb)
Po4=rc*Po2
print 'Fb '
print Fb

for B in np.arange(6,10.2,0.1):

    #Fan
    Po8=rf*Po2
    To8s=To2*(rf**((gamma1-1)/gamma1))
    To8 = ((To8s-To2)/nf)+To2
    wf_in = B*Cp1*(To8-To2)
	
    #Turbine
    wt_out=wc_in+wf_in
    To5=To4-(wt_out/(Cp2*(1+Fb)))
    To5s=To4-((To4-To5)/nt)
    Po5=Po4*(To5s/To4)**(gamma2/gamma2-1)
        
    #Core Nozzle
    To6=To5
    To7=To6
    Po6=Po5
    P7=Pa
    T7as=(To6/((Po6/P7)**(gamma2-1/gamma2)))
    T7=To6-ncn*(To6-T7as)
    M7=math.sqrt(((To7/T7)-1)*(2/(gamma2-1)))
    u7 = M7*math.sqrt(gamma2*R*T7)

    #Fan Nozzle
    To8=Toa
    To9=To8
    T9as=(To8/((Po8/Pa)**(gamma1-1/gamma1)))
    T9=To8-nfn*(To8-T9as)
    M9=math.sqrt(((To9/T9)-1)*(2/(gamma1-1)))
    u9 = M9*math.sqrt(gamma1*R*T9)

    if B == B:
        #Fan Data
        #Turbine Data
        print '--------B--------'
        print B
        print 'To5 '
        print To5
        print 'To5s '
        print To5s
        print 'Po5 '
        print Po5

        #Core Nozzle Data
        print 'T7as '
        print T7as
        print 'T7 '
        print T7
        print 'M7 '
        print M7
        print 'u7 '
        print u7

        #Fan Nozzle Data
        print 'T9as '
        print T9as
        print 'T9 '
        print T9
        print 'M9 '
        print M9
        print 'u9 '
        print u9
		
    I = B*(u9-u)+((1+Fb)*u7-u)
    TSFC = Fb/I
    Pav=((1+Fb)*(u7**2)/2 + B*(u9**2)/2 - (B+1)*(u**2)/2)
    Pin=Fb*hc*1000
    wp=I*u
    nth=Pav/Pin
    np=wp/Pin
    no=nth*np
    if B == B:
        print 'nth '
        print nth
        print 'Pav '
        print Pav
	
    Ilist.append([I])
    TSFClist.append([TSFC])
    nthlist.append([nth])
    nplist.append([np])
    nolist.append([no])
    Blist.append([B])
	
    
# Now to plot everything!
plt.figure(1)
plt.plot(Blist, Ilist)
plt.xlabel('Bypass Ratio, B')
plt.ylabel('Specific Thrust, I')
plt.title('I vs B')

plt.figure(2)
plt.plot(Blist, TSFClist)
plt.xlabel('Bypass Ratio, B')
plt.ylabel('TSFC')
plt.title('TSFC vs B')

plt.figure(3)
plt.plot(Blist, nthlist)
plt.xlabel('Bypass Ratio, B')
plt.ylabel('Thermal Efficiency, nth')
plt.title('Thermal Efficiency vs B')

plt.figure(4)
plt.plot(Blist, nplist)
plt.xlabel('Bypass Ratio, B')
plt.ylabel('Propulsive Efficiency, np')
plt.title('Propulsive Efficiency vs B')

plt.figure(5)
plt.plot(Blist, nolist)
plt.xlabel('Bypass Ratio, B')
plt.ylabel('Overall Efficiency, no')
plt.title('Overall Efficiency vs B')

plt.show()
