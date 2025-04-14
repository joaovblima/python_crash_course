prompt = "\nDigite algo que eu vou repetir de volta pra você:"
prompt += "\nDigite sair para encerrar o programa. "
active = True
message = ""
while active:
    message = input(prompt)
    if message == 'sair':
        active = False
    else:
        print(message)