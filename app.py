import os

os.system("cls")
print("""
███████████████████████████████████
██▀▄─██▄─▄█░█▄─▄▄─█─▄▄─█─▄▄─█▄─▄▄▀█
██─▀─███─██▄██─▄███─██─█─██─██─██─█
▀▄▄▀▄▄▀▄▄▄▀▄▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀\n""")
print("""Selecione uma opção:
1. Cadastrar restaurante
2. Listar restaurantes
3. Ativar  restaurante
4. Sair.
""")

def finalizar_app():
    os.system("cls")
    print("Saindo do aplicativo...")
    exit()

def cadastrar_restaurante():
    os.system("cls")
    print("Cadastrar restaurante\n")
    nome = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    telefone = input("Digite o telefone do restaurante: ")
    print(f"\nRestaurante '{nome}' cadastrado com sucesso!\n")


resposta = int(input("Digite a opção desejada: "))

while resposta != 4:
    if resposta == 1:
        cadastrar_restaurante()
    elif resposta == 2:
        print("Listar restaurantes\n")
    elif resposta == 3:
        print("Ativar restaurante\n")
    else:
        print("Opção inválida. Tente novamente.\n")

    print("""Selecione uma opção:
    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar  restaurante
    4. Sair.
    """)
    resposta = int(input("Digite a opção desejada: "))

finalizar_app()
