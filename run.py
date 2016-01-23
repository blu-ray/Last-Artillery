from pc import *
from graphic import *
##########################################

##########################################


########################
        
            
def run():
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
    game.rockets=ammo
    game.rockets_show()
    while ((gun_1.get_ammo() > 0 or gun_2.get_ammo() > 0 or gun_1.cehck_spec() or gun_2.cehck_spec()) and gun_1.get_armor() > 0 and gun_2.get_armor() > 0):

        if gun_1.get_ammo() > 0 or gun_1.cehck_spec():
            condition = game.move_select()


            if condition == "exit":
                pygame.quit()
                break



            elif condition == "restart":

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
                gun_1.reset()
                gun_2.reset()
                gun_2.set_pos()
                ####################
                game.pre_loads()
                game.rockets=ammo
                game.rockets_show()
                continue


            else:
                game.rockets_show()
                gun_1.set_pos(game.data[0])
                gun_1.set_tar(game.data[1])
                gun_1.choice_print()
                gun_1.choice(game.data[2])
                my_comm = gun_1.comm_type()
                my_check = gun_2.under_attack(my_comm,gun_1.tar)
                game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
                game.tar_hit(my_check)
                prize = gun_1.give_prize(my_check)
                game.bonus(prize)


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
                 game.end_flag = True
                 choose1 = game.finish(1)
                 if choose1 == "restart":
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
                    gun_1.reset()
                    gun_2.reset()
                    gun_2.set_pos()
                    ####################
                    game.pre_loads()
                    game.rockets=ammo
                    game.rockets_show()
                    game.end_flag = False
                    continue
                 else:
                        pygame.quit()
                        break




            if gun_2.get_ammo() > 0 or gun_2.cehck_spec():
                c6 = gun_2.set_pos()
                c7 = gun_2.choice_print()
                c8 = gun_2.choice()
                c9 = gun_2.comm_type()

                print "enemy command code was : " + `c9`
                c10 = gun_1.under_attack(c9,gun_2.tar)
                game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
                if c9==2:
                    game.under_double(gun_2.tar)
                else:
                    game.under_fire(gun_2.tar)########
                game.my_hit(c10)
                gun_2.give_prize(c10)
                print "enemy coor target is : " + `gun_2.tar`
                print "your armor is : " + `gun_1.get_armor()`
                print "your ammo is : " + `gun_1.get_ammo()`
                print "enemy armor is : " + `gun_2.get_armor()`
                print "enemy ammo is : " + `gun_2.get_ammo()`
                print "<><><><<><><><><><><><><><><><><>"

            if gun_1.get_armor() == 0:
                ###finish
                print "****you lose you destroyed****"
                game.end_flag = True
                choose2 = game.finish(2)
                if choose2 == "restart":
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
                    gun_1.reset()
                    gun_2.reset()
                    gun_2.set_pos()
                    ####################
                    game.pre_loads()
                    game.rockets=ammo
                    game.rockets_show()
                    game.end_flag = False
                    continue
                else:
                        pygame.quit()
                        break




            if gun_1.get_ammo() == 0 and gun_2.get_ammo() == 0 and gun_1.cehck_spec()== False  and gun_2.cehck_spec()== False:
                ###finish


                if gun_1.get_armor() == gun_2.get_armor():
                    print "no ammuniation no winner"
                    game.end_flag = True
                    choose3 = game.finish(3)
                    if choose3 == "restart":
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
                        gun_1.reset()
                        gun_2.reset()
                        gun_2.set_pos()
                        ####################
                        game.pre_loads()
                        game.rockets=ammo
                        game.rockets_show()
                        game.end_flag = False
                        continue
                    else:
                        pygame.quit()
                        break



                elif gun_1.get_armor() > gun_2.get_armor():
                    print "you won"
                    game.end_flag = True
                    choose4 = game.finish(4)
                    if choose4 == "restart":
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
                        gun_1.reset()
                        gun_2.reset()
                        gun_2.set_pos()
                        ####################
                        game.pre_loads()
                        game.rockets=ammo
                        game.rockets_show()
                        game.end_flag = False
                        continue
                    else:
                        pygame.quit()
                        break




                else:
                    print "you lost"
                    game.end_flag = True
                    choose5 = game.finish(5)
                    if choose5 == "restart":
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
                        gun_1.reset()
                        gun_2.reset()
                        gun_2.set_pos()
                        ####################
                        game.pre_loads()
                        game.rockets=ammo
                        game.rockets_show()
                        game.end_flag = False
                        continue
                    else:
                        pygame.quit()
                        break

            game.damage(7 - gun_1.get_armor() , 7 - gun_2.get_armor() )
            game.fire_flag = False
            



    print "game ended"
    raw_input("press<enter>")
