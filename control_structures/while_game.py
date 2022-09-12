secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter Guess: "))
    guess_count += 1 
    if guess == secret_num:
        print("You win!")
        break
    else :
        print("Oops try again")
else:
    print("OUT OF FREE TRIALS")

guess_word = "fox"
guess = ""
count = 0
limit = 3
out_of_guesses = False 

while guess != guess_word and not out_of_guesses:
    if count < limit:
        guess = input("Enter your guess: ")
        count += 1
        if guess == guess_word:
            print("You win!")
        else:
            print("Try again")

    else:
        out_of_guesses = True
        print("You are out of Guesses\nLOSER! ")


    