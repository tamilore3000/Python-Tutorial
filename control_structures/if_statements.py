price = 1000000
percent = 0
buyer = input("Do you have a good credit?\nYes or No\n")
Agent = buyer.capitalize()

if Agent == "Yes" or Agent == "yes":
    print("You need to put down 10%")
    percent = 10/100 * price
elif Agent == "No" or Agent == "no":
    print("You need to put down 20%")
    percent = 10/100 * price
else :
    print("Wrong Input")
print(f'Your down payment is ${percent}')