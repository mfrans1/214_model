###################################################################
#
#  :: Earth Temperature Model ::
#
# #################################################################

# import modules 
import numpy as np
import matplotlib.pyplot as plt
import math 

# 'single slab' atmosphere model, aka gray atmosphere
# define variables
dt = 60 # s
time = np.arange(0,3600,dt) # list of times, measured in seconds
insolation = 1367 # Wm^-2
earth_temperature = 0 # K 
earth_temperature_values = [] # empty list so we can add earth temperature values
heat_capacity = 850
albedo = 0.3

atmosphere_temperature = 0 # K
atmosphere_heat_capacity = 700
emissivity = 0.75

def black_body(temp):
    sigma = 5.67E-8 # stefan boltzmann constant
    return sigma*np.power(temp,4)

# calculate the earth temperature (and atmosphere temperature) values for entire list of times 
for interval in time:
    earth_temperature += \
    (insolation*(1-albedo) + 4*emissivity*(black_body(atmosphere_temperature)) - \
     4*black_body(earth_temperature))*dt/heat_capacity
    atmosphere_temperature += \
    emissivity*(black_body(earth_temperature)-2*black_body(atmosphere_temperature))*dt/atmosphere_heat_capacity
    earth_temperature_values.append(earth_temperature)

# plot the data
plt.figure(figsize=(6.5,4))
plt.title('Earth Temperature Model (Single-Slab Atmo.)')
plt.plot(time, earth_temperature_values, color='blue')
plt.ylim((50,300))
plt.xlabel('Time [s]'), plt.ylabel('Earth Temperature [K]')
plt.grid(True)
plt.show()

max_temp = max(earth_temperature_values)
max_temp_atmo = atmosphere_temperature
print('Earth maximum temperature', f'{max_temp:.3f}','K')
print('Atmosphere maximum temperature', f'{max_temp_atmo:.3f}','K')
