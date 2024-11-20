def main():
    while True:
        user_input = input("What you gotta say?: ")
        if user_input == "STOP":
            print("Goodbye!")
            break
        else:
            print("I got that! Anything else?")

if __name__ == "__main__":
    main()
