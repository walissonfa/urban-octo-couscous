import random
import time


class Hunter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, witch, critical_strike):
        base_damage = random.randint(1, 10) * self.level
        hunter_damage = base_damage * 2 if critical_strike else base_damage
        witch_damage = witch.witchcraft_attack()

        if critical_strike:
            print("Your critical strike {} !!".format(hunter_damage))
        else:
            print("You attacked {}".format(hunter_damage))

        print('Witch attacked {}'.format(witch_damage))

        if hunter_damage > witch_damage:
            print("You defeated {}".format(witch.name))
            return True
        else:
            print("{} ran away!".format(witch.name))
            return False
         
    
class Witch:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '{} (lv{})'.format(self.name, self.level)
    
    def witchcraft_attack(self):
        return random.randint(1, 10) * self.level


class FireWitch(Witch):
    def __init__(self, name, level, fire_staff):
        super().__init__(name, level)
        self.fire_staff = fire_staff

    def witchcraft_attack(self):
        base_attack = super().witchcraft_attack()
        if self.fire_staff:
            print('Witchcraft is filling with fire!!!')
            return base_attack * 2
        else:
            return base_attack


class EvilWitch(Witch):
    def __init__(self, name, level, black_staff_level):
        super().__init__(name, level)
        self.black_staff_level = black_staff_level

    def witchcraft_attack(self):
        base_attack = super().witchcraft_attack()
        print('Witchcraft with black staff level {}!!'.format(self.black_staff_level))
        return base_attack * 2 * self.black_staff_level


def start_game():
    
    hunter = Hunter('Hunter', 1)

    while True:
        witches = [Witch('Witch', random.randint(1, 5)),
                   FireWitch('Fire witch', random.randint(6, 20), random.choice([True, False])),
                   EvilWitch('Evil witch', random.randint(21, 30), random.randint(1, 5))]
        witch = random.choice(witches)
        print()
        print('{} has appear!'.format(witch))
        print()
        cmd = input("Do you [a]ttack, or [s]top tracing? ")
        if cmd == 'a':
            if hunter.attack(witch, random.choice([True, False])):
                hunter.level += 1
                print("Level up! {} level now".format(hunter.level))
            else:
                print("Hunter is taking time to recover")
                #time.sleep(1)
        else:
            print("Hunter stop tracing")
                
            
start_game()
