import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
screen.fill((255, 255, 255))
done = False
image = pygame.image.load('1.jpg')
clock = pygame.time.Clock()
x,y = 0,0
k=5

for i in range(20):
    screen.blit(image, (x+5, 600))
    x += 5

                        
                #screen.blit(image, (x+5, 600))
                #x += 5
                
    pygame.display.flip()
    clock.tick(60)
