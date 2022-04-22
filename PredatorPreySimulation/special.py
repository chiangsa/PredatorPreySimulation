# The special class behaves similarly to a ball but is slower (speed 4). 
# As a matter of fact, Hunters can normally outrun them. However, when the Special sees
# a Hunter within 50 sight, it changes its angle to go opposite of the Hunter,
# gets a 3x speed boost for 5 cycles, and shoots out 2 half-sized balls perpendicular
# to its position to distract the Hunter while it escapes. These 2 balls are also
# slower than normal balls and move at a speed of 4 rather than 5 (like the Special itself). 
# Once the 5 cycle ability has ended,
# the special class enters a recharge phase for 35 cycles where it cannot use its
# boost and distract abilities. This recharge phase is visually shown by the
# green special class turning yellow for the duration. Its speed is also 
# reset back to 4 during this time.

from ball import Ball
from prey  import Prey
from hunter import Hunter
from mobilesimulton import Mobile_Simulton
from math import atan2


class Special(Prey):  
    
    sight = 50
    radius = 5
    base_speed = 4      #slightly slower than ball...but can speed up when needed
    speed_boost = 3     #3x speed boost multiplier
    boost_cooldown = 40 #cycle cooldown
    boost_duration = 5  #cycle duration
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, self.radius*2, self.radius*2,0,4)
        self.randomize_angle()
        self._color = 'Green'
        self._cooldown = 0
    
    def update(self, model):     
        #If cooldown is 0, checks for hunters and activates ability if needed
        if self._cooldown == 0:
            self._color = 'Green'
            target_list = set()
            for enemy in model.find(Hunter):
                distance = self.distance(enemy.get_location())
                enemy_radius = enemy.get_dimension()[0]/2
                #Takes into consideration the size of the Hunter (radius) when seeing if Hunter is in 
                #sight range of 50. Otherwise it would be blind to a Hunter with radius 50!
                if distance <= self.sight + enemy_radius:
                    target_list.add((enemy, distance))
            #Finds closest enemy
            x = sorted(target_list, key = lambda x: x[1])
            if x:
                #Directions said to not store not duplicate inherited instance variables like the 2 commented lines below
                #x1, y1 = self.get_location()
                #x2, y2 = x[0][0].get_location()
                
                #Changes angle and speed
                self.set_angle(atan2(self.get_location()[1]-x[0][0].get_location()[1], self.get_location()[0]-x[0][0].get_location()[0]))
                self.set_speed(self.get_speed() * self.speed_boost)
                #Adds cooldown to special object
                self._cooldown += self.boost_cooldown
                
                #Creates 2 decoy balls
                ball1 = Ball(self.get_location()[0], self.get_location()[1])
                ball1.set_angle(atan2(self.get_location()[1]-x[0][0].get_location()[1], self.get_location()[0]-x[0][0].get_location()[0])+90)
                ball1.set_speed(self.base_speed)
                ball1.set_dimension(self.radius, self.radius)
                model.add(ball1)
            
                ball2 = Ball(self.get_location()[0], self.get_location()[1])
                ball2.set_angle(atan2(self.get_location()[1]-x[0][0].get_location()[1], self.get_location()[0]-x[0][0].get_location()[0])-90)
                ball2.set_speed(self.base_speed)
                ball2.set_dimension(self.radius, self.radius)
                model.add(ball2)
        #If on cooldown, reduce cooldown timer and change speed and color if boost ability timer is up    
        else:
            self._cooldown -= 1
            if self._cooldown < self.boost_cooldown - self.boost_duration:
                self.set_speed(self.base_speed)
                self._color = 'Yellow'
                #print("BOOST HAS RUN OUT")
        
        self.move()
        self.wall_bounce()
        
    def display(self, canvas): #Special size is static (5), so based off radius, not height and width
        canvas.create_oval(self.get_location()[0]-self.radius, 
                           self.get_location()[1]-self.radius,
                           self.get_location()[0]+self.radius, 
                           self.get_location()[1]+self.radius,
                           fill=self._color)
            
