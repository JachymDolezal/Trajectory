import math
import matplotlib.pyplot as plt
import numpy as np

#defines range of a barrier and land area
barrier = [200,400,200]
land_area = [900,1000,1]
#changes colors of the object and landing zone in the graph
Line1X=np.full(barrier[2],barrier[0])
Line1Y=np.arange(0,barrier[2],1)
Line2X=np.arange(barrier[0],barrier[1],1)
Line2Y=np.full(barrier[1]-barrier[0],barrier[2])
Line3X=np.full(barrier[2],barrier[1])
Line3Y=np.arange(0,barrier[2],1)

Lz1X=np.full(land_area[2],land_area[0])
Lz1Y=np.arange(0,land_area[2],1)
Lz2X=np.arange(land_area[0],land_area[1],1)
Lz2Y=np.full(land_area[1]-land_area[0],land_area[2])
Lz3X=np.full(land_area[2],land_area[1])
Lz3Y=np.arange(0,land_area[2],1)

class Trajectory:
#defines all the variables
    def __init__(self):
        self.grav = 9.81
        self.velocity = 0
        self.angle = 0
        self.Vx = 0
        self.Vy = 0
        self.radian = 0
        self.x = 0
        self.y = 0
        self.time = 0
        self.list_x = []
        self.list_y = []

#runs all the functions in for loops
    def run(self):
#changes angles for each trajectory
        for self.angle in np.arange(0,80,1):
            self.degree()
#changes changes velocity for each trajectory
            for self.velocity in np.arange(20,300,1):
#creates teporary lists
                temp_x = []
                temp_y = []
                barrier_check = False
                land_area_check = False
                self.vector()
#calculates x and y position in given time.
                for self.time in np.arange(0,100,0.1):
                    self.x = self.Vx*self.time
                    self.y = self.Vy*self.time-0.5*self.grav*self.time*self.time
                    if self.y < barrier[2] and (self.x > barrier[0] and self.x < barrier[1]):
                        barrier_check = True
                        break

                    if (self.x > land_area[0] and self.x < land_area[1]) and self.y < 0:
                        land_area_check = True
                        break

                    if self.y < 0:
                        break
                    temp_x.append(self.x)
                    temp_y.append(self.y)
                if barrier_check == False and land_area_check == True:
                    self.list_x = self.list_x + temp_x
                    self.list_y = self.list_y + temp_y

        self.graph()

#coverts degrees to radians
    def degree(self):
        pi = math.pi
        self.radian = (self.angle*pi/180)
#calculates the x and y vectors of the velocity
    def vector(self):
        self.Vx = self.velocity*math.cos(self.radian)
        self.Vy = self.velocity*math.sin(self.radian)
#graphs the data
    def graph(self):
        plt.plot(Line1X,Line1Y)
        plt.plot(Line2X,Line2Y)
        plt.plot(Line3X,Line3Y)
        plt.plot(Lz1X,Lz1Y)
        plt.plot(Lz2X,Lz2Y)
        plt.plot(Lz3X,Lz3Y)
        plt.plot(self.list_x,self.list_y)
        plt.show()
#runs the whole code
p = Trajectory()
p.run()
