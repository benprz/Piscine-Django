def read_numbers():
    numbers = []
    file = open('numbers.txt', 'r')
    delimiter = ','
    for number in file.read().split(delimiter):
        numbers.append(int(number))
    return numbers

def print_numbers():
    numbers = read_numbers()
    if len(numbers) > 0:
        for number in numbers:
            print(number)

if __name__ == '__main__':
    print_numbers()