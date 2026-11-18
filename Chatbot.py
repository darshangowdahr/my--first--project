print("Hello! Naanu ninna Chatbot 🤖")
print("Nanna hesaru Darshan Bot")

name = input("Ninna hesaru yenu? ")

print(f"Hi {name}! Ninnannu bhetiyagi khushi aaythu!")

while True:
    msg = input("Neenu: ").lower()

    if msg == "hi" or msg == "hello":
        print("Bot: Hi! Hegidiya?")
    elif msg == "how are you":
        print("Bot: Naanu super! Neenu hegidiya?")
    elif msg == "bye":
        print("Bot: Bye bye! Malli sigona 👋")
        break
    else:
        print("Bot: Sorry, adhu nanage gothilla, innondu keli!")

