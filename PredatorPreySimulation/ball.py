# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 

from prey import Prey


class Ball(Prey): 
    #Class variable radius
    radius = 5
    
    def __init__(self, x,y):
        #Initialize with prey characteristics
        Prey.__init__(self, x, y, self.radius*2, self.radius*2,0,5)
        self.randomize_angle()
    
    def update(self, model):
        #Uses the mobile_simulton methods through inheritance (inherits from prey which inherits mobile_simulton)
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        #Display the ball
        canvas.create_oval(self.get_location()[0]-self.get_dimension()[0]/2, 
                           self.get_location()[1]-self.get_dimension()[1]/2,
                           self.get_location()[0]+self.get_dimension()[0]/2, 
                           self.get_location()[1]+self.get_dimension()[1]/2,
                           fill='Blue')
    