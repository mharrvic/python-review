# OOP


class PlayerCharacter:
    # Class Object Attributes
    membership = True

    def __init__(self, name, age):
        if self.membership:
            # set underscore as private (for convention)
            self._name = name  # attributes
            self._age = age

    def shout(self):
        print(f"my name is {self._name}")

    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")

    @classmethod
    # to access the class state
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    # we will only use this, we don't want care about the class state
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tim", 12)
player3 = PlayerCharacter.adding_things(2, 3)
player2.attack = 50


print(player1.membership)
print(player2.attack)
print(player1.shout())
print(player3._name)
print(player2.speak())