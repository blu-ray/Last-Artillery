import gun
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



