class Polygon:

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("enter side "+ str(i+1)+ " :")) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print("sides",str(i+1),":", self.sides[i])

class Traingle(Polygon):

    def __init__(self):
        Polygon.__init__(self, 3)

    def parameter(self):
        a,b,c = self.sides
        s = (a+b+c)/2
        print("parameter: ", s)


t = Traingle()

t.inputSides()

t.displaySides()

t.parameter()