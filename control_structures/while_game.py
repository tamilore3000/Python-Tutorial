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