from game import play

if __name__ == "__main__":
    while True:
        play()
        if input("Do you want to play again?(Y or N): ").lower() in ('y', 'yes', '1', 'true'):
            continue
        else:
            print("Thanks for Playing!!😁")
            break