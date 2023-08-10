messages = [
    "Incorrect",
    "Really?",
    "Wait, How Don't you Know?"
    "You know what, just forget about it"
]

message_index = 0

while True:
    user_input = input("What's my favorite sport? :").lower()
    
    if user_input == "basketball":
        print("How did you know?")
        break
    else:
        print(messages[message_index])
        message_index = (message_index + 1) % len(messages)
