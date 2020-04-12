import pygame
import random

class Player(object):
    def __init__(self, img, largura, altura):
        self.spritePlayer = pygame.image.load(img)
        self.hitBox = pygame.Rect(32, 32, 32, 32)
        self.x =  (largura * 0.45)
        self.y = (altura * 0.8)

    def mover(self, tecla, bloco):
        (x, y) = (self.x, self.y)
        if keys[275]: self.x += 3 #letra D
        elif keys[276]: self.x -= 3 #letra A
        if keys[273]: self.y -=3 #letra W
        elif keys[274]: self.y += 3 #letra S
        self.teleportar()
        if self.hitBox.colliderect(bloco):
            (self.x, self.y) = (x, y)
            print ("Colisão!!!!!!!!")
        gameDisplay.blit(self.spritePlayer, (self.x,self.y))
    
    def teleportar(self):
        if self.x >= 800: self.x = 0
        elif self.x <= 0: self.x = 800
        if self.y >= 600: self.y = 0
        elif self.y <= 0: self.y = 600


class Ground(object):
    def __init__(self, img):
        self.spriteWall = pygame.image.load(img)

    def montar(self, x, y):
        gameDisplay.blit(self.spriteWall, (x ,y))    

class Wall(Ground):
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.spriteWall = pygame.image.load(img)
        self.hitBox = pygame.Rect(32, 32, 32, 32)

    def montar(self):
        gameDisplay.blit(self.spriteWall, (self.x ,self.y))   

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project: Game!')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

Jogador = Player("assets/img/spritePlayer.png", display_width, display_height)
Chao = Ground("assets/img/T6.png")
Parede = Wall("assets/img/P6.png", random.randint(0, 800), random.randint(0, 600))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: crashed = True

    if pygame.key.get_focused(): keys = pygame.key.get_pressed()
    gameDisplay.fill(white)

    for i in range(0, 800, 64):
        for l in range(0, 600, 64):
            Chao.montar(i ,l)
    
    Jogador.mover(keys, Parede.hitBox)
    Parede.montar()
 
    pygame.display.update()
    clock.tick(60)

    # cont = 0
    # for i in keys:
    #     if i == 1: print(cont)
    #     else: cont += 1

pygame.quit()
quit()