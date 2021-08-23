"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""

MENU = '''L = List places
R = Recommend random place
A = Add new place
M = Mark a place as visited
Q = Quit'''


def main():
    print("Travel Tracker 1.0 - by <Your Name>")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print("List")
        elif choice == "R":
            print("Random")
        elif choice == "A":
            print("Add")
        elif choice == "M":
            print("mark")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Have a nice day :)")


if __name__ == '__main__':
    main()
