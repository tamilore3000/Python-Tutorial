from operator import truediv


command = ""
started = False

print("Start - start car\nStop-to stop car\nquit-to quit game\nHelp- to get Options list")
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car Started Already")
        else:
            started = True 
            print("Car has started..")

    elif command == "stop":
        if not started:
            print("Car stopped Already")
        else:
            started = False
            print("Car stopped..")

    elif command == "quit":
        break
    elif  command == "help": 
        print("Start - start car\nStop-to stop car\nquit-to quit game")
    else :
        print("Sorry I dont understand")
