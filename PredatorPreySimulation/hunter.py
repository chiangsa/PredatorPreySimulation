# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    #Class variable sight
    sight = 200
    
    def __init__(self, x, y):
        #Hunter grows and shrinks like a Pulsator
        Pulsator.__init__(self, x, y)
        #Hunter moves like a Mobile_Simulton
        Mobile_Simulton.__init__(self, x, y, self.radius*2, self.radius*2, 0, 5)
        Mobile_Simulton.randomize_angle(self)
    
    def update(self, model):        
        target_set = set()
        #Set of 2-tuples with (prey, distance) format
        for prey in model.find(Prey):
            distance = self.distance(prey.get_location())
            if distance <= self.sight:
                target_set.add((prey, distance))
        #Find closest prey and change direction to match it
        x = sorted(target_set, key = lambda x : x[1])
        if x:
            #print("Closest target is", x[0])
            self.set_angle(atan2(x[0][0].get_location()[1]-self.get_location()[1], 
                                 x[0][0].get_location()[0]-self.get_location()[0]))
        
        #Shrinking behavior
        Pulsator.update(self, model)
        #Moving behavior
        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
            
            
