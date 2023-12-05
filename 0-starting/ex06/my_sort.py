d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',

}

def my_sort(d):
    for key, value in sorted(d.items(), key=lambda item: (item[1], item[0])):
        print("%s: %s" % (key, value))

if __name__ == '__main__':
    my_sort(d)