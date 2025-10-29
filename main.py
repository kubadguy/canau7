def make_stronger(password: str):
    """
    makes a given password stronger
    """
    strong_password = ""
    # Iterate to the string
    for char in password:
        # Just shift it for a basic operation
        strong_char = char << 1
        strong_password += strong_char

    return strong_password

print("Here is a password generator")
mode = input("Mode(\"g\" for get mode & \"s\" for strenthen)")
mode = "get" if mode == "g" else "stregthen" if mode == "s" else None
if mode:
    password = input(f"Type any password{"(weak passwords are also okay)" if mode == "get" else ""}: ")
    output = make_stronger(password)
    print(f"{output} is your password")
else:
    print("Invalid mode")