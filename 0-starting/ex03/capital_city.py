import sys

def get_capital_city(arg, states, capital_cities):
    if arg in states:
        return capital_cities[states[arg]]
    else:
        return None

def run(arg):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    capital = get_capital_city(arg, states, capital_cities)
    if capital:
        print(capital)
    else:
        print('Unknown state')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    