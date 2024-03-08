from Engine import *
import arcade

class Spaceship(Engine):
    def __init__(self, spaceship_index=0, scale=0.5, npc=False) -> None:
        super().__init__(spaceship_index, scale, npc)

    def setup(self):
        super().setup()
    
    def on_update(self):
        self.move()
        exts = self.get_extremidades()
        #print(self.display.detect_end_display(exts))