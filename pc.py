import gun
from gun import *
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



