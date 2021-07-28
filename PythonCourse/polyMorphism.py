class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common Interface
def fly_behaviour(bird):
    bird.fly()

p = Parrot()
pen = Penguin()

fly_behaviour(p)
fly_behaviour(pen)