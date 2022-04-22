# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 

from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    #Class variable radius
    radius = 5
    
    def __init__(self, x,y):
        #Initialize with prey characteristics
        Prey.__init__(self, x, y, self.radius*2, self.radius*2,0,5)
        self.randomize_angle()
        # 1 new instance variable for PhotoImage
        self._image = PhotoImage(file='ufo.gif')
    
    def update(self, model):
        x = random()
        # 30% Chance for this if statement to run and speed/angle to be changed
        if x <= 0.3:
            #CHANGE SPEED BY -0.5 to 0.5 value
            y = random() / 2
            if random() <= 0.50:
                y *= -1
            self.set_speed(self.get_speed() + y)
            
            #CHANGE RADIANS BY -0.5 to 0.5 value
            y = random() / 2
            if random() <= 0.50:
                y *= -1
            self.set_angle(self.get_angle() + y) #angle is already in radians, so add -0.5 to 0.5 to it (y)
            
            #Checks if speed is too high or low after changes
            if self.get_speed()> 7:
                self.set_speed(7)
            if self.get_speed()< 3:
                self.set_speed(3)
            
            #print("Angle changed, is now", self.get_angle())
            #print("Speed change, is now", self.get_speed())

        self.move()
        self.wall_bounce()
        
        
    def display(self, canvas): #Copied from p5 directions
        canvas.create_image(*self.get_location(),image=self._image)
       
    
