# Consulta de Dados de uma API Pública

Este projeto é um script em Python que consome dados de uma API pública, manipula as informações recebidas e exibe os resultados de forma organizada. Ele utiliza a biblioteca `requests` para fazer requisições HTTP e manipular dados no formato JSON.

## Funcionalidades

1. **Exibição de Usuários:**
   - Lista os IDs e nomes de todos os usuários disponíveis na API.

2. **Detalhes do Usuário:**
   - Permite inserir o ID de um usuário para exibir seus detalhes (nome e email).
   - Lista os títulos dos posts criados pelo usuário selecionado.

3. **Tratamento de Erros:**
   - Verifica erros de conexão com a API.
   - Lida com IDs de usuário inválidos.
   - Garante que a entrada do usuário seja um número válido.

## Como Executar

### Pré-requisitos

1. Python 3 instalado no sistema.
2. Instalação da biblioteca `requests`:
   ```bash
   pip install requests
   ```

### Passos para Execução

1. Clone o repositório.
2. Execute o script no terminal no local ond foi clonado:
   ```bash
   python consomeApi.py
   ```

3. O programa exibirá uma lista de usuários com IDs e nomes. Você pode:
   - Inserir um ID para visualizar detalhes de um usuário.
   - Digitar `0` para sair do programa.

## Estrutura do Código

### `fetch_data(endpoint)`
Função para buscar dados da API JSONPlaceholder. Ela:
- Faz uma requisição HTTP ao endpoint fornecido.
- Verifica o status da resposta e lança um erro em caso de falha.
- Retorna os dados no formato JSON ou `None` em caso de erro.

### `display_users(users)`
Exibe uma lista de usuários com IDs e nomes, alinhando os dados para melhor visualização.

### `display_user_details(user, posts)`
Mostra os detalhes de um usuário específico (ID, nome, email) e lista os títulos de seus posts.

### `main()`
Função principal do script que:
- Busca a lista de usuários.
- Exibe os usuários e interage com o usuário para escolher um ID.
- Busca e exibe os detalhes e posts do usuário selecionado.
- Lida com entradas inválidas.
## Exemplo de Saída

```
Lista de usuários:
ID  | Nome
--------------------
1   | Leanne Graham
2   | Ervin Howell
3   | Clementine Bauch
...

Digite o ID de um usuário para ver detalhes ou 0 para sair: 1

Detalhes do usuário:
Id: 1
Nome: Leanne Graham
Email: Sincere@april.biz

Títulos dos posts:
- sunt aut facere repellat provident occaecati excepturi optio reprehenderit
- qui est esse
- ea molestias quasi exercitationem repellat qui ipsa sit aut
...
```

## Documentação

- Biblioteca `requests`: [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)
- API JSONPlaceholder: [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
