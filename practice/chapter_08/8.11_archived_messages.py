def send_messages(messages, sent_messages):
    """Print all messages in the list, and clear the original list."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = [
    'time',
    'dinner',
    'food']

sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

# 
"""reference

"""