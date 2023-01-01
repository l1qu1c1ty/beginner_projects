import random
from pyfiglet import Figlet
from colorama import Fore


def main():
    play_game()


def ascii_banner(banner):
    figlet_banner = Figlet()
    print(Fore.GREEN, end="")
    print(figlet_banner.renderText(banner))


def play_game():
    while True:
        ascii_banner("Number\nGuess")
        secret_number = random.randint(1, 100)
        lives_remaining = 10
        high_score = 100
        for guess_count in range(lives_remaining):
            try:
                guess_number = int(input("Guess my secret number: "))

                if guess_number == secret_number:
                    print("Congratulations! You guess my secret number.")
                    print(f"High Score: {high_score}")
                    print(f"You guessed {guess_count+1} times")
                    ascii_banner("You Win :-)")
                    break

                else:
                    print("No, You don't guess my secret number.")
                    high_score -= 10
                    if guess_number > secret_number:
                        print("The number you guessed is big.")

                    else:
                        print("The number you guessed is low.")

                    lives_remaining -= 1

                    if lives_remaining != 0:
                        print(f"You have {lives_remaining} lives left.")
                        print("Try Again...")

                        if (secret_number % 2 == 0):
                            print("My secret number is even number.")

                        else:
                            print("My secret number is an odd number.")

                    else:
                        ascii_banner("Game\nOver")
                        print(f"My secret number is {secret_number}.")
                        break

            except ValueError:
                print("Enter an integer value!")

            except KeyboardInterrupt:
                print("You exited the program.")
                break

            except ZeroDivisionError:
                print("Zero Division Error!")

            except:
                print("Something Went Wrong...")

        play_again = input("Do you want to play again ? (Y/N)").upper()

        if play_again == "Y":
            continue

        else:
            break


if __name__ == "__main__":
    main()
