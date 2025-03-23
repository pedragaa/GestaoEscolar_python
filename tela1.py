import getpass

# Lista de usuários e cursos já cadastrados
usuarios = []

cursos = [
    {
        "nome": "Lei Geral de Proteção de Dados (LGPD)",
        "descricao": "Aprenda os princípios da LGPD, direitos dos titulares de dados e como proteger informações pessoais.",
        "carga": "20 horas"
    },
    {
        "nome": "Cibersegurança",
        "descricao": "Entenda como se proteger de ameaças digitais, como vírus, ataques hacker e boas práticas na internet.",
        "carga": "18 horas"
    }
]

def fazer_cadastro():
    print("\n---- Tela de Cadastro ----")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    
    while True:
        senha = getpass.getpass("Digite sua senha: ")
        confirmasenha = getpass.getpass("Confirme sua senha: ")
        if senha == confirmasenha:
            usuarios.append({"nome": nome, "email": email, "senha": senha})
            print(f"Cadastro realizado para {nome}!\n")
            break
        else:
            print("As senhas não coincidem. Tente novamente.\n")

def fazer_login():
    print("\n---- Tela de Login ----")
    email = input("Digite seu email: ")
    senha = getpass.getpass("Digite sua senha: ")
    
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuario['nome']}!\n")
            return
    print("Usuário ou senha inválidos!\n")

def cursos_disponiveis():
    if not cursos:
        print("\nNenhum curso cadastrado no momento.\n")
        return

    print("\n---- Cursos Disponíveis ----")
    for idx, curso in enumerate(cursos, start=1):
        print(f"{idx} - {curso['nome']}")

    print("0 - Voltar ao menu principal")
    opcao = input("\nEscolha um curso para ver mais informações: ")

    if opcao == "0":
        print("Voltando ao menu principal...\n")
    elif opcao.isdigit() and 1 <= int(opcao) <= len(cursos):
        curso = cursos[int(opcao) - 1]
        print(f"\n--- {curso['nome']} ---")
        print(f"Descrição: {curso['descricao']}")
        print(f"Carga horária: {curso['carga']}\n")
        input("Pressione Enter para voltar ao menu principal...")
    else:
        print("Opção inválida. Retornando ao menu principal...\n")
        input("Pressione Enter para continuar...")

def cadastrar_cursos():
    print("\n---- Cadastro de Cursos ----")
    nome = input("Digite o nome do curso: ")
    descricao = input("Digite a descrição do curso: ")
    carga = input("Digite a carga horária do curso: ")
    
    cursos.append({
        "nome": nome,
        "descricao": descricao,
        "carga": carga
    })

    print(f"Curso '{nome}' cadastrado com sucesso!\n")

def cadastrar_modulo():
    print("\n---- Cadastro de Módulo ----")
    modulo = input("Digite o nome do módulo: ")
    print(f"Módulo '{modulo}' cadastrado com sucesso!\n")

def mais_informacoes():
    print("\n---- Mais Informações ----")
    print("Essa plataforma foi criada para a educação infantil segura.\n")

def sair():
    print("\nSaindo do sistema... Até logo!")
    exit()

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
    print("6 - Ver cursos disponíveis")
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
    elif escolha == "6":
        cursos_disponiveis()
    elif escolha == "7":
        sair()
    else:
        print("\nOpção inválida! Tente novamente.\n")
