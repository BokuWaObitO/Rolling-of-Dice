from random import choice

class Random_walk:
    def __init__(self,area=50_000):
        self.area=area
        self.x_value=[0]
        self.y_value=[0]

    def walk(self):
        while len(self.x_value)<(self.area):  # no need of len here as area is in itself a integer
            x_direction=choice([-1,1])    # no need of self.x_direction ...try to run the program with self. to see the difference ...if yes ..then likely its cause def (self , direction ) the name is needed within the parameters of method 
            x_distance=choice([0,1,2,3,4])
            x_step=x_distance*x_direction
            
            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_distance*y_direction

            if x_distance==0 and y_distance==0:
                continue
            
            x=self.x_value[-1]+x_step   # here u need self.x_value....try to understand y 
            y=self.y_value[-1]+y_step   # mistake i did was not using list here ...x_value is a list , cant be added with other type ..hence i didnt used it as list ,so it wasnt able to add it with the list 
            self.x_value.append(x)      # try to understand why its [-1] with x_value as well as y 
            self.y_value.append(y)

# try to understand the reason behind the different result with self.x_value[0] and same with [-1]
# try to see line 27 in regards with line 22 n 23.. and also see what happens when u put [-2], why does it work only with -1


   