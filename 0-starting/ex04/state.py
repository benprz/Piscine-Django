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

def state(capital_city):
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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()

    capital_city = sys.argv[1]
    state = state(capital_city)
    if state:
        print(state)
    else:
        print('Unknown capital city')
    