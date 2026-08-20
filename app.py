import os

restaurantes = [{"nome": "Chico do carangueijo", "endereco": "Rua das Flores, 123", "ativo": False},
                {"nome": "Pizza do Tio", "endereco": "Avenida Paulista, 1000", "ativo": True},
                {"nome": "Sushi Express", "endereco": "Rua das Palmeiras, 456", "ativo": True}]

def exibir_menu():
    """Essa função exibe o menu principal do aplicativo."""
    os.system("cls")
    print("""
███████████████████████████████████
██▀▄─██▄─▄█░█▄─▄▄─█─▄▄─█─▄▄─█▄─▄▄▀█
██─▀─███─██▄██─▄███─██─█─██─██─██─█
▀▄▄▀▄▄▀▄▄▄▀▄▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀\n""")
    print("""Selecione uma opção:
    1. Cadastrar restaurante
    2. Listar restaurantes
    3. Ativar/Desativar restaurante
    4. Sair.
    """)

def obter_resposta():
    """
    Essa função solicita ao usuário que digite uma opção do menu e valida a entrada.
    - Outputs:
        - resposta: Retorna a opção escolhida pelo usuário (1, 2, 3 ou 4).
    """
    while True:
        try:
            resposta = int(input("Digite o número da opção desejada: "))
            if resposta in [1, 2, 3, 4]:
                return resposta
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def __main__():
    """
    Essa função exibe o menu principal e solicita a entrada do usuário.
    """
    input("Pressione qualquer tecla para voltar ao aplicativo.")

exibir_menu()
resposta = obter_resposta()

def exibir_subtitulo(titulo):
    """Essa função exibe um subtítulo formatado no console.
    - Inputs:
        - titulo: Título a ser exibido.
    - Outputs:
        - Subtítulo formatado no console.
    """
    os.system("cls")
    linha = "-" * (len(titulo))
    print(linha)
    print(titulo)
    print(linha)
    print()

def finalizar_app():
    """
    Essa função exibe uma mensagem de saída e encerra o aplicativo.
    Outputs:
        - Mensagem de saída.
    """
    exibir_subtitulo("Saindo do aplicativo...")
    exit()

def cadastrar_restaurante():
    """
    Essa função cadastra um restaurante, solicitando o nome e endereço.
    
    - Inputs:
        - nome_do_restaurante: Nome do restaurante a ser cadastrado.
        - endereco: Endereço do restaurante a ser cadastrado.
    
    - Outputs:
        - Adiciona o restaurante à lista de restaurantes.
        - Exibe uma mensagem de sucesso após o cadastro.
    """
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    restaurante = {"nome": nome_do_restaurante, "endereco": endereco, "ativo": False}
    restaurantes.append(restaurante)
    exibir_subtitulo(f"Restaurante {nome_do_restaurante} cadastrado com sucesso!")

def listar_restaurantes():
    """
    Essa função lista todos os restaurantes cadastrados, exibindo o nome, endereço e status (ativo/inativo).
    - Outputs:
        - Lista de restaurantes formatada no console.
    """
    print("Nome do Restaurante".ljust(30) + "| Endereço".ljust(30) + "| Status")
    print("-" * 90)
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante["nome"]
        endereco = restaurante["endereco"]
        status = "Ativo" if restaurante["ativo"] else "Inativo"
        print(f"- {nome_do_restaurante.ljust(27)} | {endereco.ljust(27)} | ({status})")
    print("\n")

def ativar_restaurante():
    """Essa função permite ativar ou desativar um restaurante existente na lista.
    - Inputs:
        - nome_do_restaurante: Nome do restaurante a ser ativado/desativado.
    - Outputs:
        - Mensagem de sucesso após a ativação/desativação.
    """
    nome_do_restaurante = input("Digite o nome do restaurante que deseja ativar/desativar: ").lower()
    for restaurante in restaurantes:
        if restaurante["nome"].lower() == nome_do_restaurante:
            if restaurante["ativo"] == False:
                restaurante["ativo"] = True
                exibir_subtitulo(f"Restaurante '{nome_do_restaurante}' ativado com sucesso!")
                return
            else:
                restaurante["ativo"] = False
                exibir_subtitulo(f"Restaurante '{nome_do_restaurante}' foi desativado.")
                return
        else:
            exibir_subtitulo(f"Restaurante '{nome_do_restaurante}' não encontrado.")

while resposta != 4:
    if resposta == 1:
        exibir_subtitulo("Cadastre seu restaurante")
        cadastrar_restaurante()
    elif resposta == 2:
        exibir_subtitulo("Lista de restaurantes")
        listar_restaurantes()
    elif resposta == 3:
        exibir_subtitulo("Ativar/Desativar restaurante")
        ativar_restaurante()
    else:
        print("Opção inválida. Tente novamente.")
    __main__()
    exibir_menu()
    resposta = obter_resposta()

finalizar_app()