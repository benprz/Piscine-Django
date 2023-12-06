import random
from beverages import *

class CoffeeMachine:
    drinks_served = 0

    def __init__(self):
        pass

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        print("Successfully repaired the machine!")
        self.drinks_served = 0

    def serve(self, beverage: HotBeverage):
        if self.drinks_served == 10:
            raise self.BrokenMachineException()
        
        self.drinks_served += 1
        if random.randint(0, 1) == 0:
            return self.EmptyCup()
        else:
            return beverage
        
if __name__ == "__main__":
    coffe_machine = CoffeeMachine()
    for i in range(23):
        try:
            print(coffe_machine.serve(Tea()), "\n")
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffe_machine.repair()