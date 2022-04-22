import controller
import model   # See how update_all should pass on a reference to this module

#Use the reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special #My own Special class imported

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False #Copied from p5helper
cycle_count = 0
balls = set()
select = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world(): #Copied from p5helper
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset (): #Copied from p5helper
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start (): #Copied from p5helper
    global running
    running = True

#stop running the simulation (freezing it)
def stop (): #Copied from p5helper
    global running
    running = False 


#step just one update in the simulation
def step ():
    global running, cycle_count
    cycle_count += 1
    for b in balls.copy():
            b.update(model)
    running = False

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global select
    select = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    #print(x,y)
    global select
    if select in ('Ball', 'Floater', 'Black_Hole', 'Pulsator', 'Hunter', 'Special'):
        add(eval(str(select) + "({x1},{y1})".format(x1=x, y1=y)))
    
    elif select == 'Remove':
        for thingy in balls.copy():
            if thingy.contains((x,y)):
                remove(thingy)
                 


#add simulton s to the simulation
def add(s):
    #print("Adding a", s)
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    temp = set()
    for x in balls:
        if isinstance(x,p):
            temp.add(x)
    return temp


#call update for each simulton in this simulation (pass model as an argument) 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation

def update_all(): #Copied from p5helper
    global cycle_count
    if running:
        cycle_count += 1
        for b in balls.copy():
            b.update(model)

#For animation: (1st) delete all simultons on the canvas; (2nd) call display on
#  all simulton being simulated, adding each back to the canvas, maybe in a
#  new location; (3rd) update the label defined in the controller for progress 
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation

def display_all(): #Copied from p5helper
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+" updates/"+str(len(balls))+" simultons")
