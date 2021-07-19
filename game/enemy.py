class Enemy(object):
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        if remaining_point >= 0:
            self.hit_points = remaining_point
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):
    # pass  # does nothing but due to pass we do not have syntax error
    def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)  # python 2 way of putting superclass into subclass
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)  # the proper way to use superclass
        super().__init__(name=name, lives=1, hit_points=23)  # the final version of using superclass, suggested to use

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))
