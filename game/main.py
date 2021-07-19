from player import Player
from enemy import Enemy, Troll

tim = Player("Tim")
print(tim.name)
print(tim.lives)

tim.lives -= 1
tim.level += 1
print(tim)

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(14)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll("Pug")
print("ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print("brother - {}".format(another_troll))

ugly_troll.grunt()

# # it is called getter, it gets a value from a data attribute (here data is a class Player)
# print(tim.get_name())
#
# # it is called setter, it sets a value for a data attribute (here data is a class Player)
# tim.set_lives(300)