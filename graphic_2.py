import random
                    self.screen.blit(self.ground_clean,(x,610))
                    pygame.display.flip()
                    
                elif position == 1:
                    x= 270
                    pygame.time.delay(1000)
                    self.screen.blit(self.ground_damage,(x,610))
                    pygame.display.flip()
                    pygame.time.delay(700)
                    self.screen.blit(self.ground_clean,(x,610))
                    pygame.display.flip()
                elif position == 2:
                    x= 350
                    pygame.time.delay(1000)
                    self.screen.blit(self.ground_damage,(x,610))
                    pygame.display.flip()
                    pygame.time.delay(700)
                    self.screen.blit(self.ground_clean,(x,610))
                    pygame.display.flip()
                elif position == 4:
                    x= 510
                    pygame.time.delay(1000)
                    self.screen.blit(self.ground_damage,(x,610))
                    pygame.display.flip()
                    pygame.time.delay(700)
                    self.screen.blit(self.ground_clean,(x,610))
                    pygame.display.flip()
                elif position == 5:
                    x= 590
                    pygame.time.delay(1000)
                    self.screen.blit(self.ground_damage,(x,610))
                    pygame.display.flip()
                    pygame.time.delay(700)
                    self.screen.blit(self.ground_clean,(x,610))
                    pygame.display.flip()
    def under_double(self,pos):
        shot=pygame.mixer.Sound("shot.wav")
        shot.play()
        pygame.time.delay(1000)
        hit=pygame.mixer.Sound("bomb_hit.wav")
        hit.play()
        pygame.time.delay(1000)
        if pos==1:
            if self.myposition==1:
                self.screen.blit(self.under_fire_artillery,(270,590))
                self.screen.blit(self.ground_damage,(350,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (270,590))
                self.screen.blit(self.ground_clean,(350,610))
                pygame.display.flip()
            elif self.myposition==2:
                
                self.screen.blit(self.under_fire_artillery,(350,590))
                self.screen.blit(self.ground_damage,(270,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (350,590))
                self.screen.blit(self.ground_clean,(270,610))
                pygame.display.flip()
            else :
                self.screen.blit(self.ground_damage,(270,610))
                self.screen.blit(self.ground_damage,(350,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.ground_clean,(270,610))
                self.screen.blit(self.ground_clean,(350,610))

###################                
        elif pos==2:
            if self.myposition==2:
                self.screen.blit(self.under_fire_artillery,(350,590))
                self.screen.blit(self.ground_damage,(430,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (350,590))
                self.screen.blit(self.ground_clean,(430,610))
                pygame.display.flip()
            elif self.myposition==3:
                
                self.screen.blit(self.under_fire_artillery,(430,590))
                self.screen.blit(self.ground_damage,(350,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (430,590))
                self.screen.blit(self.ground_clean,(350,610))
                pygame.display.flip()
            else :
                self.screen.blit(self.ground_damage,(430,610))
                self.screen.blit(self.ground_damage,(350,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.ground_clean,(430,610))
                self.screen.blit(self.ground_clean,(350,610))

#########################
        elif pos==3:                             
            if self.myposition==3:
                self.screen.blit(self.under_fire_artillery,(430,590))
                self.screen.blit(self.ground_damage,(510,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (430,590))
                self.screen.blit(self.ground_clean,(510,610))
                pygame.display.flip()
            elif self.myposition==4:
                
                self.screen.blit(self.under_fire_artillery,(510,590))
                self.screen.blit(self.ground_damage,(430,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (510,590))
                self.screen.blit(self.ground_clean,(430,610))
                pygame.display.flip()
            else :
                self.screen.blit(self.ground_damage,(510,610))
                self.screen.blit(self.ground_damage,(430,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.ground_clean,(510,610))
                self.screen.blit(self.ground_clean,(430,610))

########################               
        elif pos==4 or pos==5:               #1:270://///2:350////// 3:430//////4:510//////5:590
            if self.myposition==4:
                self.screen.blit(self.under_fire_artillery,(510,590))
                self.screen.blit(self.ground_damage,(590,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (510,590))
                self.screen.blit(self.ground_clean,(590,610))
                pygame.display.flip()
            elif self.myposition==5:
                self.screen.blit(self.under_fire_artillery,(590,590))
                self.screen.blit(self.ground_damage,(510,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (590,590))
                self.screen.blit(self.ground_clean,(510,610))
                pygame.display.flip()
            else :
                self.screen.blit(self.ground_damage,(590,610))
                self.screen.blit(self.ground_damage,(510,610))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.ground_clean,(590,610))
                self.screen.blit(self.ground_clean,(510,610))

    def finish(self , code):

        if code == 1:
            self.screen.blit(self.win_pic,(300 ,200))
            pygame.display.flip()

        elif code == 2:
            self.screen.blit(self.lose_pic,(300 ,200))
            pygame.display.flip()


        elif code == 3:
            self.screen.blit(self.no_win_pic,(300 ,200))
            pygame.display.flip()

        elif code == 4:
            self.screen.blit(self.you_won_pic,(300 ,200))
            pygame.display.flip()

        elif code == 5:
            self.screen.blit(self.you_lost_pic,(300 ,200))
            pygame.display.flip()

        pygame.time.delay(3000)
        pygame.quit()

    def move(self):
        pygame.display.flip()
        clock = pygame.time.Clock()
        done=False
        while not done :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if (event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT)):
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_LEFT] and x >= 350:
                                self.myposition-=1
                                for i in range(20):
                                        self.screen.blit(self.artillery, (x-4, 590))
                                        x -= 4
                                        self.screen.blit(self.white,(893,58))
                                        self.my_pos = self.myfont.render(str(self.myposition), True, (0,0,0))
                                        self.screen.blit(self.my_pos, (893, 58))
                                        pygame.display.flip()
                                        clock.tick(60)
                                
                        if pressed[pygame.K_RIGHT] and x <= 535:
                                self.myposition+=1
                                for j in range(20):
                                        self.screen.blit(self.artillery, (x+4, 590))
                                        x += 4
                                        self.screen.blit(self.white,(893,58))
                                        self.my_pos = self.myfont.render(str(self.myposition), True, (0,0,0))
                                        self.screen.blit(self.my_pos, (893, 58))
                                        pygame.display.flip()
                                        clock.tick(60)
                               
                        if event.type == pygame.KEYDOWN and (event.key == pygame.K_ENTER):
                            return self.myposition

