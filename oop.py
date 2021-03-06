class Kettle(object):

    power_source = "electricity"

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.name)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.name, kenwood.price, hamilton.name, hamilton.price))

print("Models: {0.name} = {0.price}, {1.name} = {1.price}".format(kenwood, hamilton))

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

# class can be dynamic modified by doing something like this below:
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switching to atomic power")
Kettle.power_source = "atomic"

print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"

print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("******")
print(globals())
