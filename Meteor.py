from Engine import *

class Meteor(Engine):
    def __init__(self, spaceship_index=3, scale=0.5, npc=True) -> None:
        super().__init__(spaceship_index, scale, npc)
    
    def setup(self):
        super().setup(flagRandomPosition=True, flagRandomScale=True, flagRandomSpeed=True)
        self.move_down()

    def detect_game_over(self):
        exts = self.get_extremidades()
        flagsOut = self.display.detect_end_display(exts)
        print(flagsOut)
        if(flagsOut['down']):
            self.flag_game_over = True

    def resetNPC(self):
        # Posição
        startPosition       = self.display.getRandomPositionUP()
        self.player.center_x= startPosition[0]
        self.player.center_y= startPosition[1]
        self.flag_game_over = False

        # Dimensões
        self.scale = random.randint(1, 10)/30
        self.width  = self._first_width*self.scale
        self.height = self._first_height*self.scale

        self.player.scale = self.scale

        # Velocidade
        self.speed = random.randint(1, 10)



    def on_update(self):
        self.move()
        self.detect_game_over()
        
        if(self.flag_game_over):
            self.resetNPC()

        

        

