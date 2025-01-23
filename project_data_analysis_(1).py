
import matplotlib.pyplot as plt
# remeber at line 2 we kept matplotlib only ...hence python didnt understood the .plot( method )and .show () mehtod ...only when used matplotlib.pyplot ...then the python understood the method .plot() N SUCH 


input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
print(plt.style.available)
plt.style.use('seaborn-v0_8-bright')
fig,ax=plt.subplots()  #try to know why such arangements is there within the equation and how the machine understands

ax.plot(input_values,squares,linewidth=3)# this the width of the graph reading line 
#setting up the chart title and label axis
ax.set_title("Squares Numbers", fontsize=24) # this changes the title size
   #mistake - i did ax.se.title than ax.set_title , although pyhton is not showing any error at start , but by runnning the code, it shows not recognising the .title with set method 
#same for line 12 , 13...the color of association chanegs with the changing of the (.) to (_)
# here the color association should be yellow than it was white when it returned as error


"""remember its ax.set_ylabel"""
ax.set_xlabel("Value",fontsize=14) # the description for the x axis 
ax.set_ylabel("Sqaure of the value ",fontsize=14)  
#set the size of tick label
ax.tick_params(axis="both",which="major",labelsize=14)# the size of the ticks as well as the value representing the ticks 
#the which=" major " chanegs the the value representation at the x axis from float to integer
# check what this with="major" is about in line 21
#plt.style.available....not showing the desired result

'''correcting the plot '''
#line5,9

#using built in style (line 8 ,9)
# know this u need to use that call within print statement to show you the available styles unlike int he book 

#ploting and styling individual points with scatter

ax.scatter(4,16,s=50)  # this highlights the point according to ur desire ...although y the name of method is scatter()
# check out line 33 for s argument within the statement which is the vlaue for the size of the dot 
# plotting series of points with scatter( )
x_values=[1,2,3,4,5]
y_values=[1,2,3,4,5]

ax.scatter(x_values,y_values,s=50)

#calculating data automatically 






plt.show()