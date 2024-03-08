from Display import *
import arcade
import random


class Engine:
    def __init__(self, spaceship_index=0, scale=0.5, npc=False) -> None:
        self.display         = Display()
        self.player          = None
        self.player_list     = None
        self.spaceship_index =  spaceship_index
        self.scale           = scale
        self.npc             = npc
        self.flag_game_over  = False
        self.speed           = None

        #  Dimensões do personagem
        self.width           = None
        self.height          = None

        """
        FLAGS DE MOVIMENTAÇÃO

        Quando uma flag está ativa, o personagem está em movimento,
        do contrário está parado.

        Uma flag está ativa quando um botão é pressionado e desativada quando
        o botão é liberado
        """

        self.flagMove = {
            'up'    : False,
            'right' : False,
            'down'  : False,
            'left'  : False
        }
        
    
    # Retorna a nave corerespondente e sua velocidade
    def _get_spaceship(self):
        spaceships = [
            ('sprites/spaceship_a.png'  , 4, 167, 167),
            ('sprites/spaceship_b.png'  , 3, 351, 363),
            ('sprites/spaceship_c.png'  , 9, 242, 162),
            ('sprites/meteor.png'       , 10, 205, 145)

        ]

        return spaceships[self.spaceship_index]


    def setup(self, flagRandomPosition=False, flagRandomScale=False, flagRandomSpeed=False):
        self.flag_game_over = False
        
        # Busca o personagem e sua caractreística
        sprite, self.speed, width, height  = self._get_spaceship()
        
        # Dimensões originais
        self._first_width = width
        self._first_height= height
        
        # Dimensões do personagem
        if(flagRandomScale):
            self.scale = random.randint(1, 10)/30
        
        # Velocidade
        if(flagRandomSpeed):
            self.speed = random.randint(1, 10)

        self.width  = width*self.scale
        self.height = height*self.scale

        # Monta o player e define sua posição inicial
        if(self.spaceship_index == 3):
            self.player         = arcade.Sprite(sprite, self.scale, angle=-280)
        else:
            self.player         = arcade.Sprite(sprite, self.scale)

        if(flagRandomPosition):
            startPosition       = self.display.getRandomPositionUP()
        else:
            startPosition       = self.display.getStartPositionA(100, 100)

        self.player.center_x= startPosition[0]
        self.player.center_y= startPosition[1]

        # Inicializa e add na lista
        self.player_list    = arcade.SpriteList()

        self.player_list.append(self.player)

    
    # Pausa qualquer tipo de movimento que esteja acontecendo
    def stop_player(self):
        self.flagMove['up']     = False
        self.flagMove['right']  = False
        self.flagMove['down']   = False
        self.flagMove['left']   = False
    
    # Direciona o movimento para cima
    def move_up(self):
        self.stop_player()
        self.flagMove['up'] = True
    
    # Direciona o movimento para direita
    def move_right(self):
        self.stop_player()
        self.flagMove['right'] = True
    
    # Direciona o movimento para baixo
    def move_down(self):
        self.stop_player()
        self.flagMove['down'] = True
    
    # Direciona o movimento para 
    def move_left(self):
        self.stop_player()
        self.flagMove['left'] = True
    
    def game_over(self):
        self.flag_game_over = True

    
    """
    GET EXTREMIDADES DO PERSONAGEM

    A função calcula as extremidades do personagem
    e retorna os valores
    
    > extremidades:
        (dianteira, direita, traseira, esquerda)
    """
    def get_extremidades(self):
        # Eixo y
        up   = self.player.center_y + (0.5*self.height)
        down = self.player.center_y - (0.5*self.height)

        # Eixo x
        left    = self.player.center_x - (0.5*self.width)
        right   = self.player.center_x + (0.5*self.width)
    
        return (up, right, down, left)

    def detect_out_display(self):
        exts = self.get_extremidades()
        flagOut = self.display.detect_end_display(exts)

        return flagOut

    """
    IDENTIFICAÇÃO DAS TECLALS PRESSIONADAS E LIBERADAS

    W: Cima
    D: Direita
    S: Baixo
    A: Esquerda
    """

    def key_press(self, key):
        if(not self.npc):
            if(key == arcade.key.W):
                self.flagMove['up'] = True
            
            if(key == arcade.key.D):
                self.flagMove['right'] = True
            
            if(key == arcade.key.S):
                self.flagMove['down'] = True
            
            if(key == arcade.key.A):
                self.flagMove['left'] = True
    
    def key_up(self, key):
        if(not self.npc):
            if(key == arcade.key.W):
                self.flagMove['up'] = False
            
            if(key == arcade.key.D):
                self.flagMove['right'] = False
            
            if(key == arcade.key.S):
                self.flagMove['down'] = False
            
            if(key == arcade.key.A):
                self.flagMove['left'] = False

    # Desenha somente se o player ainda estiver em jogo
    def draw(self):
        if(not self.flag_game_over):
            self.player_list.draw()
    
    # A função movimenta o personagem
    def move(self):
        if(self.flagMove['up']):
            self.player.center_y += self.speed
        
        if(self.flagMove['down']):
            self.player.center_y -= self.speed
        
        if(self.flagMove['left']):
            self.player.center_x -= self.speed
        
        if(self.flagMove['right']):
            self.player.center_x += self.speed


    def printPosition(self):
        print(self.player.center_x, self.player.center_y)
        

        