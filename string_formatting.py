def print_formatted(number):
    # your code goes here
    pad = len(bin(number)[2:])
    print(pad)
    if 1 <= number <= 99:
        for num in range(1, number + 1):
            decs = str(num).rjust(pad, " ")
            octs = oct(num)[2:].rjust(pad, " ")
            hexs = hex(num)[2:].upper().rjust(pad, " ")
            bins = bin(num)[2:].rjust(pad, " ")
            print(decs,octs,hexs,bins)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)