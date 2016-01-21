import random
import pygame


class gun (object):

    def __init__(self):

        self.atomic = 1
        self.ultra = 1
        self.double = 1
        self.pos = 3
        
    def choice_print(self):
        """ command type """
        self.temp_options = []
        self.options = []
        if self.get_ammo() >= 1:
            self.options.append("0 : normal fire " + `self.get_ammo()` + " shot(s)" )
            self.temp_options.append(0)
        if self.atomic >= 1:
            self.options.append("1 : atomic fire " + `self.atomic` + " shot(s)" )
            self.temp_options.append(1)
        if self.double >= 1:
            self.options.append("2 : double fire " + `self.double` + " shot(s)" )
            self.temp_options.append(2)
        if self.ultra >= 1:
            self.options.append("3 : ultra fire  " + `self.ultra` + " shot(s)" )
            self.temp_options.append(3)
        return self.temp_options


    def choice(self , command):
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
        #else:
         #   print "wrong command"
         #   command = input("enter command again : ")
         #   self.choice(command)

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

    def under_double(self,x):
        if self.gun_armor > 0:
            if self.pos > 0  and self.pos < self.targets  :
                if self.pos == x or self.pos == x+1:
                    self.gun_armor -= 1
                    if self.gun_armor > 0:
                        print "target hit"
                        return True
                    else:
                        print "target destroyed"
                        return True
            if self.pos == self.targets:
                if self.pos == x or self.pos == x-1:
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
            
    def set_pos(self , x):
        """ taeen mogheiyat """
        if x <= self.targets and x >= 1:
            self.pos = x
        else:
            print "wrong pos"
            print("enter coordinate again ")
            self.set_pos()

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

     
    def set_tar(self,tar):
        if tar >=1 and tar <= 5:
            self.tar = tar
        else:
            print "wrong coordinate"
            tar = input("enter your coordinate again : ")
            self.set_tar(tar)

        
##########################################
class pc(gun):

    def choice_print(self):
        """ command type """
        self.temp_options = []
        self.options = []
        if self.get_ammo() >= 1:
            self.options.append("0 : normal fire ")
            self.temp_options.append(0)
        if self.atomic >= 1:
            self.options.append("1 : atomic fire " )
            for i in range (self.atomic):
                self.temp_options.append(1)
                if self.get_ammo() >= 1:
                    self.temp_options.append(0)
        if self.double >= 1:
            self.options.append("2 : double fire " )
            for j in range (self.double):
                self.temp_options.append(2)
                if self.get_ammo() >= 1:
                    self.temp_options.append(0)
        if self.ultra >= 1:
            self.options.append("3 : ultra fire " )
            for k in range (self.ultra):
                self.temp_options.append(3)
                if self.get_ammo() >= 1:
                    self.temp_options.append(0)
        i,j,k = 0,0,0
        return self.temp_options


    def choice(self):
        command = random.randrange(0,len(self.temp_options))
        self.command = self.temp_options[command]
        if self.command == 0:
            self.tar = random.randrange(1,6)
            return self.fire()
        elif self.command == 1:
            self.tar = random.randrange(1,6)
            return self.atomicshot()
        elif self.command == 2:
            self.tar = random.randrange(1,6)
            return self.doubleshot()
        elif self.command == 3:
            self.tar = random.randrange(1,6)
            return self.ultrashot()
    

    def fire(self):
        """ shellik kardan """
        self.tar = random.randrange(1,6)
        if self.gun_ammo == 0:
            print "no ammo"
            return False
        elif self.gun_ammo > 0:
            self.gun_ammo -= 1
            return True

    def atomicshot(self):
        self.tar = random.randrange(1,6)
        if self.atomic == 0:
            print "no atomic bomb"
            return False
        if self.atomic > 0:
            self.atomic -= 1
            return True
        
    def doubleshot (self):
        self.tar = random.randrange(1,6)
        if self.double == 0:
            print "no double bomb"
            return False
        if self.double > 0:
            self.double -= 1
            return True

    def ultrashot(self):
        self.tar = random.randrange(1,6)
        if self.ultra == 0:
            print "no ultra ammo"
            return False
        if self.ultra > 0:
            self.ultra -= 1
            return True

    def set_pos(self):
        self.pos = random.randrange(1,6)




##########################################
class graphic(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1006, 682))
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

        self.my_damage=pygame.image.load('Damage/7-you.png')#
        self.screen.blit(self.my_damage,(825,340))
        self.enemy_damage=pygame.image.load('Damage/7-enemy.png')#
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
        self.screen.blit(self.game_icon,(17,595))       
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
        graphic.bg_music(self)
        graphic.rockets_show(self)
        graphic.num_special_rockets(self)
        
        #graphic.move_select(self)
        self.data = []
        #graphic.bonus(self,2)

        self.code =0##
        self.my_pos = self.myfont.render(str(self.myposition), 3, (0,0,0))
        self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
        self.screen.blit(self.my_pos, (893, 58))
        self.screen.blit(self.tar_text,(892,135))
    """def start:
         self.myMovie = pygame.movie.Movie(self.fullfilename)   #Load video file
         self.resolution = self.myMovie.get_size()              #Get it's dimensions
         self.movie_length = self.myMovie.get_length()          #Get it's play length
  
         self.image_surface = pygame.Surface(self.resolution)   #Create surface for the video
         self.image_surface.fill([0,0,0])                       #Fill surface black
  
         self.myMovie.set_display(self.image_surface)           #Assign video stream to the surface
         self.myMovie.play()                                    #Start video stream 
         self.start_time = time.time()                          #Get time the stream was started
  """
    #def victory:
    def move_select(self):

        pygame.display.flip()
        normal_flag=True
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
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if (self.fire_flag==False and event.type==pygame.KEYDOWN and (event.key == pygame.K_f)) :
                    self.fire_flag=True
                    self.data = graphic.fire(self,self.myposition,x,normal_flag,atomic_flag,double_flag,ultra_flag)
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
                    if self.atomic_button.collidepoint(pos)and not self.fire_flag and self.atomic_rockets!=0:
                        if not atomic_flag :
                            graphic.weapon_select_sound(self)
                            atomic_flag=True
                            double_flag=False
                            ultra_flag=False
                            normal_flag=False
                           
                            self.screen.blit(self.atomic_deactive,(16,105))
                            
                        elif atomic_flag:
                             graphic.weapon_select_sound(self)
                             atomic_flag=False
                             normal_flag=True
                           
                             self.screen.blit(self.atomic_active,(16,105))
                            
                             
                        print "__________atomic_bomb_________"
               #######################################
                    elif self.double_button.collidepoint(pos) and not self.fire_flag and self.double_rockets!=0:
                        graphic.weapon_select_sound(self)
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
                             graphic.weapon_select_sound(self)
                             double_flag=False
                             normal_flag=True
                             
                             
                             self.screen.blit(self.double_active,(16,235))
                             
                            
                        
                        print "__________double_bomb_________"
                   ############################################
                    elif self.ultra_button.collidepoint(pos) and not self.fire_flag and self.ultra_rockets!=0:
                        graphic.weapon_select_sound(self)
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
                             graphic.weapon_select_sound(self)
                             ultra_flag=False
                             normal_flag=True
                            
                            
                             self.screen.blit(self.ultra_active,(16,360))
                          
                        
                            
                        print "__________ultra_bomb_________"
                    
                    elif self.target_pos_up.collidepoint(pos) and not self.fire_flag:
                        if self.tar_select<4:
                            graphic.weapon_select_sound(self)
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
                            graphic.weapon_select_sound(self)
                            self.tar_select=self.tar_select+1
                        ############    
                            self.screen.blit(self.white,(890,135))
                            self.screen.blit(self.target_pos_up_de,(930,135))
                            self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                            self.screen.blit(self.tar_text,(894,135))###
                            print self.tar_select
                        
                    
                    elif self.target_pos_down.collidepoint(pos) and not self.fire_flag:
                        if self.tar_select>2:
                            graphic.weapon_select_sound(self)
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
                            #self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))
                            #self.screen.blit(self.tar_text,(894,135))###
                            print self.tar_select
                        elif self.tar_select==2:
                            graphic.weapon_select_sound(self)
                            self.tar_select=self.tar_select-1
                            self.screen.blit(self.white,(890,135))
                            self.screen.blit(self.target_pos_down_de,(860,135))
                            self.tar_text=self.myfont.render(str(self.tar_select),3,(0,0,0))###
                            self.screen.blit(self.tar_text,(894,135))###
                            print self.tar_select                    
                    graphic.num_special_rockets(self)
                    pygame.display.flip()
        i,j=0,0    
        
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

    #def finish(self):#####################################################################

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
        elif atomic_flag:
            self.atomic_rockets-=1
            if self.atomic_rockets!=0:
                self.screen.blit(self.atomic_active,(16,105))
            
        elif double_flag:
            self.double_rockets-=1
            if self.double_rockets!=0:
                self.screen.blit(self.double_active,(16,235))
        elif ultra_flag:
            self.ultra_rockets-=1
            if self.ultra_rockets!=0:
                self.screen.blit(self.ultra_active,(16,360))
            
        graphic.num_special_rockets(self)
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
            pygame.display.flip()
            pygame.time.delay(2000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            self.atomic_rockets+=1
            
        elif bonus_code==2:
            self.screen.blit(self.double_bonus,(10,400))
            pygame.display.flip()
            pygame.time.delay(2000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            self.double_rockets+=1
           
        elif bonus_code==3:
            self.screen.blit(self.ultra_bonus,(10,400))
            pygame.display.flip()
            pygame.time.delay(2000)
            self.screen.blit(self.bonus_pic,(10,400))
            pygame.display.flip()
            self.ultra_rockets+=1 
        graphic.num_special_rockets(self)
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
###############################################################
##########################################
gun_1 = gun()
gun_2 = pc()
####################
ammo = 100
armor = 7
targets = 5
####################
gun_1.set_targets(targets)
gun_2.set_targets(targets)
gun_1.set_armor(armor)
gun_2.set_armor(armor)
gun_2.set_pos()
gun_1.set_ammo(ammo)
gun_2.set_ammo(ammo)
####################
game = graphic()

while ((gun_1.get_ammo() > 0 or gun_2.get_ammo() > 0 or gun_1.cehck_spec() or gun_2.cehck_spec()) and gun_1.get_armor() > 0 and gun_2.get_armor() > 0):

    game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
    if gun_1.get_ammo() > 0 or gun_1.cehck_spec():
        game.move_select()
        game.rockets_show()
        game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
        gun_1.set_pos(game.data[0])
        gun_1.set_tar(game.data[1])
        gun_1.choice_print()
        gun_1.choice(game.data[2])
        my_comm = gun_1.comm_type()
        my_check = gun_2.under_attack(my_comm,gun_1.tar)
        game.tar_hit(my_check)
        gun_1.give_prize(my_check)
        game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )

        print "your command was : " + `my_comm`
        print "enemy coor pos was : " + `gun_2.get_pos()`
        print "your armor is : " + `gun_1.get_armor()`
        print "your ammo is : " + `gun_1.get_ammo()`
        print "enemy armor is : " + `gun_2.get_armor()`
        print "enemy ammo is : " + `gun_2.get_ammo()`
        print "<><><><><><><><><><><><><><><><><><>\n"



    if gun_2.get_armor() == 0:
        ###finish
         print "****you won enemy destroyed****"
         break

    if gun_2.get_ammo() > 0 or gun_2.cehck_spec():
        c6 = gun_2.set_pos()
        c7 = gun_2.choice_print()
        c8 = gun_2.choice()

        c9 = gun_2.comm_type()

        game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
        print "enemy command code was : " + `c9`
        c10 = gun_1.under_attack(c9,gun_2.tar)
        game.under_fire(gun_2.tar)
        game.my_hit(c10)
        gun_2.give_prize(c10)
        game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
        print "enemy coor target is : " + `gun_2.tar`
        print "your armor is : " + `gun_1.get_armor()`
        print "your ammo is : " + `gun_1.get_ammo()`
        print "enemy armor is : " + `gun_2.get_armor()`
        print "enemy ammo is : " + `gun_2.get_ammo()`
        print "<><><><<><><><><><><><><><><><><>"


    if gun_1.get_armor() == 0:
        ###finish
        print "****you lose you destroyed****"
        break


    if gun_1.get_ammo() == 0 and gun_2.get_ammo() == 0 and gun_1.cehck_spec()== False  and gun_2.cehck_spec()== False:
        ###finish
        print "no ammuniation no winner"
        break

    game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
    game.fire_flag = False
game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
print "game ended"
raw_input("press<enter>")

