class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."
    
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

class Intern:
    Name = "My name? I’m nobody, an intern, I have no name"

    def __init__(self, name: str= None):
        if name != None:
            self.Name = name
    
    def __str__(self):
        return self.Name
    
    def make_coffee(self):
        return Coffee()

def run():
    intern1 = Intern()
    intern2 = Intern("Mark")
    
    print(intern1, intern2)
    print(intern2.make_coffee())

    try:
        intern2.make_coffee().work()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()