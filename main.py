def ord_ascii(character):
    """Returns the ASCII integer value for a single character or raises a ValueError."""
    if len(character) != 1:
        raise ValueError("Input must be a single character.")
    value = ord(character)
    if 0 <= value <= 127:
        return value
    else:
        raise ValueError(f"Character '{character}' is not a valid ASCII character.")

def chr_ascii(value):
    """Returns the ASCII character for an integer or raises a ValueError."""
    if not isinstance(value, int):
        raise TypeError("Input must be an integer.")
    if 0 <= value <= 127:
        return chr(value)
    else:
        raise ValueError(f"Integer {value} is outside the ASCII range (0-127).")

def make_stronger(password: str):
    """
    Makes a given password stronger by shifting characters and
    wrapping the value within the printable ASCII range.
    """
    strong_password = ""
    # Define the range of printable ASCII characters
    min_char_code = ord('!')  # 33
    max_char_code = ord('~')  # 126
    
    for character in password:
        # Get the character's ASCII value and shift it
        try:
            char_code = ord_ascii(character)
        except ValueError:
            # Handle non-ASCII characters gracefully
            strong_password += character
            continue

        # Shift the value and wrap it within the printable range
        shifted_code = char_code + 1
        if shifted_code > max_char_code:
            shifted_code = min_char_code + (shifted_code - max_char_code - 1)

        # Convert back to character and append to the result
        strong_character = chr_ascii(shifted_code)
        strong_password += strong_character

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