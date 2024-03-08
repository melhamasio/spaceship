from Engine import *
import random

class Display:
    def __init__(self) -> None:
        self.height         = 600
        self.width          = 800
        self.flag_infinity  = True
    

    def getStartPositionA(self, player_width, player_height):
        
        x = (self.width/2) + (player_width/2)
        y = 100 + player_height
        
        return (x, y )
    
    def getRandomPositionUP(self):
        y = self.height
        x = random.randint(0, self.width)

        return (x, y)

    """
    DETECT END DISPLAY

    A função verifica se todo o personagem já extrapolou os limites do display,
    por exemplo:

    > Para um personagem extrapolar os limites superiores, a sua extremidade inferior deve
    ser maior que o limite superior do display
    """
    def detect_end_display(self, exts):
        up, right, down, left = exts

        dictFlags = {
            'up'    : False,
            'right' : False,
            'down'  : False,
            'left'  : False,

        }
        
        if(down > self.height):
            dictFlags['up'] = True

        if(up < 0):
            dictFlags['down'] = True
        
        if(left > self.width):
            dictFlags['right'] = True
        
        if(right < 0):
            dictFlags['left'] = True
        


        return dictFlags
