#last update 24 january 2016    2:00 AM      #
                                             #
#last artilery                               #
                                             #
#this is multi beta version                  #
##############################################
import random
import socket
from cryptography import *
import random
import pygame
from pygame import *

class graphic(object):

    def __init__(self):
        self.pre_loads()                                                               # initializing some graphics parameters to start a new Game

    def pre_loads(self):
        pygame.init()                                                                  # initializing pygame
        self.screen = pygame.display.set_mode((1006, 682),FULLSCREEN)                  # make a pygame_screen
        self.screen.fill((255, 255, 255))                                              # screen_bg(white)
        self.rockets = 100                                                             # primary value of normal rockets
        self.atomic_rockets = 1                                                        # primary value of atomic_rockets
        self.double_rockets = 1                                                        # primary value of double_rockets
        self.ultra_rockets = 1                                                         # primary value of ultra_rockets


        self.bg = pygame.image.load('source\\background.jpg')                               #bg_pic
        self.artillery = pygame.image.load('source\\artillery.png')                         #artillery_pic
        self.screen.blit(self.bg , (0,0))
        self.screen.blit(self.artillery , (430,590))
                                                 #___Task_bar___#
        self.atomic_active= pygame.image.load('source\\atomic_bomb_active.png')
        self.screen.blit(self.atomic_active,(16,105))

        self.double_active= pygame.image.load('source\\double_bomb_active.png')
        self.screen.blit(self.double_active,(16,235))

        self.ultra_active= pygame.image.load('source\\ultra_bomb_active.png')
        self.screen.blit(self.ultra_active,(16,360))

        self.atomic_deactive= pygame.image.load('source\\atomic_bomb_deactive.png')
        self.double_deactive= pygame.image.load('source\\double_bomb_deactive.png')
        self.ultra_deactive= pygame.image.load('source\\ultra_bomb_deactive.png')
                                                 #___Damages_board____#
        self.my_damage=pygame.image.load('source\\7-you.png')
        self.screen.blit(self.my_damage,(825,340))
        self.enemy_damage=pygame.image.load('source\\7-enemy.png')
        self.screen.blit(self.enemy_damage,(925,340))
                                                 #___Target_position_buttons____#
        self.target_pos_up=pygame.image.load('source\\target_pos_up_active.png').convert_alpha()
        self.screen.blit(self.target_pos_up,(930,135))
        pygame.display.flip()
        self.target_pos_up =self.target_pos_up.get_rect()                     #using Rect to make a button in size of loading picture
        self.target_pos_up.move_ip(930,135)                                   # change Rect position

        self.target_pos_down=pygame.image.load('source\\target_pos_down_active.png').convert_alpha()
        self.screen.blit(self.target_pos_down,(860,135))
        pygame.display.flip()
        self.target_pos_down =self.target_pos_down.get_rect()                #using Rect to make a button in size of loading picture
        self.target_pos_down.move_ip(860,135)                                # change Rect position

        self.target_pos_up_de=pygame.image.load('source\\target_pos_up_deactive.png')
        self.target_pos_down_de=pygame.image.load('source\\target_pos_down_deactive.png')

        self.atomic_button = pygame.image.load('source\\atomic_bomb_button.png').convert_alpha()
        self.screen.blit(self.atomic_button,(18,18))
        pygame.display.flip()
        self.atomic_button =self.atomic_button.get_rect()                    #using Rect to make a button in size of loading picture
        self.atomic_button.move_ip(18,18)                                    # change Rect position

        self.double_button = pygame.image.load('source\\double_bomb_button.png').convert_alpha()
        self.screen.blit(self.double_button,(18,145))
        pygame.display.flip()
        self.double_button =self.double_button.get_rect()                   #using Rect to make a button in size of loading picture
        self.double_button.move_ip(18,145)                                  # change Rect position

        self.ultra_button = pygame.image.load('source\\ultra_bomb_button.png').convert_alpha()
        self.screen.blit(self.ultra_button,(18,275))

        self.white=pygame.image.load("source\\white_fill.png")

        self.under_fire_artillery=pygame.image.load("source\\under_fire_artillery.png")

        self.tar_des=pygame.image.load("source\\tar_destroyed.png")

        self.black_bg=pygame.image.load("source\\num_special_rocket.png")
        self.white_bg=pygame.image.load("source\\num_zero.png")
        self.my_status_pic=pygame.image.load("source\\status2.png")
        self.screen.blit(self.my_status_pic,(15,517))
        self.bonus_pic=pygame.image.load("source\\bonus.png")                      #bonus_box
        self.screen.blit(self.bonus_pic,(10,400))
        self.status_box=pygame.image.load("source\\status.png")                    #my_status

        self.atomic_bonus=pygame.image.load("source\\atomic.png")
        self.double_bonus=pygame.image.load("source\\double.png")
        self.ultra_bonus=pygame.image.load("source\\ultra.png")


        self.ground_clean=pygame.image.load("source\\ground_hide.png")

        self.screen.blit(self.status_box,(830,550))

        pygame.display.flip()

        self.fire_flag=False                                                 #this Flag shows if it's your turn to fire the enemy or not
        self.tar_select = 3                                                  # default position displayed in target_position_box
        self.myposition = 3                                                  # your default position in game start

        self.ground_damage=pygame.image.load("source\\ground_damage.png")
        self.white_rockets=pygame.image.load("source\\white_rockets.jpg")

        self.ultra_button =self.ultra_button.get_rect()
        self.ultra_button.move_ip(18,275)

        self.myfont = pygame.font.SysFont("",50)                        #initiallizing a sys Font in size 50
        self.myfont2 = pygame.font.SysFont("",20)                       #initiallizing a sys Font in size 20
        self.myfont3 = pygame.font.SysFont("",30)                       #initiallizing a sys Font in size 30
        pygame.display.flip()
        self.bg_music()                                                    # this methode is used to play a background_music repeatedly !
        self.rockets_show()
        self.num_special_rockets()

        self.data = []                                                     # this data a list that used during the game to know sth about my_pos & enemy_pos & fire_type & .....

        self.code =0                                                       # this variable used in finish methode that specifies the winner of Game !!!!

        self.my_pos = self.myfont.render(str(self.myposition), 3, (0,0,0))    #Dispaly my default_pos
        self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))      #Dispaly enemy default_pos
        self.screen.blit(self.my_pos, (893, 58))
        self.screen.blit(self.tar_text,(892,135))

        self.exit_button=pygame.image.load("source\\exit.png").convert_alpha()        #exit_button
        self.screen.blit(self.exit_button,(20,635))
        pygame.display.flip()
        self.exit_button =self.exit_button.get_rect()
        self.exit_button.move_ip(20,635)

        self.restart_button=pygame.image.load("source\\restart.png").convert_alpha()  #restart_button
        self.screen.blit(self.restart_button,(20,600))
        pygame.display.flip()
        self.restart_button =self.restart_button.get_rect()
        self.restart_button.move_ip(20,600)


        #############_____finish_pictures______#####
        self.win_pic = pygame.image.load("source\\game_won.png")
        self.lose_pic = pygame.image.load("source\\game_lost.png")
        self.no_win_pic = pygame.image.load("source\\no_winner.png")
        self.you_won_pic = pygame.image.load("source\\you_won.png")
        self.you_lost_pic = pygame.image.load("source\\you_lost.png")

        self.end_flag = False                 #this flag shows if the game is finished or not !


    def move_select(self):
        pygame.display.flip()
        normal_flag=True                     # your weapon sets to normal_rockets in every fire turn at first !

        if self.rockets==0:
            normal_flag=False

        atomic_flag=False
        double_flag=False
        ultra_flag=False

        clock = pygame.time.Clock()          # using Clock to make clock_ticks and clock Delays

        x= 430                               # default cordinate of artitillery (x,y) is (430,590)

        if self.myposition == 3:
            x= 430
        elif self.myposition == 1:
            x= 270
        elif self.myposition == 2:
            x= 350
        elif self.myposition == 4:
            x= 510
        elif self.myposition == 5:
            x= 590

        done = False                        # this flag is to finish below loop  when QUIT event happens

        while not done and not self.end_flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

                    if (self.fire_flag==False and event.type==pygame.KEYDOWN and (event.key == pygame.K_f) and self.rockets+self.atomic_rockets+self.double_rockets+self.ultra_rockets>=1) :
                        if normal_flag or atomic_flag or double_flag or ultra_flag :       # this checks if we have any ammiunation to continue the Game or not....
                            self.fire_flag=True
                            self.data = self.fire(self.myposition,x,normal_flag,atomic_flag,double_flag,ultra_flag)
                            print self.myposition
                            done = True

                    if (self.fire_flag==False and event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT)):
                            pressed = pygame.key.get_pressed()                            #key_down events in pygame to change artillery pos
                            if pressed[pygame.K_LEFT] and x >= 350:                       # there is a limitation for x that x can't be less than 350 and more than 535
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

                    if pygame.mouse.get_pressed()[0] :              # pygame mouse_click events
                        pos = pygame.mouse.get_pos()                # the position that mouse clicked
                        '''if self.exit_button.collidepoint(pos):      # click on exit_button
                            return "exit"
                        if self.restart_button.collidepoint(pos):   # click on restart button
                            return "restart"'''
                        if self.atomic_button.collidepoint(pos)and not self.fire_flag and self.atomic_rockets!=0:
                            if not atomic_flag :
                                self.weapon_select_sound()          # click sound plays
                                atomic_flag=True
                                double_flag=False
                                ultra_flag=False
                                normal_flag=False
                                self.screen.blit(self.atomic_deactive,(16,105))    #atomic bomb deactives after click
                                if self.double_rockets!=0:
                                    self.screen.blit(self.double_active,(16,235))
                                if self.ultra_rockets!=0:
                                    self.screen.blit(self.ultra_active,(16,360))
                            elif atomic_flag:
                                 self.weapon_select_sound()
                                 atomic_flag=False
                                 if self.rockets>0:
                                     normal_flag=True
                                 self.screen.blit(self.atomic_active,(16,105))   #atomic bomb reactives after click


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
                                self.screen.blit(self.double_deactive,(16,235))  #double bomb button deactives
                                if self.atomic_rockets!=0:
                                    self.screen.blit(self.atomic_active,(16,105))
                                if self.ultra_rockets!=0:
                                    self.screen.blit(self.ultra_active,(16,360))

                            elif double_flag:
                                 self.weapon_select_sound()
                                 double_flag=False
                                 if self.rockets>0:
                                     normal_flag=True
                                 self.screen.blit(self.double_active,(16,235))   #double bomb reactives after click

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
                                self.screen.blit(self.ultra_deactive,(16,360)) #ultra bomb deactives after click
                                if self.double_rockets!=0:
                                    self.screen.blit(self.double_active,(16,235))
                                if self.atomic_rockets!=0:
                                    self.screen.blit(self.atomic_active,(16,105))
                            elif ultra_flag:
                                 self.weapon_select_sound()
                                 ultra_flag=False
                                 if self.rockets>0:
                                     normal_flag=True
                                 self.screen.blit(self.ultra_active,(16,360)) #atomic bomb reactives after click

                        elif self.target_pos_up.collidepoint(pos) and not self.fire_flag:       # event to change the target position
                            if self.tar_select<4:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select+1
                                self.screen.blit(self.white,(890,135))
                                self.target_pos_up=pygame.image.load('source\\target_pos_up_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_up,(930,135))
                                pygame.display.flip()

                                self.target_pos_up =self.target_pos_up.get_rect()
                                self.target_pos_up.move_ip(930,135)
                                self.target_pos_down=pygame.image.load('source\\target_pos_down_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_down,(860,135))
                                pygame.display.flip()

                                self.target_pos_down =self.target_pos_down.get_rect()
                                self.target_pos_down.move_ip(860,135)
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
                                self.screen.blit(self.tar_text,(894,135))
                                print self.tar_select

                            elif self.tar_select==4:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select+1
                                self.screen.blit(self.white,(890,135))
                                self.screen.blit(self.target_pos_up_de,(930,135))
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
                                self.screen.blit(self.tar_text,(894,135))
                                print self.tar_select

                        elif self.target_pos_down.collidepoint(pos) and not self.fire_flag:
                            if self.tar_select>2:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select-1
                                self.screen.blit(self.white,(890,135))
                                self.target_pos_up=pygame.image.load('source\\target_pos_up_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_up,(930,135))
                                pygame.display.flip()

                                self.target_pos_up =self.target_pos_up.get_rect()
                                self.target_pos_up.move_ip(930,135)
                                self.target_pos_down=pygame.image.load('source\\target_pos_down_active.png').convert_alpha()
                                self.screen.blit(self.target_pos_down,(860,135))
                                pygame.display.flip()

                                self.target_pos_down =self.target_pos_down.get_rect()
                                self.target_pos_down.move_ip(860,135)
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
                                self.screen.blit(self.tar_text,(894,135))
                                print self.tar_select

                            elif self.tar_select==2:
                                self.weapon_select_sound()
                                self.tar_select=self.tar_select-1
                                self.screen.blit(self.white,(890,135))
                                self.screen.blit(self.target_pos_down_de,(860,135))
                                self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
                                self.screen.blit(self.tar_text,(894,135))
                                print self.tar_select

                        self.num_special_rockets()       # Displays the changes of (atomic,double,ultra) bombs if available.....
                        pygame.display.flip()


    def bg_music(self):          #methode to play background_music repeatedly
        pygame.mixer.music.load("source\\background_music.mp3")
        pygame.mixer.music.play(10000)
        pygame.mixer.music.set_volume(0.6)


    def tar_destroy(self):      # the picture that is displayed when the target destroyed !
        self.screen.blit(self.tar_des,(120,230))


    def tar_hit(self , check):
        if check :              # check is a flag that checks if the target has been hitted !
            self.screen.blit(self.status_box,(830,550))
            self.tar_hit_text=self.myfont.render("hit",3,(0,0,0))
            self.screen.blit(self.tar_hit_text,(880,608))         #Displays the "hit" in target_status_box
            pygame.display.flip()

            pygame.time.delay(1500)
            self.screen.blit(self.status_box,(830,550))
            pygame.display.flip()                                 # refresh the target_status_box

        else:
            self.screen.blit(self.status_box,(830,550))
            self.tar_didnt_hit_text=self.myfont.render("no hit",3,(0,0,0))
            self.screen.blit(self.tar_didnt_hit_text,(855,605))   #Displays the "hit" in target_status_box
            pygame.display.flip()

            pygame.time.delay(1500)
            self.screen.blit(self.status_box,(830,550))
            pygame.display.flip()                                # refreshs the target _status_box


    def my_hit(self , check):
       if check:                                                 # this checks if you've hitted after fire
           self.screen.blit(self.my_status_pic,(15,517))
           self.tar_hit_text=self.myfont3.render("hit",3,(0,0,0))# Displays the "hit" in my_staus_box
           self.screen.blit(self.tar_hit_text,(50,558))
           pygame.display.flip()

           pygame.time.delay(1500)
           self.screen.blit(self.my_status_pic,(15,517))
           pygame.display.flip()                                # refreshs the my_status_box

       else:
           self.screen.blit(self.my_status_pic,(15,517))
           self.tar_not_hit_text=self.myfont3.render("no hit",3,(0,0,0))        # Displays "no hit" in my_status_box
           self.screen.blit(self.tar_not_hit_text,(35,558))
           pygame.display.flip()

           pygame.time.delay(1500)
           self.screen.blit(self.my_status_pic,(15,517))
           pygame.display.flip()                                                #refresh my_status_box


    def weapon_select_sound(self):                                              # click sound
        weapon_select=pygame.mixer.Sound("source\\select_weapon.wav")
        weapon_select.play()


    def damage(self,my_damage , enemy_damage):                                  # this methode is to Display my damage and enemy_damage
       my_damage=pygame.image.load("source\\"+str(7-my_damage)+'-you.png')
       enemy_damage=pygame.image.load("source\\"+str(7-enemy_damage)+'-enemy.png')
       self.screen.blit(my_damage,(825,340))
       self.screen.blit(enemy_damage,(925,340))


    def rockets_show(self):                       # Displays the normal_rockets in normal_rockets_box
       self.screen.blit(self.white_rockets,(850,220))
       self.tar_didnt_hit_text=self.myfont.render(str(self.rockets),3,(0,0,0))
       self.screen.blit(self.tar_didnt_hit_text,(880,225))


    def num_special_rockets(self):               # displays the changes of special_rockets_changes
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


    def fire(self ,myposition,x,normal_flag,atomic_flag,double_flag,ultra_flag):         # the graphical changes after F_key event in main loop()
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

        shot=pygame.mixer.Sound("source\\shot.wav")
        shot.play()

        firing_artillery=pygame.image.load("source\\"+str(myposition)+".png")
        pygame.display.flip()

        pygame.time.delay(500)
        self.screen.blit(firing_artillery,(x,590))
        pygame.display.flip()
        pygame.time.delay(500)
        self.screen.blit(self.artillery , (x,590))
        pygame.display.flip()

        pygame.time.delay(500)
        hit=pygame.mixer.Sound("source\\bomb_hit.wav")
        hit.play()
        pygame.time.delay(1200)
        tar_blast=pygame.image.load("source\\tar_ground_hit.png")
        self.screen.blit(tar_blast,(453,318))
        pygame.display.flip()

        pygame.time.delay(1000)
        hide_fire=pygame.image.load("source\\white.png")
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


    def get_posg(self):
        return self.myposition


    def get_targ(self):
        return self.tar_select


    def under_fire(self,position):             # this methode is to Display under_fire after enemy fire
        if position==self.myposition:
            shot=pygame.mixer.Sound("source\\shot.wav")
            shot.play()

            pygame.time.delay(1000)
            hit=pygame.mixer.Sound("source\\bomb_hit.wav")
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
                shot=pygame.mixer.Sound("source\\shot.wav")
                shot.play()

                pygame.time.delay(1000)
                hit=pygame.mixer.Sound("source\\bomb_hit.wav")
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


    def under_double(self,pos):            #the double_shot hits 2 positions ,

        shot=pygame.mixer.Sound("source\\shot.wav")
        shot.play()
        pygame.time.delay(1000)

        hit=pygame.mixer.Sound("source\\bomb_hit.wav")
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

        elif pos==4 or pos==5:
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

    def finish(self , code):                           # when your game finishes this methode is called ,
        # code=1   => you won
        # code=2   => you lost
        # code=2   => no winner
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

        """while True:
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                     pos = pygame.mouse.get_pos()

                     if self.exit_button.collidepoint(pos):       #event of exit
                                return "exit"

                     if self.restart_button.collidepoint(pos):    #event of restart
                                return "restart"  """




    def move(self):
        pygame.display.flip()
        clock = pygame.time.Clock()
        done=False
        x=430
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

                if event.type == pygame.KEYDOWN and (event.key == pygame.K_f):
                    return self.myposition

class gun (object):

    def __init__(self):

        self.atomic = 1
        self.ultra = 1
        self.double = 1
        self.pos = 3
        
    def choice_print(self):
        """ command type list """
        self.temp_options = []
        self.options = []
        if self.get_ammo() >= 1:
            self.options.append("0 : normal fire " + str(self.get_ammo()) + " shot(s)")
            self.temp_options.append(0)
        if self.atomic >= 1:
            self.options.append("1 : atomic fire " + str(self.atomic) + " shot(s)")
            self.temp_options.append(1)
        if self.double >= 1:
            self.options.append("2 : double fire " + str(self.double) + " shot(s)")
            self.temp_options.append(2)
        if self.ultra >= 1:
            self.options.append("3 : ultra fire  " + str(self.ultra) + " shot(s)")
            self.temp_options.append(3)
        return self.temp_options


    def choice(self , command):
        """ choose type of fire """
        if command in self.temp_options:
            self.command = command
            if self.command == 0:
                return self.fire()
            elif self.command == 1:
                return self.atomicshot()
            elif self.command == 2:
                return self.doubleshot()
            elif self.command == 3:
                return self.ultrashot()

    def comm_type(self):
        return self.command
                
    def set_targets(self , num):
        """ taeen tedad sangar ha"""
        self.targets = num

    def set_armor(self , armor):
        """taeen armor"""
        self.gun_armor= armor
        
    def set_ammo(self , ammo):
        """taeen goloole"""
        self.gun_ammo = ammo

    def get_ammo(self):
        """ bargardoondane goloole """
        return self.gun_ammo

    def get_armor(self):
        """ bargardoondane armor """
        return self.gun_armor
        
    def fire(self):
        """ shellik kardan """
        if self.gun_ammo == 0:
            print "no ammo"
            return False
        if self.tar <= self.targets and self.tar >= 1:
            if self.gun_ammo > 0:
                self.gun_ammo -= 1
                return True
        else:
            print "wrong coordinate"
            self.tar = input("enter target again : ")
            self.fire ()
        
    def atomicshot(self):
        if self.atomic == 0:
            print "no atomic bomb"
            return False
        if self.tar <= self.targets and self.tar >= 1:
            if self.atomic > 0:
                self.atomic -= 1
                return True
        else:
            print "wrong coordinate"
            self.tar = input("enter target again : ")
            self.atomicshot()

    def doubleshot (self):   
        if self.double == 0:
            print "no double bomb"
            return False
        if self.tar <= self.targets and self.tar >= 1:
            if self.double >0:
                self.double -= 1
                return True
        else:
            print "wrong coordinate"
            self.tar = input("enter target again : ")
            self.doubleshot()
            
    def ultrashot(self):
        if self.ultra == 0:
            print "no ultra ammo"
            return False
        if self.tar <= self.targets and self.tar >= 1:
            if self.ultra > 0:
                self.ultra -= 1
                return True
        else:
            print "wrong coordinate"
            self.tar = input("enter target again : ")
            self.ultrashot()
            
    def under_atom(self,x):
        if self.gun_armor > 0:
            if self.pos == x:
                self.gun_armor =0
                print "target destroyed"
                return True
            else :
                print "didn't hit"
                return False

    def under_double(self, x):
        """ double hit """
        if self.gun_armor > 0:
            if x == 1:
                if self.pos == 1 or self.pos == 2:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            elif x == 2:
                if self.pos == 3 or self.pos == 2:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            elif x == 3:
                if self.pos == 3 or self.pos == 4:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            elif x == 4:
                if self.pos == 4 or self.pos == 5:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            elif x == 5:
                if self.pos == 5 or self.pos == 4:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            print "didn't hit"
            return False

    def under_ultra(self,x):
         if self.gun_armor > 0:
            if self.pos == x:
                if self.gun_armor > 2:
                    print "target hit"
                    self.gun_armor -= 2
                    return True
                elif self.gun_armor == 2:
                    self.gun_armor -= 2
                    print "target destroyed"
                    return True
                elif self.gun_armor == 1:
                    self.gun_armor -= 1
                    print "target destroyed"
                    return True
            else :
                print "didn't hit"
                return False
            
    def set_pos(self, x):
        """ taeen mogheiyat """
        if x <= self.targets and x >= 1:
            self.pos = x
        else:
            print "wrong pos"
            print("enter coordinate again ")
            x = input("enter your pos")
            self.set_pos(x)

    def get_pos(self):
        return self.pos

    def check_gun_in(self , pos):
        """ taeen in ke aya artilery dar in position hast ya na"""
        if self.pos == pos:
            return True        

    def under_normalfire(self , x):
        """ goloole khordan """
        if self.gun_armor > 0:
            if self.pos == x:
                self.gun_armor -= 1
                if self.gun_armor > 0:
                    print "target hit"
                    return True
                else:
                    print "target destroyed"
                    return True
            else :
                print "didn't hit"
                return False

    def under_attack(self , firetype , x):
        if firetype == 0:
            return self.under_normalfire(x)
        if firetype == 1:
            return self.under_atom(x)
        if firetype == 2:
            return self.under_double(x)
        if firetype == 3:
            return self.under_ultra(x)


    def cehck_spec(self):
        specs = [self.atomic , self.ultra , self.double]
        if specs[0] == 0 and specs[1] == 0 and specs[2] == 0 :
            return False
        else:
            return True


    def give_prize(self,condition):
        if condition == True:
            sap = random.randrange(1,4)
            if sap == 1 :
                self.atomic += 1
            elif sap == 3 :
                self.ultra += 1
            elif sap == 2 :
                self.double += 1       
            print "prize code is : " + `sap`
        else :
            return False


    def set_tar(self, tar):
        """ set target coordinate """
        if tar >= 1 and tar <= 5:
            self.tar = tar
        else:
            print "wrong coordinate"
            tar = input("enter your coordinate again : ")
            self.set_tar(tar)

    def get_status(self):
        return str(self.atomic)+str(self.ultra) + str(self.double)+ str(self.tar) + str(self.gun_ammo)

    def update_status(self,string):
        self.atomic =int( string[0])
        self.ultra = int(string[1])
        self.double = int( string[2])
        self.tar = int(string[3])
        self.gun_ammo = int(string[4:])

def make_prime():
    prime_list=[2]
    for i in range(3,500):
        flag=True
        for j in prime_list:
            if i%j==0 :
                flag=False
                break
            if j>i**0.5 :
                break
        if flag :
            prime_list.append(i)
    return prime_list        
    
##########################################
gun_1 = gun()
gun_2 = gun()
####################
ammo = 100
armor = 7
targets = 5
####################
gun_1.set_targets(targets)
gun_2.set_targets(targets)
gun_1.set_armor(armor)
gun_2.set_armor(armor)
gun_1.set_ammo(ammo)
gun_2.set_ammo(ammo)
####################
game = graphic()
game.rockets = ammo
game.rockets_show()


#defining host or client and connect to host
mysoc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
role = raw_input("do you want to be host or client? ")
key1='#1s[A}!@g'
if role=="host" : #baz kardan port roye host va montazere vasl shodan az taraf client mandan
    ishost=True
    host=socket.gethostname()
    port=12350
    mysoc.bind((host,port))
    mysoc.listen(5)
    client1, addr=mysoc.accept()
    print "got connection from", addr

    prime_list=make_prime() #sakht klid moshtarak
    randprime=prime_list[random.randrange(10,len(prime_list))]
    pubnum=random.randrange(5,5000)
    client1.send(str(randprime)+ '+' + str(pubnum))
    hostnum=random.randrange(2,50)
    first_calc=(pubnum**hostnum)%randprime
    client1.send(str(first_calc))
    cfirst_calc=int(client1.recv(1024))
    key2=((cfirst_calc)**hostnum)%randprime
        
if role == "client" : #vasl shodan be host
    ishost=False
    host = raw_input("host Computername or IP :")
    port=12350
    mysoc.connect((host,port))

    string=mysoc.recv(1024) #sakht klid moshtarak
    i=string.find('+')
    randprime=int(string[:i])
    pubnum=int(string[i+1:])
    clientnum=random.randrange(2,50)
    first_calc=(pubnum**clientnum)%randprime
    mysoc.send(str(first_calc))
    hfirst_calc=int(mysoc.recv(1024))
    key2=((hfirst_calc)**clientnum)%randprime
    my_pos = game.move()
    gun_1.set_pos(my_pos) #taaiin mogheiate avalie client bedone shelik (host chon dar dast aval pas az taiin moghiat shelik mikonad niazi ba taiin moghiate avalie bedon shelik nadarad
    ##GAME MOVE

notfirstround=False
while ((gun_1.get_ammo() > 0 or gun_2.get_ammo() > 0 or gun_1.cehck_spec() or gun_2.cehck_spec()) and gun_1.get_armor() > 0 and gun_2.get_armor() > 0):


    if gun_1.get_ammo() > 0 or gun_1.cehck_spec():
        if ishost :
            if notfirstround :
                
                string = decrypt(client1.recv(1024),key1,key2)
                gun_1.gun_armor =int(string[0]) #####daryaft armor gune ma az harif . chon dast aval harif client shelik nakarde baraye hamin az daste dovom in khat ra ejra mikonim

                gun_2.update_status(string[1:]) ######daryaft ammo va target gune harif (daste aval chon hanoz harif shlik nakarde in khat ra az dast dovom ejra mikonim)
                game.under_fire(gun_2.tar)
                game.damage(7 - gun_1.get_armor(), 7 - gun_2.get_armor())

                if gun_1.get_armor() == 0:   #end
                    print "****you lose you destroyed****"
                    game.end_flag = True
                    game.finish(2)
                print "enemy target was : " + `gun_2.tar`
                print "your armor is : " + `gun_1.get_armor()`
                print "your ammo is : " + `gun_1.get_ammo()`
                print "enemy armor is : " + `gun_2.get_armor()`
                print "enemy ammo is : " + `gun_2.get_ammo()`
                print "<><><><><><><><><><><><><><><><><>"


            game.move_select()
            gun_1.set_pos(game.data[0]) ######MOVE SEL
            gun_1.set_tar(game.data[1])
            gun_1.choice_print()
            gun_1.choice(game.data[2])
            my_comm = gun_1.comm_type()
            client1.send(str(gun_1.pos)) #ferestadan mogheiate gune ma be harif
            gun_2.pos = int(client1.recv(1)) #daryaft mogheiate gune harif
            my_check = gun_2.under_attack(my_comm,gun_1.tar)
            prize = gun_1.give_prize(my_check)
            game.bonus(prize)


            print "enemy coor pos was : " + `gun_2.get_pos()`
            print "your armor is : " + `gun_1.get_armor()`
            print "your ammo is : " + `gun_1.get_ammo()`
            print "enemy armor is : " + `gun_2.get_armor()`
            print "enemy ammo is : " + `gun_2.get_ammo()`
            print "<><><><><><><><><><><><><><><><><>"

            client1.send(encrypt(str(gun_2.gun_armor)+gun_1.get_status(),key1,key2)) #ferestadan armore gune harif (pas az daryaft moghiat dar khat haye bala gun_2 ra under attack gozashtim va armor an ra taiin kardim hal armorash ra be harif mifrestim) va ferestadane target va ammoye gune ma be harif
            notfirstround=True


            if gun_2.get_armor() == 0:  #gui
                 print "****you won enemy destroyed****"
                 game.end_flag = True
                 game.finish(1)
                 break


        else:



            mysoc.send(str(gun_1.pos)) #ferestadan mogheiate gune ma (daste aval moghiat kharej while taiin shode (dar bala ghesmate if role='client'))
          ######################## to do  gun_2.pos = int(mysoc.recv(1)) #daryaft moghiate gune harif
            string=decrypt(mysoc.recv(1024),key1,key2) 
            gun_1.gun_armor =int(string[0]) #daryaft armore gun ma
            gun_2.update_status(string[1:]) #daryaft target va ammoye gun harif
            ##GAME UNDRFIRE
            if gun_1.gun_armor == 0:
                print "****you lose you destroyed****"
                break
            print "enemy target was : " + `gun_2.tar`
            print "your armor is : " + `gun_1.get_armor()`
            print "your ammo is : " + `gun_1.get_ammo()`
            print "enemy armor is : " + `gun_2.get_armor()`
            print "enemy ammo is : " + `gun_2.get_ammo()`
            print "<><><><><><><><><><><><><><><><><>"
            gun_1.set_pos()

            c1 = gun_1.choice_print()
            c2 = input("enter command sir : ")
            c3 = gun_1.choice(c2)
            c4 = gun_1.comm_type()
            c5 = gun_2.under_attack(c4,gun_1.tar)
            gun_1.give_prize(c5)

            print "enemy coor pos was : " + `gun_2.get_pos()`
            print "your armor is : " + `gun_1.get_armor()`
            print "your ammo is : " + `gun_1.get_ammo()`
            print "enemy armor is : " + `gun_2.get_armor()`
            print "enemy ammo is : " + `gun_2.get_ammo()`
            print "<><><><><><><><><><><><><><><><><>"

            mysoc.send(encrypt(str(gun_2.gun_armor)+ gun_1.get_status(),key1,key2) ) #ferestadane target va ammoye gune ma va armore gune harif be harif

           if gun_2.get_armor() == 0:  #gui
                 print "****you won enemy destroyed****"
                 game.end_flag = True
                 game.finish(1)
                 break

                
           
            

    if gun_2.get_ammo() > 0 or gun_2.cehck_spec():
        
        if gun_1.get_armor() == 0:
            print "****you lose you destroyed****"
            break        


    if gun_1.get_ammo() == 0 and gun_2.get_ammo() == 0 and gun_1.cehck_spec()== False  and gun_2.cehck_spec()== False:
        if gun_1.get_armor() == gun_2.get_armor():
                print "no ammuniation no winner"
                game.end_flag = True
                game.finish(3)
                break


        elif gun_1.get_armor() > gun_2.get_armor():
                print "you won"
                game.end_flag = True
                break
        else:
            print "you lost"
                game.end_flag = True
                choose5 = game.finish(5)
                break


print "game ended"
mysoc.close()
raw_input("press<enter>")


############################################################
# bug ha ra inja benevisid :


