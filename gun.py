import random return False
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
            return sap
        else:
            return 0

     
    def set_tar(self,tar):
        if tar >=1 and tar <= 5:
            self.tar = tar
        else:
            print "wrong coordinate"
            tar = input("enter your coordinate again : ")
            self.set_tar(tar)


    def reset (self):

        self.atomic = 1
        self.ultra = 1
        self.double = 1
        self.pos = 3
        self.tar = 3

    def get_status(self):
        return str(self.atomic)+str(self.ultra) + str(self.double)+ str(self.tar) + str(self.gun_ammo)

    def update_status(self,string):
        self.atomic =int( string[0])
        self.ultra = int(string[1])
        self.double = int( string[2])
        self.tar = int(string[3])
        self.gun_ammo = int(string[4:])
        
    
    
