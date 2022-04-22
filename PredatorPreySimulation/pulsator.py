# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    #Class variable 'class_counter'
    class_counter = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        #Self variable for specific object's counter
        self._counter = 0
        
    def update(self, model):
        #Get set of eaten preys from Black_Hole update method
        eatens = Black_Hole.update(self, model)
        #If set is empty increase counter, and shrink size if needed
        if eatens == set():
            self._counter += 1
            if self._counter >= self.class_counter:
                self._counter = 0
                self.change_dimension(-1, -1)
                #current_width, current_height = self.get_dimension()
                if self.get_dimension()[0] <= 0 and self.get_dimension()[1] <= 0:
                    model.remove(self)
        #Otherwise increase in size based on how many things they ate
        else:
            x = len(eatens)
            self._counter = 0
            self.change_dimension(+x, +x)
        
        return eatens
        
