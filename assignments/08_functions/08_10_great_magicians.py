# Assuming the original list of messages from Exercise 8-9
text_messages = [
    "Tristan, how are you?",
    "I'm doing great, thanks for asking!",
    "Let's meet up this weekend.",
    "Sounds good, where should we meet?",
    "How about the park at 2 PM?"
]

# Function to send messages
def send_messages(messages):
    sent_messages = []
    for message in messages:
        print(message)
        sent_messages.append(message)
    return sent_messages

sent_messages = send_messages(text_messages)

print("\nOriginal list of messages:")
print(text_messages)

print("\nList of sent messages:")
print(sent_messages)