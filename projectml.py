#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

#P = π/2 * r² * v³ * ρ * η
# "P" is the power generated
# "r" id the radius of the turbine
# "v" is the speed or velocity of the wind
# "ρ" is the air density
# "η" is the Efficiency factor=40%


speed_w=ctrl.Antecedent(np.arange(0,26,0.02),'speed_w')
radius=ctrl.Antecedent(np.arange(19,90,0.5),'radius')
density=ctrl.Antecedent(np.arange(0.07,1.3,0.03),'density')
power=ctrl.Consequent(np.arange(0,95426,200),'power')

speed_w['poor']=fuzzy.trimf(speed_w.universe,[0,4,7])
speed_w['average']=fuzzy.trimf(speed_w.universe,[6,10,16])
speed_w['good']=fuzzy.trimf(speed_w.universe,[15,20,26])

radius['poor']=fuzzy.trimf(radius.universe,[19,28,40])
radius['average']=fuzzy.trimf(radius.universe,[30,45,60])
radius['good']=fuzzy.trimf(radius.universe,[55,70,90])

density['poor']=fuzzy.trimf(density.universe,[0.07,0.1,0.5])
density['average']=fuzzy.trimf(density.universe,[0.4,0.8,1.0])
density['good']=fuzzy.trimf(density.universe,[0.9,1.1,1.3])

power['dismal']=fuzzy.trimf(power.universe,[0,0,50])
power['poor']=fuzzy.trimf(power.universe,[40,200,400])
power['mediocre']=fuzzy.trimf(power.universe,[390,1800,4000])
power['average']=fuzzy.trimf(power.universe,[4000,8000,20000])
power['decent']=fuzzy.trimf(power.universe,[19000,25000,35000])
power['good']=fuzzy.trimf(power.universe,[34500,50000,65000])
power['excellent']=fuzzy.trimf(power.universe,[64000,70000,95000])

#density.view()
#speed_w.view()
#radius.view()
#power.view()

rule1=ctrl.Rule(speed_w['poor']&radius['poor']&density['poor'],power['dismal'])
rule2=ctrl.Rule(speed_w['poor']&radius['poor']&density['average'],power['dismal'])
rule3=ctrl.Rule(speed_w['poor']&radius['poor']&density['good'],power['dismal'])
rule4=ctrl.Rule(speed_w['poor']&radius['average']&density['poor'],power['mediocre'])
rule5=ctrl.Rule(speed_w['poor']&radius['average']&density['average'],power['average'])
rule6=ctrl.Rule(speed_w['poor']&radius['average']&density['good'],power['decent'])
rule7=ctrl.Rule(speed_w['poor']&radius['good']&density['poor'],power['mediocre'])
rule8=ctrl.Rule(speed_w['poor']&radius['good']&density['average'],power['average'])
rule9=ctrl.Rule(speed_w['poor']&radius['good']&density['good'],power['decent'])
rule10=ctrl.Rule(speed_w['average']&radius['poor']&density['poor'],power['mediocre'])
rule11=ctrl.Rule(speed_w['average']&radius['poor']&density['average'],power['average'])
rule12=ctrl.Rule(speed_w['average']&radius['poor']&density['good'],power['average'])
rule13=ctrl.Rule(speed_w['average']&radius['average']&density['poor'],power['average'])
rule14=ctrl.Rule(speed_w['average']&radius['average']&density['average'],power['decent'])
rule15=ctrl.Rule(speed_w['average']&radius['average']&density['good'],power['good'])
rule16=ctrl.Rule(speed_w['average']&radius['good']&density['poor'],power['decent'])
rule17=ctrl.Rule(speed_w['average']&radius['good']&density['average'],power['decent'])
rule18=ctrl.Rule(speed_w['average']&radius['good']&density['good'],power['good'])
rule19=ctrl.Rule(speed_w['good']&radius['poor']&density['poor'],power['decent'])
rule20=ctrl.Rule(speed_w['good']&radius['poor']&density['average'],power['good'])
rule21=ctrl.Rule(speed_w['good']&radius['poor']&density['good'],power['good'])
rule22=ctrl.Rule(speed_w['good']&radius['average']&density['poor'],power['good'])
rule23=ctrl.Rule(speed_w['good']&radius['average']&density['average'],power['good'])
rule24=ctrl.Rule(speed_w['good']&radius['average']&density['good'],power['good'])
rule25=ctrl.Rule(speed_w['good']&radius['good']&density['poor'],power['good'])
rule26=ctrl.Rule(speed_w['good']&radius['good']&density['average'],power['excellent'])
rule27=ctrl.Rule(speed_w['good']&radius['good']&density['good'],power['excellent'])

tipping=ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13
                           ,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])
Tip=ctrl.ControlSystemSimulation(tipping)
print("*********************Wind Energy System using Fuzzy Interface*********************")
print("Wind Speed is in range 1-25m/s")
print("Length of wing is in range 19-90meters")
print("Air density is in the range 0.08-1.24 kg/m^3")
a=float(input("Enter the speed of wind m/s:"))
b=float(input("Enter the length of wing m:"))
c=float(input("Enter the density of air kg/m^3:"))
Tip.input['speed_w']=a
Tip.input['radius']=b
Tip.input['density']=c
Tip.compute()
print("The Power Generated in Kilowatts:",Tip.output['power'])


# In[ ]:




