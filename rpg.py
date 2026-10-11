import random
import csv
class Player:

    def __init__(self, name, health = 100, gold = 10):
        self.name = name
        self.health = health
        self.gold = gold

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Remaining Hp: {self.health}")
    def is_alive(self):
        return self.health > 0
    def save_game(self, filename ="save_data.csv"):
        with open(filename, mode= "w", newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Health", "Gold"])
            writer.writerow([self.name, self.health, self.gold])
        print(f"👾 Game Progress Successfully saved to {filename}!")
    @classmethod
    def load_game(cls, filename= "save_data.csv"):
        import os
        if not os.path.exists(filename):
            print("No save file found. Starting a fresh adventure!")
            return None
        with open(filename, mode = 'r') as file:
            reader = csv.reader(file)
            next(reader)
            saved_row = next(reader)
            print(f"⭐ Found saved data! Welcome back, {saved_row[0]}!")
            return cls(name=saved_row[0], health=int(saved_row[1]), gold=int(saved_row[2]))
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def take_damage(self, amount):
        self.health -= amount
        print(f"The {self.name} took {amount} damage! Remaining Hp of the enemy: {self.health}")
    def is_alive(self):
        return self.health > 0
hero = Player("Rohit")
monster = Enemy("Goblin", 30, 8)

print(f"---A wild {monster.name} appears!----")
while hero.is_alive() and monster.is_alive():
    rohit_dmg = random.randint(10, 20)
    monster.take_damage(rohit_dmg)
    if monster.is_alive():
        goblin_dmg = random.randint(5, 11)
        hero.take_damage(goblin_dmg)
        print('--------------------')
print(f"\n===Battle Over====")

if hero.is_alive():
    gold_reward = random.randint(5, 15)
    hero.gold += gold_reward
    print(f"Congratulation 🎉 {hero.name} defeated {monster.name}!")
    print(f"💰 Found {gold_reward} gold! Total Gold: {hero.gold}")
    hero.save_game()
else:
    print(f"🪦 {hero.name} has fallen in battle!")
