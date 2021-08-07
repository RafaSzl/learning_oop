class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("great ratio")
        if self.ratio == 1:
            print("hard to fly, but fly")
        if self.ratio < 1:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8) # we created new Wing class object and assigned it to _wing attribute of Duck class

    def walk(self):
        print("tap tap tap")

    def swim(self):
        print("duck is swimming")

    def quack(self):
        print("Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("i can tap tap too")

    def swim(self):
        print("swim almost like a duck")

    def quack(self):
        print("Quack, but in penguinish")



# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()
    # test_duck(percy)

