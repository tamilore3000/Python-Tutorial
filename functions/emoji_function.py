from socket import MsgFlag


msg = input("Enter message: ")
def emojicon(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😃",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

emojified = emojicon(msg)
print(emojified)