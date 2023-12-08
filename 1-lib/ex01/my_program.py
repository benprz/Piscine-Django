from local_lib.path import Path

if __name__ == '__main__':
    Path('my_path').mkdir_p().cd()
    file = Path('my_test.txt').touch()
    file.write_lines(['Je suis une ligne', 'Je suis une autre ligne'])
    print(file.read_text())