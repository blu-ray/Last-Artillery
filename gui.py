import pygame

pygame.init()
screen = pygame.display.set_mode((576, 608))
screen.fill((255, 255, 255))
done = False
image = pygame.image.load('1.jpg')
bg = pygame.image.load('2.jpg')
screen.blit(bg , (0,0))
clock = pygame.time.Clock()
x,y = 255,0
k=5
screen.blit(image, (255, 525))
while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True

                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT):
        
                        pressed = pygame.key.get_pressed()

                        if pressed[pygame.K_LEFT] and x >= 175:
                                for i in range(20):
                                        screen.blit(image, (x-4, 525))
                                        x -= 4
                                        pygame.display.flip()
                                        clock.tick(60)

                                
                        if pressed[pygame.K_RIGHT] and x <= 335:
                                for j in range(20):
                                        screen.blit(image, (x+4, 525))
                                        x += 4
                                        pygame.display.flip()
                                        clock.tick(60)
        pygame.display.flip()

        i,j=0,0
