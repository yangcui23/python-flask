

class Pet:
    def __init__(self, name, type, tricks, health, energy) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy has been increased to {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy has been increase to {self.energy}")
        print(f"{self.name}'s health has been increase to {self.health}")
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        print(f"{self.name}'s health has been increase to {self.health}")
        print(f"{self.name}'s energy has been decrease to {self.energy}")

        return self

    def noise(self):
        print(f"{self.name} has been spoken!!!!")
        return self


class Pug(Pet):
    def __init__(self, name, type, tricks, health, energy) -> None:
        super().__init__(name, type, tricks, health, energy)

    def sleep(self):
        self.energy += 5
        print(f"{self.name}'s energy has been increased to {self.energy}")
        return self

    def eat(self):
        self.energy += 10
        self.health += 20
        print(f"{self.name}'s energy has been increase to {self.energy}")
        print(f"{self.name}'s health has been increase to {self.health}")
        return self

    def play(self):
        self.health += 10
        self.energy -= 20
        print(f"{self.name}'s health has been increase to {self.health}")
        print(f"{self.name}'s energy has been decrease to {self.energy}")

        return self

    def noise(self):
        print(f"{self.name} has been spoken!!!!")
        return self
