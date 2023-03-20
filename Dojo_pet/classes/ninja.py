

class Ninja:
    def __init__(self, first_name, _last_name, treats, pet_food, pet) -> None:
        self.first_name = first_name
        self.last_name = _last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

        print(f"Finn have walked {self.pet.name}")
        # print(f"Finn have also walked {self.pet.name}")
        return self

    def feed(self):
        self.pet.eat()
        print(f"{self.treats} has been feed to {self.pet.name}")
        return self

    def bathe(self):
        self.pet.noise()
        return self
