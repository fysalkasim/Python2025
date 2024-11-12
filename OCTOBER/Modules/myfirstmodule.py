def palindrome():
    word = input("Enter a word:")
    str_rev=word[::-1]
    if str_rev==word:
        print(f"The word \"{word}\" is a palindrome")
    else:
        print(f"The word \"{word}\" is not a palindrome")

def greeting(name):
    global msg
    msg = "Welcome to the world of python"
    print(f"{name}! {msg}")
