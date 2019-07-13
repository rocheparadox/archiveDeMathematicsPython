#Author : Roche Christopher
#File created on 13 Jul 2019 5:36 PM

#reference - https://www.nxp.com/docs/en/application-note/AN3397.pdf

import math

area_to_be_found = math.pi
#number of samples to be taken
no_of_samples = 100

#sampling interval - interval at which signals are sampled
sampling_interval = round(area_to_be_found/no_of_samples, 2)
sampled_values=[]

for i in range(0, no_of_samples + 1):
    sampled_value = round(math.sin(i * (area_to_be_found/no_of_samples)), 3)
    #print(sampled_value)
    sampled_values.append(sampled_value)

#print(sampling_interval, sampled_values)

area = 0

for i in range(1, no_of_samples + 1):

    # width = sampling interval, height = previous sampled_value
    rectangle_area = sampling_interval * sampled_values[i-1]
    # width = sampling interval
    # height of the triangle is the difference between the previous and present sampled values
    triangle_area = (abs(sampled_values[i] - sampled_values[i-1]) * sampling_interval) / 2
    area = round(area + rectangle_area + triangle_area, 2)

print(area)