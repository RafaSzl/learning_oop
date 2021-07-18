from player import Player

tim = Player("Tim")
print(tim.name)
print(tim.lives)

tim.lives -= 1
tim.level += 1
print(tim)

tim.lives -= 1
tim.level += 1
print(tim)

tim.lives -= 1
tim.level += 7
print(tim)

tim.lives += 1
print(tim)

tim.score = 500
print(tim)



# # it is called getter, it gets a value from a data attribute (here data is a class Player)
# print(tim.get_name())
#
# # it is called setter, it sets a value for a data attribute (here data is a class Player)
# tim.set_lives(300)