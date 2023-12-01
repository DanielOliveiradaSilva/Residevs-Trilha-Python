import os
# Função para reajustar o salário em 10%

def Reajusta_dez_porcento(listaDeEmpregados):
    for funcionariox in listaDeEmpregados:
        
        aumento =  (funcionariox['salario'] /100) *10  # Calcula 10% do salário
        funcionariox['salario'] += aumento  # Soma o aumento ao salário existente

# Função para ler os dados dos funcionários de um arquivo
def ler_dados_funcionarios(arquivo):
    listaDeFuncionarios = []
    try:
        with open(arquivo, 'r') as file:
            for line in file:
                dados = line.strip().split(',')  # dados separados por vírgula
                if len(dados) == 6:
                    nome, sobrenome, ano_nascimento, RG, ano_admissao, salario = dados
                    #dicionario
                    empregado = {
                        'nome': nome,
                        'sobrenome': sobrenome,
                        'ano_nascimento': int(ano_nascimento),
                        'RG': RG,
                        'ano_admissao': int(ano_admissao),
                        'salario': float(salario)
                    }
                    #lista de dicionarios
                    listaDeFuncionarios.append(empregado)
                else:
                    print(f"Dados inválidos: {line}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return  listaDeFuncionarios

def salvar_dados_funcionarios(arquivo, listaDeFuncionarios):
    with open(arquivo, 'w') as file:
        for funcionario in listaDeFuncionarios:
            linha = f"{funcionario['nome']},{funcionario['sobrenome']},{funcionario['ano_nascimento']},{funcionario['RG']},{funcionario['ano_admissao']},{funcionario['salario']}\n"
            file.write(linha)

def adicionar_funcionario(listaDeFuncionarios):
    while True:
        nome = input("Digite o nome do novo funcionário: ")
        if nome.isalpha():
            break
        else:
            print("Nome inválido. Digite apenas letras.")

    while True:
        sobrenome = input("Digite o sobrenome do novo funcionário: ")
        if sobrenome.isalpha():
            break
        else:
            print("Sobrenome inválido. Digite apenas letras.")

    while True:
        ano_nascimento = input("Digite o ano de nascimento do novo funcionário: ")
        if ano_nascimento.isdigit():
            break
        else:
            print("Ano de nascimento inválido. Digite apenas números.")

    while True:
        RG = input("Digite o RG do novo funcionário: ")
        if RG.isdigit():
            break
        else:
            print("RG inválido. Digite apenas números.")

    while True:
        ano_admissao = input("Digite o ano de admissão do novo funcionário: ")
        if ano_admissao.isdigit():
            break
        else:
            print("Ano de admissão inválido. Digite apenas números.")

    while True:
        salario = input("Digite o salário do novo funcionário: ")
        try:
            salario = float(salario)
            break
        except ValueError:
            print("Salário inválido. Digite um número válido.")

    novo_funcionario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'ano_nascimento': int(ano_nascimento),
        'RG': RG,
        'ano_admissao': int(ano_admissao),
        'salario': float(salario)
    }

    listaDeFuncionarios.append(novo_funcionario)
    print("Novo funcionário adicionado com sucesso!")
def reajustar_salario_de_um_funcionario(funcionarios):
    print("Funcionários disponíveis:")
    for index, funcionario in enumerate(funcionarios):
        print(f"{index}: {funcionario['nome']} {funcionario['sobrenome']}")

    while True:
        try:
            indice = int(input("Digite o id do funcionário para reajustar o salário: "))
            if 0 <= indice < len(funcionarios):
                aumento = (funcionarios[indice]['salario'] / 100) * 10
                funcionarios[indice]['salario'] += aumento
                print(f"Salario do funcionario {funcionarios[indice]['nome']} reajustado com suceso.")
                break
            else:
                print("Índice inválido. Digite um id valido.")
        except ValueError:
            print("ID inválido. Digite um numero valido.")

def exibir(listaDeFuncionarios):
    for empregado in listaDeFuncionarios:
        print(empregado)
# Função principal para testar o reajuste de salários
def main():
    arquivo_funcionarios = 'Empresa/funcionarios.txt'  #arquivo de dados

    # Ler os dados dos funcionários do arquivo
    liataDeFuncionarios = ler_dados_funcionarios(arquivo_funcionarios)

    if liataDeFuncionarios:
        print("Lista de funcionários antes do reajuste:")
        for empregado in liataDeFuncionarios:
            print(empregado)

    Reajusta_dez_porcento(liataDeFuncionarios)

    print("\nLista de funcionários apois o reajuste de 10% nos salários:")
    exibir(liataDeFuncionarios)

    while True:
        print("\n=== MENU ===")
        print("1. Adicionar novo funcionário")
        print("2. Salvar dados dos funcionários em arquivo")
        print("3. Reajustar salário de um funcionário")
        print("4. exibir lista")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario(liataDeFuncionarios)
        elif opcao == '2':
            salvar_dados_funcionarios(arquivo_funcionarios, liataDeFuncionarios)
            print("Dados dos funcionários salvos no arquivo.")
        elif opcao == '3':
            reajustar_salario_de_um_funcionario(liataDeFuncionarios)
        elif opcao == '4':
            exibir(liataDeFuncionarios)
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
