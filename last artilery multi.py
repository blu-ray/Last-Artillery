#last update 16-1-2016     7:00 pm           #
                                             #
#last artilery                               #
                                             #
#this is final single                        #
##############################################
import random

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
        print "\nchoose command : \n" 
        for command in self.options :
            print command
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
        else:
            print "wrong command"
            command = input("enter command again : ")
            self.choice(command)

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
            
    def set_pos(self):
        """ taeen mogheiyat """
        x = input("<><><><><><><><><><><><><><><><>\nenter your coordinate : ")
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
gun_1.set_pos()
gun_2.set_pos()
gun_1.set_ammo(ammo)
gun_2.set_ammo(ammo)
####################
while ((gun_1.get_ammo() > 0 or gun_2.get_ammo() > 0 or gun_1.cehck_spec() or gun_2.cehck_spec()) and gun_1.get_armor() > 0 and gun_2.get_armor() > 0):


    if gun_1.get_ammo() > 0 or gun_1.cehck_spec():
        gun_1.set_pos()
        tar_1 = input("enter target coordinate : ")
        gun_1.set_tar(tar_1)
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
        if gun_2.get_armor() == 0:
            print "****you won enemy destroyed****"
            break
    

    if gun_2.get_ammo() > 0 or gun_2.cehck_spec():
        gun_2.set_pos()
        tar_2 = input("enter target coordinate : ")
        gun_2.set_tar(tar_2)
        c6 = gun_2.choice_print()
        c7 = input("enter command sir : ")
        c8 = gun_2.choice(c7)
        c9 = gun_2.comm_type()
        print "enemy command code was : " + `c9`
        c10 = gun_1.under_attack(c9,gun_2.tar)
        gun_2.give_prize(c10)
        print "enemy coor target is : " + `gun_2.tar` 
        print "your armor is : " + `gun_1.get_armor()`
        print "your ammo is : " + `gun_1.get_ammo()`
        print "enemy armor is : " + `gun_2.get_armor()`
        print "enemy ammo is : " + `gun_2.get_ammo()`
        if gun_1.get_armor() == 0:
            print "****you lose you destroyed****"
            break        


    if gun_1.get_ammo() == 0 and gun_2.get_ammo() == 0 and gun_1.cehck_spec()== False  and gun_2.cehck_spec()== False:
        print "no ammuniation no winner"
        break


print "game ended"
raw_input("press<enter>")


############################################################
# bug ha ra inja benevisid :



