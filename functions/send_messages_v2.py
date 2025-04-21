def show_messages(messages):
    for message in messages:
        print(f"{message.title()}")

def send_messages(messages, sent_messages):
    while messages:
        actual_message = messages.pop()
        print(f'A mensagem: {actual_message} foi enviada.')
        sent_messages.append(actual_message)

    print(messages)
    print(sent_messages)

messages = ['Deus é bom', 'O verbo estava junto a Deus', "Sacramento da comunhão"]
messages_sents = []
show_messages(messages)


send_messages(messages[:], messages_sents)
print()
print(messages)
print(messages_sents)