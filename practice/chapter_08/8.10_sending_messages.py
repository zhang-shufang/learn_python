sent_messages = []

def send_messages(lst):
    """Print all messages in the list, and clear the original list."""
    while lst:
        message = lst.pop()
        print(message)
        sent_messages.append(message)

messages = [
    'time',
    'dinner',
    'food']

send_messages(messages)

print(messages)
print(sent_messages)

# 注意传入参数的方式
"""reference
def send_messages(messages, sent_messages):
    # Print each message, and then move it to sent_messages.
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
"""