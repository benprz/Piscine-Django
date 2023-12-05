import sys

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

def capital_city(state):
    if state in states:
        return capital_cities[states[state]]
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()

    state = sys.argv[1]
    capital = capital_city(state)
    if capital:
        print(capital)
    else:
        print('Unknown state')
    