import random
import pygame
from pygame import *
class graphic(object):
    def __init__(self):
        self.pre_loads()
    def pre_loads(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1006, 682),FULLSCREEN)
        self.screen.fill((255, 255, 255))
        self.atomic_rockets=1
        self.double_rockets=1
        self.ultra_rockets=1
        
        self.bg = pygame.image.load('background.jpg')#
        self.artillery = pygame.image.load('artillery.png')#
        self.screen.blit(self.bg , (0,0))
        self.screen.blit(self.artillery , (430,590))
        self.rockets=100

        self.game_icon=pygame.image.load("Game_icon.png")

        self.atomic_active= pygame.image.load('atomic_bomb_active.png')#
        self.screen.blit(self.atomic_active,(16,105))
       
        self.double_active= pygame.image.load('double_bomb_active.png')#
        self.screen.blit(self.double_active,(16,235))
       
        self.ultra_active= pygame.image.load('ultra_bomb_active.png')#
        self.screen.blit(self.ultra_active,(16,360))
      

        self.atomic_deactive= pygame.image.load('atomic_bomb_deactive.png')
        self.double_deactive= pygame.image.load('double_bomb_deactive.png')
        self.ultra_deactive= pygame.image.load('ultra_bomb_deactive.png')

        self.my_damage=pygame.image.load('7-you.png')#
        self.screen.blit(self.my_damage,(825,340))
        self.enemy_damage=pygame.image.load('7-enemy.png')#
        self.screen.blit(self.enemy_damage,(925,340))

        self.target_pos_up=pygame.image.load('target_pos_up_active.png').convert_alpha()
        self.screen.blit(self.target_pos_up,(930,135))
        pygame.display.flip()
        self.target_pos_up =self.target_pos_up.get_rect()
        self.target_pos_up.move_ip(930,135)
        
        self.target_pos_down=pygame.image.load('target_pos_down_active.png').convert_alpha()
        self.screen.blit(self.target_pos_down,(860,135))
        pygame.display.flip()
        self.target_pos_down =self.target_pos_down.get_rect()
        self.target_pos_down.move_ip(860,135)
        
        self.target_pos_up_de=pygame.image.load('target_pos_up_deactive.png')
        self.target_pos_down_de=pygame.image.load('target_pos_down_deactive.png')

        self.atomic_button = pygame.image.load('atomic_bomb_button.png').convert_alpha()#
        self.screen.blit(self.atomic_button,(18,18))
        pygame.display.flip()
        self.atomic_button =self.atomic_button.get_rect()
        self.atomic_button.move_ip(18,18)

        self.double_button = pygame.image.load('double_bomb_button.png').convert_alpha()#
        self.screen.blit(self.double_button,(18,145))
        pygame.display.flip()
        self.double_button =self.double_button.get_rect()
        self.double_button.move_ip(18,145)
        
        self.ultra_button = pygame.image.load('ultra_bomb_button.png').convert_alpha()#
        self.screen.blit(self.ultra_button,(18,275))

        self.white=pygame.image.load("white_fill.png")

        self.under_fire_artillery=pygame.image.load("under_fire_artillery.png")

        self.tar_des=pygame.image.load("tar_destroyed.png")

        self.black_bg=pygame.image.load("num_special_rocket.png")
        self.white_bg=pygame.image.load("num_zero.png")
        self.my_status_pic=pygame.image.load("status2.png")
        self.screen.blit(self.my_status_pic,(15,517))
        self.bonus_pic=pygame.image.load("bonus.png")######
        self.screen.blit(self.bonus_pic,(10,400))
        self.status_box=pygame.image.load("status.png")

        self.atomic_bonus=pygame.image.load("atomic.png")
        self.double_bonus=pygame.image.load("double.png")
        self.ultra_bonus=pygame.image.load("ultra.png")


        self.ground_clean=pygame.image.load("ground_hide.png")
        
        self.screen.blit(self.status_box,(830,550))
        
        pygame.display.flip()
        
        self.fire_flag=False
        self.tar_select = 3
        self.myposition = 3

        
        self.ground_damage=pygame.image.load("ground_damage.png")

        self.white_rockets=pygame.image.load("white_rockets.jpg")
        

        self.ultra_button =self.ultra_button.get_rect()
        self.ultra_button.move_ip(18,275)
        self.myfont = pygame.font.SysFont("",50)
        self.myfont2 = pygame.font.SysFont("",20)
        self.myfont3 = pygame.font.SysFont("",30)
        pygame.display.flip()
        self.bg_music()
        self.rockets_show()
        self.num_special_rockets()
        
        
        self.data = []
        

        self.code =0##
        self.my_pos = self.myfont.render(str(self.myposition), 3, (0,0,0))
        self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
        self.screen.blit(self.my_pos, (893, 58))
        self.screen.blit(self.tar_text,(892,135))

        self.exit_button=pygame.image.load("exit.png").convert_alpha()
        self.screen.blit(self.exit_button,(20,635))
        pygame.display.flip()
        self.exit_button =self.exit_button.get_rect()
        self.exit_button.move_ip(20,635)

        self.restart_button=pygame.image.load("restart.png").convert_alpha()
        self.screen.blit(self.restart_button,(20,600))
        pygame.display.flip()
        self.restart_button =self.restart_button.get_rect()
        self.restart_button.move_ip(20,600)
        


        self.win_pic = pygame.image.load("game_won.png")
        self.lose_pic = pygame.image.load("game_lost.png")
        self.no_win_pic = pygame.image.load("no_winner.png")
        self.you_won_pic = pygame.image.load("you_won.png")
        self.you_lost_pic = pygame.image.load("you_lost.png")



        self.end_flag = False

    def move_select(self):

        pygame.display.flip()
        normal_flag=True
        if self.rockets==0:
            normal_flag=False
        atomic_flag=False
        double_flag=False
        ultra_flag=False
        clock = pygame.time.Clock()
        x,y = 430,0
        if self.myposition == 3:
            x,y = 430,0
        elif self.myposition == 1:
            x,y = 270,0
        elif self.myposition == 2:
            x,y = 350,0
        elif self.myposition == 4:
            x,y = 510,0
        elif self.myposition == 5:
            x,y = 590,0

        k=5
        done = False
        
        while not done and not self.end_flag:

##############################az____inja____________________#####################
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
                    if (self.fire_flag==False and event.type==pygame.KEYDOWN and (event.key == pygame.K_f) and self.rockets+self.atomic_rockets+self.double_rockets+self.ultra_rockets>=1) :
                        if normal_flag or atomic_flag or double_flag or ultra_flag :
                            self.fire_flag=True
                            self.data = self.fire(self.myposition,x,normal_flag,atomic_flag,double_flag,ultra_flag)
                            print self.myposition
                            done = True

                    if (self.fire_flag==False and event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT)):
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

                    if pygame.mouse.get_pressed()[0] :
                        pos = pygame.mouse.get_pos()
                        if self.exit_button.collidepoint(pos):
                            pygame.quit()
                        if self.restart_button.collidepoint(pos):
                            return "restart"
                        if self.atomic_button.collidepoint(pos)and not self.fire_flag and self.atomic_rockets!=0:
                            if not atomic_flag :
                                self.weapon_select_sound()
                                atomic_flag=True
                                double_flag=False
                                ultra_flag=False
                                normal_flag=False

                                self.screen.blit(self.atomic_deactive,(16,105))

                            elif atomic_flag:
                                 self.weapon_select_sound()
                                 atomic_flag=False
                                 normal_flag=True

                                 self.screen.blit(self.atomic_active,(16,105))


                            print "__________atomic_bomb_________"
                   ####
                        elif self.double_button.collidepoint(pos) and not self.fire_flag and self.double_rockets!=0:
                            self.weapon_select_sound()
                            if not double_flag:
                                if atomic_flag==True :

                                    self.screen.blit(self.atomic_active,(16,105))

                                if ultra_flag==True :

                                    self.screen.blit(self.ultra_active,(16,360))

                                atomic_flag=False
                                double_flag=True
                                ultra_flag=False
                                normal_flag=False

                                self.screen.blit(self.double_deactive,(16,235))

                            elif double_flag:
                                 self.weapon_select_sound()
                                 double_flag=False
                                 normal_flag=True


                                 self.screen.blit(self.double_active,(16,235))



                            print "__________double_bomb_________"
                       ####
                        elif self.ultra_button.collidepoint(pos) and not self.fire_flag and self.ultra_rockets!=0:
                            self.weapon_select_sound()
                            if not ultra_flag:
                                if atomic_flag==True :

                                    self.screen.blit(self.atomic_active,(16,105))

                                if double_flag==True :

                                    self.screen.blit(self.double_active,(16,235))

                                normal_flag=False
                                atomic_flag=False
                                double_flag=False
                                ultra_flag=True

                                self.screen.blit(self.ultra_deactive,(16,360))

                            elif ultra_flag:
                                 self.weapon_select_sound()
                                 ultra_flag=False
                                 normal_flag=True


                                 self.screen.blit(self.ultra_active,(16,360))



                            print "__________ultra_bomb_________"

                        elif self.target_pos_up.collidepoint(pos) and not self.fire_flag:
                            if self.tar_select<4:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select+1
                                self.screen.blit(self.white,(890,135))
                                self.target_pos_up=pygame.image.load('target_pos_up_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_up,(930,135))
                                pygame.display.flip()
                                self.target_pos_up =self.target_pos_up.get_rect()
                                self.target_pos_up.move_ip(930,135)

                                self.target_pos_down=pygame.image.load('target_pos_down_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_down,(860,135))
                                pygame.display.flip()
                                self.target_pos_down =self.target_pos_down.get_rect()
                                self.target_pos_down.move_ip(860,135)
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                                self.screen.blit(self.tar_text,(894,135))###
                                print self.tar_select
                            elif self.tar_select==4:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select+1
                            ############
                                self.screen.blit(self.white,(890,135))
                                self.screen.blit(self.target_pos_up_de,(930,135))
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                                self.screen.blit(self.tar_text,(894,135))###
                                print self.tar_select


                        elif self.target_pos_down.collidepoint(pos) and not self.fire_flag:
                            if self.tar_select>2:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select-1
                                self.screen.blit(self.white,(890,135))
                                self.target_pos_up=pygame.image.load('target_pos_up_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_up,(930,135))
                                pygame.display.flip()
                                self.target_pos_up =self.target_pos_up.get_rect()
                                self.target_pos_up.move_ip(930,135)
                                self.target_pos_down=pygame.image.load('target_pos_down_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_down,(860,135))
                                pygame.display.flip()
                                self.target_pos_down =self.target_pos_down.get_rect()
                                self.target_pos_down.move_ip(860,135)
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                                self.screen.blit(self.tar_text,(894,135))###
                                print self.tar_select
                            elif self.tar_select==2:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select-1
                                self.screen.blit(self.white,(890,135))
                                self.screen.blit(self.target_pos_down_de,(860,135))
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                                self.screen.blit(self.tar_text,(894,135))###
                                print self.tar_select
                        self.num_special_rockets()
                        pygame.display.flip()
############################################_____ta inja_______##############################
    def bg_music(self):
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(10000)
        pygame.mixer.music.set_volume(0.6)
    def tar_destroy(self):
        self.screen.blit(self.tar_des,(120,230))
        #sound
    def tar_hit(self , check):
        if check :
            self.screen.blit(self.status_box,(830,550))
            self.tar_hit_text=self.myfont.render("hit",3,(0,0,0))
            self.screen.blit(self.tar_hit_text,(880,608))
            pygame.display.flip()
            pygame.time.delay(1500)
            self.screen.blit(self.status_box,(830,550))
            pygame.display.flip()
            #bg
            #sound
        else:
            self.screen.blit(self.status_box,(830,550))
            self.tar_didnt_hit_text=self.myfont.render("no hit",3,(0,0,0))
            self.screen.blit(self.tar_didnt_hit_text,(855,605))
            pygame.display.flip()
            pygame.time.delay(1500)
            self.screen.blit(self.status_box,(830,550))
            pygame.display.flip()

    def my_hit(self , check):
       if check:
           self.screen.blit(self.my_status_pic,(15,517))
           self.tar_hit_text=self.myfont3.render("hit",3,(0,0,0))
           self.screen.blit(self.tar_hit_text,(50,558))
           pygame.display.flip()
           pygame.time.delay(1500)
           self.screen.blit(self.my_status_pic,(15,517))
           pygame.display.flip()
           #####whitebg
       else:
           self.screen.blit(self.my_status_pic,(15,517))
           self.tar_not_hit_text=self.myfont3.render("no hit",3,(0,0,0))
           self.screen.blit(self.tar_not_hit_text,(35,558))
           pygame.display.flip()
           pygame.time.delay(1500)
           self.screen.blit(self.my_status_pic,(15,517))
           pygame.display.flip()
       #sound


       
    def weapon_select_sound(self):
        weapon_select=pygame.mixer.Sound("select_weapon.wav")
        weapon_select.play()
    def damage(self,my_damage , enemy_damage):
       my_damage=pygame.image.load(str(7-my_damage)+'-you.png')
       enemy_damage=pygame.image.load(str(7-enemy_damage)+'-enemy.png')
       self.screen.blit(my_damage,(825,340))
       self.screen.blit(enemy_damage,(925,340))

    
    def rockets_show(self):
       self.screen.blit(self.white_rockets,(850,220))
       self.tar_didnt_hit_text=self.myfont.render(str(self.rockets),3,(0,0,0))
       self.screen.blit(self.tar_didnt_hit_text,(880,225))

    def num_special_rockets(self):
        self.atomic_num=self.myfont2.render("x"+str(self.atomic_rockets),3,(255,255,255))
        self.double_num=self.myfont2.render("x"+str(self.double_rockets),3,(255,255,255))
        self.ultra_num=self.myfont2.render("x"+str(self.ultra_rockets),3,(255,255,255))
        if  self.atomic_rockets>=1:
            self.screen.blit(self.black_bg,(105,106))
            self.screen.blit(self.atomic_num,(112,111))
        if  self.atomic_rockets==0:
            self.screen.blit(self.white_bg,(105,106))
            self.screen.blit(self.atomic_num,(112,111))    
    
        if self.double_rockets>=1:
            self.screen.blit(self.black_bg,(105,236))
            self.screen.blit(self.double_num, (112,241))
        if self.double_rockets==0:
            self.screen.blit(self.white_bg,(105,236))
            self.screen.blit(self.double_num, (112,241))
            
        if self.ultra_rockets>=1:
            self.screen.blit(self.black_bg,(105,361))
            self.screen.blit(self.ultra_num, (112,366))
        if self.ultra_rockets==0:
            self.screen.blit(self.white_bg,(105,361))
            self.screen.blit(self.ultra_num, (112,366))
            
    def fire(self ,myposition,x,normal_flag,atomic_flag,double_flag,ultra_flag):
        if normal_flag:
            self.rockets-=1
            self.rockets_show()
        elif atomic_flag:
            self.atomic_rockets-=1
            if self.atomic_rockets!=0:
                self.screen.blit(self.atomic_active,(16,105))
        elif double_flag:
            self.double_rockets-=1
            pygame.display.flip()
            if self.double_rockets!=0:
                self.screen.blit(self.double_active,(16,235))
        elif ultra_flag:
            self.ultra_rockets-=1
            if self.ultra_rockets!=0:
                self.screen.blit(self.ultra_active,(16,360))
        self.num_special_rockets()
        shot=pygame.mixer.Sound("shot.wav")
        shot.play()
        firing_artillery=pygame.image.load(str(myposition)+".png")
        pygame.display.flip()
        pygame.time.delay(500)
        self.screen.blit(firing_artillery,(x,590))
        pygame.display.flip()
        pygame.time.delay(500)
        self.screen.blit(self.artillery , (x,590))
        pygame.display.flip()
        pygame.time.delay(500)
        hit=pygame.mixer.Sound("bomb_hit.wav")
        hit.play()
        pygame.time.delay(1200)
        tar_blast=pygame.image.load("tar_ground_hit.png")
        self.screen.blit(tar_blast,(453,318))
        pygame.display.flip()
        pygame.time.delay(1000)
        hide_fire=pygame.image.load("white.png")
        self.screen.blit(hide_fire,(453,318))
        pygame.display.flip()
        if normal_flag:
            self.code = 0
        elif atomic_flag:
            self.code =1
        elif double_flag:
            self.code =2
        elif ultra_flag:
            self.code =3
        return [self.myposition , self.tar_select ,self.code ]

    def bonus(self,bonus_code):
        #sound
        if bonus_code==1:
            self.screen.blit(self.atomic_bonus,(10,400))
            self.atomic_rockets+=1
            self.screen.blit(self.atomic_active,(16,105))
            self.num_special_rockets()
            pygame.display.flip()
            pygame.time.delay(1000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            
            
        elif bonus_code==2:
            self.screen.blit(self.double_bonus,(10,400))
            self.double_rockets+=1
            self.screen.blit(self.double_active,(16,235))
            self.num_special_rockets()
            pygame.display.flip()
            pygame.time.delay(1000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            
           
        elif bonus_code==3:
            self.screen.blit(self.ultra_bonus,(10,400))
            self.ultra_rockets+=1
            self.screen.blit(self.ultra_active,(16,360))
            self.num_special_rockets()
            pygame.display.flip()
            pygame.time.delay(1000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            
       
###############################    
    def get_posg(self):
        return self.myposition

    def get_targ(self):
        return self.tar_select
###############################
    def under_fire(self,position):
        if position==self.myposition:
            shot=pygame.mixer.Sound("shot.wav")
            shot.play()
            pygame.time.delay(1000)
            hit=pygame.mixer.Sound("bomb_hit.wav")
            hit.play()
            if self.myposition == 3:
                x = 430
                pygame.time.delay(1000)
                self.screen.blit(self.under_fire_artillery,(x,590))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (x,590))
                pygame.display.flip()
            elif self.myposition == 1:
                x = 270
                pygame.time.delay(1000)
                self.screen.blit(self.under_fire_artillery,(x,590))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (x,590))
                pygame.display.flip()
            elif self.myposition == 2:
                x= 350
                pygame.time.delay(1000)
                self.screen.blit(self.under_fire_artillery,(x,590))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (x,590))
                pygame.display.flip()
            elif self.myposition == 4:
                x = 510
                pygame.time.delay(1000)
                self.screen.blit(self.under_fire_artillery,(x,590))
                pygame.display.flip()
                pygame.time.delay(700)
                self.screen.blit(self.artillery , (x,590))
                pygame.display.flip()
            elif self.myposition == 5:
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
                     if self.exit_button.collidepoint(pos):
                                pygame.quit()
                     if self.restart_button.collidepoint(pos):
                                return "restart"
                
            #pygame.time.delay(3000)
        #pygame.quit()

