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

def get_state(capital_city):
    state = None
    for key, value in capital_cities.items():
        if value == capital_city:
            state = key
            break
    if state:
        for key, value in states.items():
            if value == state:
                state = key
                break
    return state

def capital_city(state):
    if state in states:
        return capital_cities[states[state]]
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()

    input = sys.argv[1]
    for expr in input.split(','):
        formatted_expr = " ".join(expr.split()).title()
        if formatted_expr:
            capital = capital_city(formatted_expr)
            if capital:
                print("{} is the capital of {}".format(capital, formatted_expr))
            else:
                state = get_state(formatted_expr)
                if state:
                    print("{} is the capital of {}".format(formatted_expr, state))
                else:
                    print('{} is neither a capital city nor a state'.format(expr.strip()))
    