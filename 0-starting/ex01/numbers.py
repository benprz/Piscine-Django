def read_numbers():
    numbers = []
    line = open('numbers.txt', 'r')
    delimiter = ','
    for number in line.read().split(delimiter):
        numbers.append(int(number))
    return numbers

def print_numbers(numbers):
    for number in numbers:
        print(number)

if __name__ == '__main__':
    numbers = read_numbers()
    if len(numbers) > 0:
        print_numbers(numbers)