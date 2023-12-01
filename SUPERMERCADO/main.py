# Função para inserir um novo produto
def inserir_produto(produtos):
    while True:
        try:
            codigo = input("Digite o código do produto (13 dígitos numéricos): ")
            if not (codigo.isdigit() and len(codigo) == 13):
                raise ValueError("Código inválido. Deve conter 13 dígitos numéricos.")
            
            for produto in produtos:
                if produto['codigo'] == codigo:
                    raise ValueError("Código já existe. Insira um código diferente.")
            
            nome = input("Digite o nome do produto: ")

            preco = float(input("Digite o preço do produto: "))
            produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco})
            print("Produto inserido com sucesso!")
            break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")

# Função para excluir um produto cadastrado
def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

# Função para listar todos os produtos
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("Lista de produtos:")
    for produto in produtos:
        print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Preço: R${produto['preco']:.2f}")

# Função para consultar o preço de um produto por código
def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço do produto '{produto['nome']}' é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")

# Função principal
def main():
    # Exemplo de produtos iniciais
    produtos = [
        {'codigo': '1234567890123', 'nome': 'Arroz', 'preco': 5.99},
        {'codigo': '9876543210987', 'nome': 'Feijão', 'preco': 4.49},
        {'codigo': '1111111111111', 'nome': 'Macarrão', 'preco': 3.25}
    ]

    while True:
        print("\n=== MENU ===")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto por código")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            excluir_produto(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            consultar_preco(produtos)
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()
