# The Black_Hole class is derived from Simulton; it updates by finding+removing
#   any class derived from Prey whose center is contained inside its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    #Class variable radius
    radius = 10
    
    def __init__(self, x, y):
        #Black_Hole is a static Simulton, inherit Simulton characterstics
        Simulton.__init__(self, x, y, self.radius*2, self.radius*2)
    
    def update(self, model):
        #Empty set of preys currently eaten
        eaten = set()
        #Find preys in model.py 'balls' variable and checks if they are contained in black_hole
        for prey in model.find(Prey):
            if self.contains(prey.get_location()):
                #Remove eaten preys and add them to set
                eaten.add(prey)
                model.remove(prey)
        return eaten

    def display(self, canvas): 
        #For purposes of Pulsator and later classes that grow from eating, the display dimensions are based off of height and width,
        #as the class variable radius is static and doesn't change
        canvas.create_oval(self.get_location()[0]-self.get_dimension()[0]/2, 
                           self.get_location()[1]-self.get_dimension()[1]/2,
                           self.get_location()[0]+self.get_dimension()[0]/2, 
                           self.get_location()[1]+self.get_dimension()[1]/2,
                           fill='Black')
    
    #Override the contains class
    def contains(self,xy):     
        #self.get_dimension()[0]/2 is the same as height/2 or radius essentially
        return self.distance(xy) < self.get_dimension()[0]/2

    
