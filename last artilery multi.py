#last update 24 january 2016    2:00 AM      #
                                             #
#last artilery                              
            print "wrong coordinate"
            self.tar = input("enter target again : ")
            self.atomicshot()

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
        return str(self.atomic)+str(self.ultra) + str(self.double)+ str(self.tar)+ str(self.command) + str(self.gun_ammo)

    def update_status(self,string):
        self.atomic =int( string[0])
        self.ultra = int(string[1])
        self.double = int( string[2])
        self.tar = int(string[3])
        self.command = int(string[4])
        self.gun_ammo = int(string[5:])

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


