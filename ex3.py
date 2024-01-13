def guess_the_number():
    print("Welcome To Guess The Number,you will be given 9 guesses to guess a random number Chosen."
          "The number is between 1 and 150. All The Best\n\nPress ENTER to start the game")
    strt = input()
    import random_module
    n = random.randint(0, 100)
    a = 0
    if strt.upper() == "":
        print("The number has been chosen.")
        while (a < 9):
            try:

                    i = int(input("Guess the number\n"))
                    a = a + 1
                    if n < i:
                        print("Try a smaller number\n\nNumber of guesses left:", 9 - a)


                    elif n > i:
                        print("Try a greater number\n\nNumber of guesses left:", 9 - a)
                    else:
                        print("You have guessed the correct number\nNumber of guesses taken=", a)
                        break
                    if a > 8 and n != i:
                        print("Game Over. You have made 9 Guesses.\nThe number was",n)
            except:
                print("Input toh dhang se dalo. Number dalna hai")
    else:
        print("See You Next Time Then")
guess_the_number()
def again():
    print("Do you want to play again?\nYes(Y)/No(N)")
    i = input().capitalize()
    if i == "Y":
        guess_the_number()
        again()
    elif i=="N":
        print("Thank You for playing.\nSee you next time.")
    else:
        print("Enter 'Y' for yes and 'N' for no.\n")
        again()
again()