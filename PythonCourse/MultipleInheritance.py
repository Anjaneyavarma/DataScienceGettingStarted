class A:
    def fun(self):
        print("Class A")
class B(A):
    def fun(self):
        print("Class B")
        # super().fun()
class C(A):
    def fun(self):
        print("Class C")
        # super().fun()
class D(B, C):
    pass

d = D()
d.fun()
print(D.mro())


class Family:
    def show_family(self):
        print("This is our family:")


# Father class inherited from Family
class Father(Family):
    fathername = ""

    def show_father(self):
        print(self.fathername)


# Mother class inherited from Family
class Mother(Family):
    mothername = ""

    def show_mother(self):
        print(self.mothername)


# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


s1 = Son()  # Object of Son class
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_family()
s1.show_parent()