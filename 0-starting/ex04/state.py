import sys

def get_state(arg, states, capital_cities):
    state = None
    for key, value in capital_cities.items():
        if value == arg:
            state = key
            break
    if state:
        for key, value in states.items():
            if value == state:
                state = key
                break
    return state

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

    state = get_state(arg, states, capital_cities)
    if state:
        print(state)
    else:
        print('Unknown capital city')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    