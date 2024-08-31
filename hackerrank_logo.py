# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
if 0 <= n <= 50:
    if n%2:
        max = (4*n + int(n/2) + 3)
        for i in range(max):
            if i < n:
                txt = 'H'*(2*i+1)
                print(txt.center(2*n - 1,' '))
            elif n <= i and i < (2*n + 1):
                txt1 = ' '*int(n/2)
                txt2 = 'H'*n
                txt3 = ' '*(n*3)
                print(txt1, end='')
                print(txt2, end='')
                print(txt3, end='')
                print(txt2)
            elif (2*n + 1) <= i and i < (2*n + int(n/2) + 2):
                txt4 = 'H'*n*5
                print(txt1, end='')
                print(txt4)
            elif (2*n + int(n/2) + 2) <= i and i < (3*n + int(n/2) + 3):
                print(txt1, end='')
                print(txt2, end='')
                print(txt3, end='')
                print(txt2)
            elif (3*n + int(n/2) + 3) <= i < (max):
                #txt5 = ' '*n + ' '*(n*2 + 
                txt5 = ' '*4*n
                var = (4*n + int(n/2) + 3) - i
                txt6 = 'H'*(2*var-1)
                print(txt5, end='')
                print(txt6.center(2*n - 1,' '))
                