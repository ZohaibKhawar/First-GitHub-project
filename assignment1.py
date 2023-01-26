import random

class Role:
    def __init__(self, name, strength, dexterity, intelligence, health):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.health = health

    def __str__(self):
        return f"{self.name}:\n\tStrength: {self.strength}\n\tDexterity: {self.dexterity}\n\tIntelligence: {self.intelligence}\n\tHealth: {self.health}"

class Game:
    def __init__(self):
        self.roles = {
            "barbarian": Role("Barbarian", 2, 1, -1, 10),
            "wizard": Role("Wizard", -1, 1, 2, 8)
        }
        self.current_role = None
        self.quest_completed = False

    def pick_role(self):
        print("Select a role:")
        for i, role in enumerate(self.roles):
            print(f"{i + 1}. {role}")
        choice = int(input("> ")) - 1
        self.current_role = list(self.roles.values())[choice]
        print(f"You have chosen the role of {self.current_role.name}.")
    
    def roll_dice(self):
        return random.randint(2, 12)

    def quest(self):
        challenges = [
            {"attribute": "strength", "difficulty": 3},
            {"attribute": "dexterity", "difficulty": 5},
            {"attribute": "intelligence", "difficulty": 7}
        ]
        for challenge in challenges:
            roll = self.roll_dice()
            attribute_value = getattr(self.current_role, challenge["attribute"])
            total_value = roll + attribute_value
            if total_value < 4:
                print("Critical Loss!")
                attribute_value -= 1
            elif total_value < 8:
                print("Loss!")
            elif total_value < 11:
                print("Win!")
            else:
                print("Critical Win!")
                attribute_value += 1
            setattr(self.current_role, challenge["attribute"], attribute_value)
            print(f"{challenge['attribute'].capitalize()} challenge: Rolled {roll}, attribute value {attribute_value}, total value {total_value}")
        print("Quest completed!")
        self.quest_completed = True


def main():
    game = Game()
    game.pick_role()
    game.quest()

if __name__ == "__main__":
    main()

