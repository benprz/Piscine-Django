class HotBeverage:
    price=0.30
    name="hot beverage"

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return f"name : {self.name}" + "\n" + f"price : {self.price}" + "\n" + f"description : {self.description()}"

class Coffee(HotBeverage):
    name="coffee"
    price=0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    name="tea"
    price=0.30

    def description(self):
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    name="chocolate"
    price=0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Capuccino(HotBeverage):
    name="cappuccino"
    price=0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
    hb=HotBeverage()
    coffee=Coffee()
    tea=Tea()
    chocolate=Chocolate()
    capuccino=Capuccino()
    #print all instances
    print(hb)
    print(coffee)
    print(tea)
    print(chocolate)
    print(capuccino)
    