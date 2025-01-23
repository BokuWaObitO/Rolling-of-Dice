import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]


plt.style.use('grayscale')

fig, ax = plt.subplots()  

# still not understanding the statement is like this 
#mistake that i made was i used plt.subplot than subplots...be vary about that

ax.scatter(x_values,y_values,s=10)

ax.set_title("Square numbers ",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of the number",fontsize=14)
ax.tick_params(axis="both",which="major",labelsize=14)  
# see the diff here that ,here we r using labelsize than fontsize
ax.axis([0,1100,0,100_000])  #just cause of line 22 ...the diff of pattern of graph is huge

# things to know - here i used 6 zeros after 1 ...so the graph showed its representation
#with the y axis tick mark as 1e6(the graph shows)....but if i remove one zero ,then the graph shows the representation as normal no 

 
 
 # remember we are using list within the method call 

#defining custom colors by three methods

#ax.scatter(x_values,y_values,c="red",s=10)
ax.scatter(800,8000,c="purple",s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Oranges,s=10)
#try to understand line 34 much better ..whats plt.cm.Oranges

plt.savefig('squares_no.png',bbox_inches='tight')

plt.show()

#saving your plots automatically
#why does the line 41 shows error when i use any name of variable for whitespace....bbboxinches returns error but , bbox_innches doesnt ?..is it case sensitive 
# the fig thats saved on the directory is blank ....?
#ans is that cause after the save i called the plot show, hence the image is overidden ..something like  that ...so 
'''Always call plt.savefig() before plt.show()'''
# now it works














