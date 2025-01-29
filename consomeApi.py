import requests

def fetch_data(endpoint):
    """Função para buscar dados de um endpoint específico da API JSONPlaceholder."""
    base_url = "https://jsonplaceholder.typicode.com/"
    try:
        response = requests.get(base_url + endpoint)
        response.raise_for_status() # Verifica o status da resposta HTTP, se o status indica erro um HTTPError será lançado
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar-se à API: {e}")
        return None

def display_users(users):
    """Exibe uma lista de usuários com seus IDs e nomes."""
    print("\nLista de usuários:")
    print(f"{'ID':<3} | Nome")
    print("-" * 20)
    for user in users:
        print(f"{user['id']:<3} | {user['name']}") #"<3" é para alinhar os itens

def display_user_details(user, posts):
    """Exibe os detalhes de um usuário específico e seus posts."""
    print(f"\nDetalhes do usuário:")
    print(f"Id: {user['id']}")
    print(f"Nome: {user['name']}")
    print(f"Email: {user['email']}\n")

    print("Títulos dos posts:")
    if posts: #aqui
        for post in posts:
            print(f"- {post['title']}")
    else:
        print("Nenhum post encontrado para este usuário.")

def main():
    """Função principal do script."""
    # Busca dados de usuários
    users = fetch_data("users")
    if not users:
        return

    display_users(users)

    user_id = -1
    while user_id!=0:
        try:
            user_id = int(input("\nDigite o ID de um usuário para ver detalhes ou 0 para sair: "))
            if user_id == 0:
                print("Encerrando o programa.")
                break

            # Busca informações do usuário pelo id
            user = next((user for user in users if user['id'] == user_id), None)
            if not user:
                print("ID de usuário inválido. Tente novamente.")
                continue

            # Busca posts do usuário pelo id
            posts = fetch_data(f"posts?userId={user_id}")
            if posts is None:
                continue

            display_user_details(user, posts)
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
