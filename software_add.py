# Drew Van Amberg

password = input()
def encode(password):
    new_password = ''
    for character in password:
        character = int(character)
        character += 3
        new_password += str(character)
    return new_password

#David Favors
def decode(password):
    new_password = ''
    for character in password:
        character = int(character)
        character -= 3
        new_password += str(character)
    return new_password


def main():
    resume = True
    while resume:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Exit")
        print("")
        option = int(input("Please enter an option: "))
        password = input("Please enter your password to encode: ")

        if option == 1:
            encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            decode(password)
            print(f"The encoded password is {encode(password)}, and the original password is {decode(password)}")
        elif option == 3:
            break


if __name__ == "main":
    main()
