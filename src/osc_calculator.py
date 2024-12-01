def validate_input(lines, players):
    assert lines > 2 , "Lines must be strictly greater than 2."
    assert lines < players, "Lines must be strictly less than players."

def main():
    while True:
        print("Enter non-number to exit.") 
        try:
            lines = int(input("How many lines in the drill? "))
            players = int(input("How many players in the drill? "))
        except:
            print("Non-number entered. Exiting.")
            break
        validate_input(lines, players)

        if (players - 1) % lines == 0:
            if ((players - 1) // lines) % 2 == 0:
                print("Zero oscillations as # iterations approaches infinity.")
            else:
                print("Oscilllations occur as # iterations approaches infinity.")
        else:
            print("Unkown.")
        print("-" * 50)

if __name__ == "__main__":
    main()