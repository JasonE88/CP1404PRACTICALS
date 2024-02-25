def main():
    min_length = 8

    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password length should be at least", min_length, "characters.")
        password = input("Enter a password: ")

    print("*" * len(password))


main()