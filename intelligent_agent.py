from time import sleep

class WashingMachine:
    def __init__(self):
        self.water_level = 0
        self.detergent_level = 100  # Assume full detergent initially
        self.dirty_clothes = 0
        self.clean_clothes = 0

    def add_water(self, amount):
        self.water_level += amount

    def add_detergent(self, amount):
        self.detergent_level += amount

    def add_dirty_clothes(self, amount):
        self.dirty_clothes += amount

    def wash(self):
        if self.water_level >= 10 and self.detergent_level >= 5 and self.dirty_clothes > 0:
            print("Starting washing machine...")
            sleep(2)
            print("Adding detergent...")
            sleep(2)
            print("Filling water...")
            sleep(2)
            self.water_level -= 10
            self.detergent_level -= 5
            self.dirty_clothes -= 1
            self.clean_clothes += 1
            print("Washing completed successfully!")
        else:
            print("Insufficient resources or no dirty clothes to wash.")

# Example usage
washing_machine = WashingMachine()
washing_machine.add_water(20)
washing_machine.add_detergent(10)
washing_machine.add_dirty_clothes(3)
washing_machine.wash()
print("Clean clothes:", washing_machine.clean_clothes)
