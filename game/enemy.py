import random


class Enemy(object):
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True  # add new attribute

    def take_damage(self, damage):
        remaining_point = self._hit_points - damage
        if remaining_point >= 0:
            self._hit_points = remaining_point
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    # pass  # does nothing but due to pass we do not have syntax error
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)  # python 2 way of putting superclass into subclass
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)  # the proper way to use superclass
        super().__init__(name=name, lives=1, hit_points=23)  # the final version of using superclass, suggested to use

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampyre(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodging(self):
        if random.randint(1, 3) == 3:
            print(" ****** {0._name} dodges ***".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodging():
            super().take_damage(damage=damage)


class Vampyreking(Vampyre):

    def __init__(self, name):
        super().__init__(name=name)

    def take_damage(self, damage):
        if not self.dodging():
            super().take_damage(damage=(damage//4)) # jeden slash nie zaokragla w dol, dwa zaokraglaja





