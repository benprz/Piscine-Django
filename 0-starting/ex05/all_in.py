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

def get_capital_city(arg, states, capital_cities):
    if arg in states:
        return capital_cities[states[arg]]
    else:
        return None

def run(args):
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

    for arg in args.split(','):
        formatted_arg = " ".join(arg.split()).title()
        if formatted_arg:
            capital = get_capital_city(formatted_arg, states, capital_cities)
            if capital:
                print("{} is the capital of {}".format(capital, formatted_arg))
            else:
                state = get_state(formatted_arg, states, capital_cities)
                if state:
                    print("{} is the capital of {}".format(formatted_arg, state))
                else:
                    print('{} is neither a capital city nor a state'.format(arg.strip()))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
