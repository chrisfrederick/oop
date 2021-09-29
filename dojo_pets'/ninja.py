
from pet import Pet
class Ninja():
    def __init__(self, name, last_name, treat = "Dog treat", pet_food = "Dog Food"):
        self.name = name
        self.last_name = last_name
        self.pet = Pet("Cleo", "Dog", "Flips")
        self.treat = treat
        self.pet_food = pet_food


    def walk(self):
        self.pet.play()
        print(f'You walked your {self.pet.type}! {self.pet.name} now has {self.pet.health}! in Health!')
        return self
    def feed(self):
        self.pet.eat()
        print(f'You fed your {self.pet.type}! {self.pet.name} now has {self.pet.energy} energy and {self.pet.health} health')
        return self
    def bathe(self):
        print(f'You washed your {self.pet.type}! {self.pet.name} says {self.pet.bark} to thank you!')
        return self




chris = Ninja("Chris", "Frederick")

print(chris.walk())
print(chris.feed())
print(chris.bathe())


