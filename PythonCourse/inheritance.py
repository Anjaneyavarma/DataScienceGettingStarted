class Bird:

    def __init__(self):
        print("Bird is ready")

    def WhoIsThis(self):
        print("I am Bird")

    def Run(self):
        print("run faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def WhoIsThis(self):
        super().WhoIsThis()
        print("I'm Penguin")

    def Swim(self):
        print("Swim faster")

penguin = Penguin()
penguin.WhoIsThis()
penguin.Swim()
penguin.Run()
