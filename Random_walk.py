import matplotlib.pyplot as plt 

from R_W_cl import Random_walk

i=0

loop_run=int(input("How many random projections do you want.....?"))


for i in range(0,loop_run):
    
    rw=Random_walk()
    rw.walk()
    plt.style.use('ggplot')
    fig,ax=plt.subplots(figsize=(6,6),dpi=128)
    #ax.scatter(rw.x_value,rw.y_value,c="Purple",s=15)
    plt.savefig("Random walk.png",bbox_inches='tight')
    point_num=range(rw.area)
    ax.scatter(rw.x_value,rw.y_value,c=point_num,cmap=plt.cm.Oranges,edgecolors='none',s=1)

    #emphasize the first and last points 
    ax.scatter(rw.x_value[-1],rw.y_value[-1],c="Yellow",s=55,edgecolors='none')
    ax.scatter(0,0,c="Purple",s=55,edgecolors='none')

    #to remove the axis 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    

    plt.show()





#altering the size to fill the screen at line 15 ...and dpi ?? know what it is 





    
    

    
    



