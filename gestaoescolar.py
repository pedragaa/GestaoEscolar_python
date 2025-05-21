import json
import getpass
import os
import re

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_CURSOS = "cursos.json"
ARQUIVO_MODULOS = "modulos.json"
ARQUIVO_QUESTIONARIOS = "questionarios.json"
ARQUIVO_RESULTADOS = "resultados.json"

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

usuarios = carregar_dados(ARQUIVO_USUARIOS)
cursos = carregar_dados(ARQUIVO_CURSOS)
modulos = carregar_dados(ARQUIVO_MODULOS)
questionarios = carregar_dados(ARQUIVO_QUESTIONARIOS)
resultados = carregar_dados(ARQUIVO_RESULTADOS)

usuario_logado = None

def senha_segura(senha):
    return (len(senha) >= 8 and
            re.search(r"[A-Z]", senha) and
            re.search(r"[a-z]", senha) and
            re.search(r"\d", senha) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha))

def fazer_cadastro():
    print("\n---- Tela de Cadastro ----")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")

    for u in usuarios:
        if u["email"] == email:
            print("Já existe um usuário com esse e-mail.\n")
            return

    while True:
        senha = getpass.getpass("Digite sua senha: ")
        if not senha_segura(senha):
            print("A senha deve conter:\n"
                  "- Pelo menos 8 caracteres\n"
                  "- Uma letra maiúscula\n"
                  "- Um número\n"
                  "- Um caractere especial (!@#$%^&* etc)\n")
            continue

        confirmasenha = getpass.getpass("Confirme sua senha: ")
        if senha == confirmasenha:
            novo_usuario = {"nome": nome, "email": email, "senha": senha}
            usuarios.append(novo_usuario)
            salvar_dados(ARQUIVO_USUARIOS, usuarios)
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
            return usuario
    print("Usuário ou senha inválidos!\n")
    return None

def tela_inicial():
    global usuario_logado
    while True:
        print("\n" + "=" * 80)
        print("************* BEM-VINDO À PLATAFORMA DE EDUCAÇÃO INFANTIL SEGURA **************")
        print("=" * 80)
        print("1 - Fazer cadastro")
        print("2 - Fazer login")
        print("3 - Sair")
        print("=" * 80)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fazer_cadastro()
        elif opcao == "2":
            usuario_logado = fazer_login()
            if usuario_logado:
                break
        elif opcao == "3":
            sair()
        else:
            print("Opção inválida! Tente novamente.\n")

def realizar_questionario(curso_nome):
    print(f"Iniciando o questionário do curso: {curso_nome}")

    with open('questionarios.json', 'r', encoding='utf-8') as f:
        questionarios = json.load(f)

    perguntas = next((item["perguntas"] for item in questionarios if item["curso"] == curso_nome), None)

    if perguntas is None:
        print(f"Nenhum questionário encontrado para o curso '{curso_nome}'.")
        return

    total_perguntas = len(perguntas)
    acertos = 0

    for i, pergunta in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")
        for idx, opcao in enumerate(pergunta["respostas"], start=1):
            print(f"  {chr(64 + idx)}. {opcao}")
        resposta = input("Sua resposta (A, B, C): ").strip().upper()
        index = ord(resposta) - 65
        if 0 <= index < len(pergunta["respostas"]):
            if pergunta["respostas"][index] == pergunta["correta"]:
                print("✅ Correto!")
                acertos += 1
            else:
                print(f"❌ Errado! Resposta correta: {pergunta['correta']}")
        else:
            print("❌ Resposta inválida.")

    print(f"\nVocê acertou {acertos} de {total_perguntas} perguntas. ({(acertos / total_perguntas) * 100:.1f}%)")

            
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
        escolha = input("Deseja realizar o questionário deste curso? (s/n): ").lower()
        if escolha == "s":
            realizar_questionario(curso['nome'])
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
    salvar_dados(ARQUIVO_CURSOS, cursos)
    print(f"Curso '{nome}' cadastrado com sucesso!\n")

def cadastrar_modulo():
    print("\n---- Cadastro de Módulo ----")
    nome = input("Digite o nome do módulo: ")
    descricao = input("Digite a descrição do módulo: ")
    carga = input("Digite a carga horária do módulo: ")

    modulos.append({
        "nome": nome,
        "descricao": descricao,
        "carga": carga
    })
    salvar_dados(ARQUIVO_MODULOS, modulos)
    print(f"Módulo '{nome}' cadastrado com sucesso!\n")

def modulos_disponiveis():
    print("\n---- Módulos Cadastrados ----")
    if not modulos:
        print("Nenhum módulo cadastrado ainda.\n")
        return

    for idx, modulo in enumerate(modulos, start=1):
        print(f"{idx} - {modulo['nome']}")
    print("0 - Voltar ao menu principal")

    opcao = input("\nEscolha um módulo para ver mais informações: ")

    if opcao == "0":
        print("Voltando ao menu principal...\n")
    elif opcao.isdigit() and 1 <= int(opcao) <= len(modulos):
        modulo = modulos[int(opcao) - 1]
        print(f"\n--- {modulo['nome']} ---")
        print(f"Descrição: {modulo['descricao']}")
        print(f"Carga horária: {modulo['carga']}\n")
        input("Pressione Enter para voltar ao menu principal...")
    else:
        print("Opção inválida. Retornando ao menu principal...\n")
        input("Pressione Enter para continuar...")

def mais_informacoes():
    print("\n---- Mais Informações ----")
    print("Essa plataforma foi criada para a educação infantil segura.\n")

    print("---- Informações de Segurança ----")
    print("🔒 Segurança de Dados:")
    print("- Seus dados pessoais são armazenados com segurança e utilizados apenas para fins educacionais.")
    print("- Evite compartilhar sua senha com outras pessoas.\n")

    print("📜 LGPD (Lei Geral de Proteção de Dados):")
    print("- Garantimos seus direitos como titular de dados.")
    print("- Você pode solicitar a exclusão ou alteração de suas informações a qualquer momento.")
    print("- Tratamos seus dados de forma transparente e segura.\n")

    print("💡 Boas Práticas de Segurança:")
    print("- Use senhas fortes e únicas para seu cadastro.")
    print("- Sempre faça logout após utilizar a plataforma em dispositivos compartilhados.")
    print("- Desconfie de links ou mensagens suspeitas que peçam seus dados pessoais.")
    print("- Mantenha seu dispositivo atualizado e com antivírus ativo.\n")

    input("Pressione Enter para voltar ao menu principal...")

def sair():
    print("\nSaindo do sistema... Até logo!")
    exit()

# Função cadastrar_questionario removida

tela_inicial()

while True:
    print("\n" + "*" * 80)
    print("***************** PLATAFORMA DE EDUCAÇÃO INFANTIL SEGURA *************************")
    print("*" * 80)
    print("1 - Cadastrar cursos")
    print("2 - Cadastrar módulo de cursos")
    print("3 - Ver módulos cadastrados")
    print("4 - Mais informações")
    print("5 - Ver cursos disponíveis")
    print("6 - Sair")
    # Opção 7 removida do menu
    print("*" * 80)

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_cursos()
    elif escolha == "2":
        cadastrar_modulo()
    elif escolha == "3":
        modulos_disponiveis()
    elif escolha == "4":
        mais_informacoes()
    elif escolha == "5":
        cursos_disponiveis()
    elif escolha == "6":
        sair()
    else:
        print("Opção inválida. Tente novamente.")
