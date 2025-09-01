class Superhero:
    def __init__(self, name, power, strength, secret_identity):
        self.name = name
        self.power = power
        self.strength = strength
        self.secret_identity = secret_identity

    def introduce(self):
        print(f"Hi! I'm {self.name}, and I fight crime with my {self.power} power.")

    def use_superpower(self):
        print(f"{self.name} uses their {self.power} power to defeat the villain!")

    def attack(self):
        print(f"{self.name} attacks with a strength of {self.strength}!")

    def reveal_identity(self):
        print(f"Secret identity: {self.secret_identity}")


# Inheritance layer (Superhero -> Hero -> SuperHeroWithVehicle)
class Hero(Superhero):
    def __init__(self, name, power, strength, secret_identity, hero_type):
        super().__init__(name, power, strength, secret_identity)
        self.hero_type = hero_type

    def display_hero_type(self):
        print(f"{self.name} is a {self.hero_type} hero.")

# Superhero with Vehicle (Inheriting from Hero)
class SuperHeroWithVehicle(Hero):
    def __init__(self, name, power, strength, secret_identity, hero_type, vehicle):
        super().__init__(name, power, strength, secret_identity, hero_type)
        self.vehicle = vehicle

    def show_vehicle(self):
        print(f"{self.name} uses their {self.vehicle} for fast travel!")

    def use_superpower(self):
        # Polymorphism: Overriding the superpower method to change behavior.
        print(f"{self.name} uses their {self.power} power while flying in the {self.vehicle}!")

# Testing the Superhero Class
iron_man = SuperHeroWithVehicle("Iron Man", "Repulsor beams", 90, "Tony Stark", "Tech Genius", "Iron Man Suit")
iron_man.introduce()
iron_man.attack()
iron_man.show_vehicle()
iron_man.use_superpower()
iron_man.reveal_identity()

print("\n")
batman = Hero("Batman", "Martial Arts", 85, "Bruce Wayne", "Dark Knight")
batman.introduce()
batman.attack()
batman.display_hero_type()
batman.reveal_identity()
