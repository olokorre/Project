import pygame

class Player(object):
    def move(self):
        pass

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project: Cu!')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('assets/img/spritePlayer.png')

print(type(carImg))

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

    keys = pygame.key.get_pressed()

    cont = 0
    for i in keys:
        if i == 1: print(cont)
        else: cont += 1

    if keys[100]: #letra d
        x +=1
    if keys[97]: #letra a
        x -= 1
    if keys[119]: #letra w
        y -=1
    if keys[115]: #letra s
        y += 1

pygame.quit()
quit()