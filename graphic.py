import random
import pygame
                x = 590
                pygame.time.delay(1000)
                self.screen.blit(self.under_fire_artillery,(x,590))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (x,590))
                pygame.display.flip()
        else :
                shot=pygame.mixer.Sound("shot.wav")
                shot.play()
                pygame.time.delay(1000)
                hit=pygame.mixer.Sound("bomb_hit.wav")
                hit.play()
                if position == 3:
                    x = 430        
                    pygame.time.delay(1000)
                    self.screen.blit(self.ground_damage,(x,610))
                    pygame.display.flip()
                    pygame.time.delay(700)
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

        while True:
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                     pos = pygame.mouse.get_pos()
                     if self.exit_button.collidepoint(pos):
                                return "exit"
                     if self.restart_button.collidepoint(pos):
                                return "restart"
                
            #pygame.time.delay(3000)
        #pygame.quit()

