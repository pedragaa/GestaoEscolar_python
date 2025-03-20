def fazer_cadastro():
    print("\n---- Tela de Cadastro ----")
    nome = input("Digite seu nome: ")
    print(f"Cadastro realizado para {nome}!\n")

def fazer_login():
    print("\n---- Tela de Login ----")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    print(f"Login realizado para {usuario}!\n")

def cadastrar_cursos():
    print("\n---- Cadastro de Cursos ----")
    curso = input("Digite o nome do curso: ")
    print(f"Curso '{curso}' cadastrado com sucesso!\n")

def cadastrar_modulo():
    print("\n---- Cadastro de Módulo ----")
    modulo = input("Digite o nome do módulo: ")
    print(f"Módulo '{modulo}' cadastrado com sucesso!\n")

def mais_informacoes():
    print("\n---- Mais Informações ----")
    print("Essa plataforma foi criada para a educação infantil segura.\n")

def sair():
    print("\nSaindo do sistema... Até logo!")
    exit()  # Encerra o programa

# Menu principal
while True:
    print("\n" + "*" * 80)
    print("***************** PLATAFORMA DE EDUCAÇÃO INFANTIL SEGURA *************************")
    print("*" * 80)
    print("1 - Fazer cadastro")
    print("2 - Fazer login")
    print("3 - Cadastrar cursos")
    print("4 - Cadastrar módulo de cursos")
    print("5 - Mais informações")
    print("7 - Sair")
    print("*" * 80)

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        fazer_cadastro()
    elif escolha == "2":
        fazer_login()
    elif escolha == "3":
        cadastrar_cursos()
    elif escolha == "4":
        cadastrar_modulo()
    elif escolha == "5":
        mais_informacoes()
    elif escolha == "7":
        sair()
    else:
        print("\nOpção inválida! Tente novamente.\n")
