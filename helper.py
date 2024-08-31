# my helper file

def print_name():
    print("The __name__ variable is: ", __name__)

def print_fibonacci():
    print("I don't want to write code")

if __name__ == '__main__':
    choice = input("Enter your choice: ")
    if choice == "main":
        print("This is MAIN")
    else:
        for _ in __name__:
            print(_)