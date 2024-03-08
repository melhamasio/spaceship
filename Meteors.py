from Meteor import *
import arcade

class Meteors:
    def __init__(self) -> None:
        self.meteors        = None
        self.num_meteors    = None
    
    def setup(self, num_meteors):
        self.num_meteors = num_meteors
        self.meteors = []

        for _ in range(num_meteors):
            m = Meteor()
            m.setup()

            self.meteors.append(m)
    
    def on_update(self):
        for m in self.meteors:
            m.on_update()
    
    def draw(self):
        for m in self.meteors:
            m.draw()
