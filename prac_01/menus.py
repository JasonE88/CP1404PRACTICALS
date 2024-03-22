MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(MENU)
user_input = input(">>> ").upper()
while user_input != "Q":
    if user_input == "H":
        print(f"Hello {name}")
    elif user_input == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    user_input = input(">>> ").upper()
print("Finished")