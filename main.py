import pygame

class Player(object):
    def __init__(self, img, largura, altura):
        self.spritePlayer = pygame.image.load(img)
        self.x =  (largura * 0.45)
        self.y = (altura * 0.8)

    def mover(self, tecla):
        if keys[100]: self.x +=1 #letra D
        if keys[97]: self.x -= 1 #letra A
        if keys[119]: self.y -=1 #letra W
        if keys[115]: self.y += 1 #letra S
        gameDisplay.blit(self.spritePlayer, (self.x,self.y))

class Wall(object):
    def __init__(self, img):
        self.spriteWall = pygame.image.load(img)

    def montar(self, x, y):
        gameDisplay.blit(self.spriteWall, (x ,y))

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
Parede = Wall("assets/img/t6erra.png")

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: crashed = True

    if pygame.key.get_focused(): keys = pygame.key.get_pressed()
    gameDisplay.fill(white)
    Jogador.mover(keys)
    Parede.montar(500, 500)

        
    pygame.display.update()
    clock.tick(60)

    # cont = 0
    # for i in keys:
    #     if i == 1: print(cont)
    #     else: cont += 1

pygame.quit()
quit()