import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))
image=pygame.image.load("daisy.png")
running=True
while running:
    screen.fill((255,255,255))
    screen.blit(image,(100,100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()