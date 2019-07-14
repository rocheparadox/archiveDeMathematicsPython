#Author : Roche Christopher
#File created on 14 Jul 2019 5:45 PM

#This is a demo program to find the area between a straight line and x axis

no_of_samples=5

#function of x defined as y
get_y = lambda x : x
sampling_interval = 0.2 #x - axis
sampling_points=[round(sampling_interval*x,2) for x in range(1,no_of_samples+1)]
sampled_values=[]

for x in range(0, no_of_samples):

    sampled_value = get_y(sampling_points[x])
    #print(sampled_value)
    sampled_values.append(sampled_value)

sampled_values.insert(0,0)
sampling_points.insert(0,0)

#print(sampling_points, sampled_values)
area = 0
for i in range(1, no_of_samples + 1):

    # width = sampling interval, height = previous sampled_value
    rectangle_area = sampling_interval * sampled_values[i-1]
    # width = sampling interval
    # height of the triangle is the difference between the previous and present sampled values
    triangle_area = (abs(sampled_values[i] - sampled_values[i-1]) * sampling_interval) / 2
    area = round(area + rectangle_area + triangle_area, 2)

print(area)

