# Parent Class
class User:
    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


# Children Class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left-{self.num_arrows}")


# Multiple Inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
hb1 = HybridBorg("borgie", 80, 100)
# wizard1.attack()
# archer1.attack()
hb1.attack()

# print(isinstance(wizard1, object))