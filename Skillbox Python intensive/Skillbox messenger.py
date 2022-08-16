test_message = {
    "text": "Эй йоу, какие дела?",
    "sender": "Mike",
    "time": "19:31"
}

# messanger
all_messanges = []  # list of all messanges

# function to display messages
def print_message(message):
    print(f"-[{message['sender']}]: {message['text']} // {message['time']}")

# call function
print_message(test_message)