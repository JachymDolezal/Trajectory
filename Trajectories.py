import math
import matplotlib.pyplot as plt
import numpy as np

class Ballsim:

    def __init__(self):
        self.angle = 30 # in degrees
        self.velocity = 40 # no unit
        self.Vx = 0 # horizontal vector
        self.Vy = 0 # vertical vector
        self.radian = 0
        self.list_x = []
        self.list_y = []
        self.edge = [200,300,5]
        self.a = 1/2*9.81 #constant
        self.t = 0 #variable that changes
        self.h = 0 #inital height
        self.x = 0
        self.y = 0
        self.time_step = 0.01
        self.d = 10 # intial x axis
        self.p = 1
        self.gradient = 0


    def Vectors(self):
        self.Vx = self.velocity*math.cos(self.radian)
        self.Vy = self.velocity*math.sin(self.radian)
        #print("Vx = ",self.Vx)
        #print("Vy = ",self.Vy)

    def rad(self):
        pi = math.pi
        self.radian = (self.angle*pi/180)
        #print("radian = ",self.radian)

    def grad(self):
        self.gradient = (self.list_y[-1]-self.list_y[-2])/(self.list_x[-1]-self.list_x[-2])
        #print(self.gradient)

    def launch_x(self):
        self.x = self.Vx*self.t + self.d
        print("x = ",self.x)
        #print("d =",self.d)

    def launch_y(self):
        self.y = self.h+self.Vy*self.t-self.a*self.t*self.t
        print("y = ",self.y)

    def trajectory(self):
        self.rad()
        self.Vectors()
        ground_hit = False
        box_hit = False

        while self.Vy > 0.01:
        #for x in range(1,30):
            while ground_hit == False or box_hit == False:

                print(self.Vy)
                self.launch_x()
                self.launch_y()

            #    if self.y < 0 or ((self.x > 200 and self.x < 300) and self.y < 5):
            #        self.d = self.x
            #        self.y = 0
            #        self.t = 0
            #        print('hi')
                if self.y < 0:
                    self.d = self.x
                    self.y = 0
                    self.t = 0
                    self.Vy = self.Vy*0.8
                    print('//////////////////////////////////')
                    break
                    """
                if (self.x > self.edge[0] and self.x < self.edge[1]) and self.y < self.edge[2]:
                    self.d = self.x
                    self.t = 0
                    self.h = 5.1
                    print('hey ')
                    self.Vy = (self.list_y[-1]-self.list_y[-2])*100
                    print(self.Vy)
                    #self.Vy = self.Vy*0.3
                    #print(self.Vy)
                    break
                    """
                self.list_x.append(self.x)
                self.list_y.append(self.y)
                self.t = self.t + self.time_step
        self.graph()

    def ground_bounce(self):
        pass

    def box_bounce(self):
        pass


    def graph(self):
        plt.plot(self.list_x,self.list_y)
        plt.show()

p = Ballsim()
p.trajectory()
