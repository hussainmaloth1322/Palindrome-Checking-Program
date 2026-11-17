"""Console program: check whether an input string is a palindrome."""

def is_palindrome(value):
    normalized = value.strip().lower()
    return normalized == normalized[::-1]


def main():
    value = input("Enter a string: ")
    if is_palindrome(value):
        print("The given string is a Palindrome")
    else:
        print("The given string is Not a Palindrome")


if __name__ == "__main__":
    main()
