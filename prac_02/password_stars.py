def main():
    password = get_password()

    print_asterisks(password)


def get_password():
    min_length = 8

    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password length should be at least", min_length, "characters.")
        password = input("Enter a password: ")

    return password


def print_asterisks(password):
    print("*" * len(password))


main()
