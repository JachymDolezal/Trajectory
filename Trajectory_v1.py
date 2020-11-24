import math
import matplotlib.pyplot as plt
import numpy as np
import box

#nas_box = box.Box(20,50,200,100)
#nas_box1 =  box.Box(20,50,200,100)
#nas_box2 = box.Box(20,50,200,100)

#seznam_box = (nas_box1,nas_box2,nas_box)

#for box in seznam_box:
 #   if box.height > 200:
 #       nas_box = None


class Ballsim:

    def __init__(self):

        self.angle = 40 # in degrees
        self.velocity = 20 # no unit

        self.Vx = 0 # horizontal vector
        self.Vy = 0 # vertical vector

        self.radian = 0

        self.list_x = [] #list where y coordinates are being saved
        self.list_y = [] #list where x coordinates are being saved

        self.edge = [20,21,50,20] #dimentions of a box

        self.a = 1/2*9.81 #gravitaitonal constant
        self.t = 0 #variable that changes representing time
        self.h = 0 #inital height
        self.x = 0 #represents x coordinate
        self.y = 0 #represents x coordinate
        self.time_step = 0.01 #freqeuency of change of t variable
        self.d = 0 # intial x axis
        self.Vy_temp = []

 # calculates vectors from velocity and angle
    def Vectors(self):
        self.Vx = self.velocity*math.cos(self.radian)
        self.Vy = self.velocity*math.sin(self.radian)
        #print("Vx = ",self.Vx)
        #print("Vy = ",self.Vy,"ddddddddd")

# converts degrees to radians
    def rad(self):
        pi = math.pi
        self.radian = (self.angle*pi/180)
        #print("radian = ",self.radian)

# calculates x coordinate for particular t
    def launch_x(self):
        self.x = self.Vx*self.t + self.d
        #print("x = ",self.x)
        #print("d =",self.d)

# calculates y coordinate for particular t
    def launch_y(self):
        self.y = self.h+(self.Vy*self.t)-(self.a*self.t ** 2 )
        #print("y = ",self.y)

# main function that is running the program
    def trajectory(self):
        self.rad()
        self.Vectors()
        ground_hit = False
        box_hit = False
        stop = False
# program stops when when the bounce is too small (Vy > 0.01)
        while self.Vy > 0.05 and stop == False:
            while ground_hit == False:

               # print(self.Vy)
                self.launch_x()
                self.launch_y()

            #    if self.y < 0 or ((self.x > 200 and self.x < 300) and self.y < 5):
            #        self.d = self.x
            #        self.y = 0
            #        self.t = 0
            #        print('hi')
            #bounce of the ground
                if self.y < 0:
                    self.d = self.x
                    self.y = 0
                    self.t = 0
                    if box_hit == True:
                        self.Vy = self.Vy_temp[0]
                    self.Vy = self.Vy*0.8
                    print("ground")
                    box_hit = False
                    break
            #bouce of the top of the box
                elif (self.x > self.edge[1] and self.x < self.edge[2]) and self.y < self.edge[3]:
                    box_hit = True
                    self.Vy_temp.append(self.Vy)
                    self.Vy = self.y/self.t
                    self.d = self.x
                    self.t = 0
                    self.h = self.edge[3]+0.01
                    self.y = 0
                    print("top")
                    break
                elif (self.y<self.edge[3] and self.x > self.edge[0] and self.x < self.edge[1]):

                    stop = True
                    ground_hit = True
                    print("side")
                    break
                self.list_x.append(self.x)
                self.list_y.append(self.y)
                self.t = self.t + self.time_step
        self.graph()

# not implemented yet

    def ground_bounce(self):
        pass
# not implemented yet
    def box_bounce(self):
        pass

# graphs the lists of coordinates
    def graph(self):

        plt.plot(self.list_x,self.list_y)
        #plt.axis('equal')
        plt.ylim(0.,80.0)
        plt.xlim(0.,80.0)
        plt.figure(figsize=(1,10))
        plt.show()

# calls the class
p = Ballsim()
p.trajectory()