#making a histogram 
from plotly.graph_objs import Bar, Layout
from plotly import offline




from rolling_dice import Die

#rolling the die

die_1=Die()
die_2=Die(10)



results=[]
for roll_num in range (50_000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#analyze the results 
frequencies=[]
max_sides=die_2.num_sides+die_1.num_sides
for value in range(2,max_sides+1):  #when u run this ,it shows count of 1-5 not 6 cause range ends one value before the given second value 
    frequency=results.count(value)
    frequencies.append(frequency)

#print(frequencies)


#visualize the results
x_values=list(range(2,max_sides+1))
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={"title":"Result","dtick":1}
y_axis_config={"title":"Frequency of Result"}
my_layout=Layout(title="Results of rolling 2 dice with  6 n 10  side for 50000 times",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_10.html')
# know the line 35 returned a error cause the key was 'layout' not 'Layout'...reason of failure is cause the 'Layout' is not coded in the offline.py

#rolling dice of diffrent sizes
#changes in line13,18