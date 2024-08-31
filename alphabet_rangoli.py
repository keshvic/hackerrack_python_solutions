import string


def print_rangoli(size):
    # your code goes here
    if 0 < size < 27:
        char_list = []
        for index, letter in enumerate(string.ascii_lowercase):
            if index == size:
                break
            char_list.append(letter)
        pattern = ""
        line_len = (size - 1)*4 + 1
        for n in range(size):
            pattern = char_list[-1-n]
            for _ in range(-n, 0):
                #print(f"n = {n}, _ = {_}, char_list[_] = {char_list[_]}")
                pattern = char_list[_]+"-"+pattern+"-"+char_list[_]
            print(pattern.center(line_len, '-'))
        for n in range(size-2, -1, -1):
            pattern = char_list[-1-n]
            for _ in range(-n, 0):
                pattern = char_list[_]+"-"+pattern+"-"+char_list[_]
            print(pattern.center(line_len, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)