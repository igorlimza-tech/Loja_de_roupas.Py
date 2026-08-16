# 👕 Loja de Roupas.py

> Sistema de gerenciamento de uma loja de roupas desenvolvido em **Python**, com foco em **Programação Orientada a Objetos (POO), modularização, validação de dados e organização de código**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📌 Sobre o projeto

O **Loja de Roupas.py** é um sistema desenvolvido em Python que simula operações básicas de gerenciamento de uma loja através do terminal.

O projeto foi criado como parte da minha evolução nos estudos de **Python e Programação Orientada a Objetos**, colocando em prática conceitos como classes, objetos, métodos, funções, modularização, validação de dados, tratamento de erros e separação de responsabilidades.

O sistema permite gerenciar clientes e produtos, controlar o estoque, montar carrinhos com múltiplos itens e registrar vendas.

Atualmente, os dados são mantidos em memória durante a execução do programa. A persistência dos dados será implementada futuramente através da integração com banco de dados.

---

## ⚙️ Funcionalidades

### 👤 Gerenciamento de clientes

- Cadastro de clientes
- Validação de CPF
- Verificação de CPF já cadastrado
- Validação de nome
- Validação de telefone
- Registro e validação da data de nascimento
- Listagem de clientes

### 👕 Gerenciamento de produtos

- Cadastro de produtos
- Validação de código de barras
- Verificação de código de barras duplicado
- Cadastro de nome, preço e quantidade
- Listagem do estoque
- Busca de produtos por código de barras
- Busca de produtos por nome
- Busca parcial por nome
- Seleção entre múltiplos produtos encontrados
- Reposição de estoque
- Alteração do preço do produto

### 🔎 Busca de produtos

Durante uma venda ou operação de gerenciamento, o sistema permite escolher entre:

```text
1- Buscar por nome
2- Buscar por código
```

Na busca por nome, não é necessário informar o nome completo.

Por exemplo, pesquisando:

```text
camisa
```

o sistema pode apresentar:

```text
1 - Camisa Social
2 - Camisa Polo
3 - Camisa Esportiva
```

O usuário pode então selecionar o produto desejado.

### 🛒 Carrinho e vendas

- Identificação do cliente através do CPF
- Carrinho com múltiplos produtos
- Adição de diferentes produtos na mesma venda
- Controle de produtos repetidos no carrinho
- Atualização da quantidade de um produto já adicionado
- Verificação do estoque disponível
- Bloqueio de quantidades superiores ao estoque
- Cálculo automático do subtotal
- Cálculo do valor total da compra
- Atualização automática do estoque após a venda
- Registro da forma de pagamento
- Registro automático da data e hora da compra
- Histórico das vendas realizadas

### 💰 Histórico de preços

O sistema preserva o **preço praticado no momento da venda**.

Isso significa que, caso o preço de um produto seja alterado posteriormente, as vendas anteriores continuam exibindo o valor que foi utilizado quando aquela venda aconteceu.

Exemplo:

```text
Venda realizada:
Camisa - R$ 50,00

Preço alterado posteriormente:
Camisa - R$ 65,00

Histórico da venda:
Camisa - R$ 50,00
```

### 📦 Gerenciamento de estoque

O sistema possui um submenu específico para gerenciamento:

```text
=== GERENCIAMENTO DO ESTOQUE ===
1- Adicionar produtos ao estoque
2- Alterar valor do produto
3- Voltar ao menu principal
```

As operações utilizam a mesma busca por **nome ou código de barras** disponível durante as vendas.

### 💳 Formas de pagamento

- Dinheiro
- Cartão de débito
- Cartão de crédito
- Pix

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento foram utilizados diversos conceitos da linguagem Python:

- **Programação Orientada a Objetos (POO)**
- Classes e objetos
- Construtores (`__init__`)
- Atributos
- Métodos
- Funções
- Modularização
- Listas
- Dicionários
- Iteração
- `enumerate()`
- Estruturas condicionais
- Estruturas de repetição
- Tratamento de exceções
- Validação de dados
- Busca de objetos
- Manipulação de strings
- Uso de `datetime`
- Separação de responsabilidades
- Reutilização de código
- Refatoração

---

## 🏗️ Estrutura do projeto

```text
Loja_de_roupas.Py/
│
├── main.py
├── clientes.py
├── produtos.py
├── vendas.py
├── utilidades.py
└── README.md
```

### `main.py`

Responsável pelo fluxo principal da aplicação, menu principal e submenu de gerenciamento do estoque.

O programa é iniciado através de:

```python
if __name__ == "__main__":
    main()
```

### `clientes.py`

Contém a classe `Cliente` e as funcionalidades relacionadas ao cadastro, busca e listagem dos clientes.

### `produtos.py`

Contém a classe `Produto` e as funcionalidades relacionadas ao cadastro, busca e gerenciamento dos produtos e estoque.

Também centraliza a seleção de produtos através da função:

```python
selecionar_produto()
```

permitindo reutilizar a mesma lógica de busca em diferentes partes do sistema.

### `vendas.py`

Contém a classe `Venda` e é responsável por:

- montagem do carrinho;
- cálculo dos valores;
- formas de pagamento;
- atualização do estoque;
- registro das vendas;
- histórico de vendas.

### `utilidades.py`

Centraliza funções reutilizáveis de leitura, validação e apoio ao sistema:

```text
ler_int()
ler_float()
validar_cpf()
ler_cpf()
ler_nome()
ler_nome_produto()
ler_codigo()
ler_telefone()
ler_sim_nao()
ler_data()
linha()
pausar()
```

---

## 🔐 Validação de dados

### CPF

A validação realiza:

- remoção da formatação;
- verificação da quantidade de dígitos;
- verificação de caracteres numéricos;
- bloqueio de CPFs com todos os dígitos iguais;
- cálculo do primeiro dígito verificador;
- cálculo do segundo dígito verificador.

### 📅 Data de nascimento

A data é informada no formato:

```text
DD/MM/AAAA
```

O sistema utiliza `datetime.strptime()` para verificar se a data realmente existe.

Exemplos:

```text
15/08/2002 → válido
31/02/2002 → inválido
```

Internamente, a data é armazenada como um objeto `date`.

### 📞 Telefone

São aceitos telefones com **10 ou 11 dígitos**.

Exemplos:

```text
(11) 99999-9999
11 99999-9999
11999999999
```

A formatação é removida antes da validação.

### 🏷️ Código de barras

O código deve:

- conter somente números;
- possuir tamanho compatível com os formatos aceitos pelo sistema.

São aceitos códigos com:

```text
8, 12, 13 ou 14 dígitos
```

---

## 🖥️ Menu principal

```text
========== LOJA DE ROUPAS.PY ==========
1- Cadastrar cliente
2- Listar clientes
3- Cadastrar produto
4- Listar estoque
5- Realizar venda
6- Listar vendas
7- Gerenciamento do estoque
8- Sair do Programa
```

---

## 🔄 Fluxo básico

```text
                    ┌──────────────┐
                    │   main.py    │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        ┌─────────┐   ┌─────────┐   ┌─────────┐
        │Clientes │   │Produtos │   │ Vendas  │
        └────┬────┘   └────┬────┘   └────┬────┘
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    ┌──────────────┐
                    │utilidades.py │
                    └──────────────┘
```

A divisão em módulos permite separar as responsabilidades do sistema e evita concentrar toda a lógica em um único arquivo.

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.x
- Git

### Clone o repositório

```bash
git clone https://github.com/igorlimza-tech/Loja_de_roupas.Py.git
```

### Entre na pasta

```bash
cd Loja_de_roupas.Py
```

### Execute

```bash
python main.py
```

---

## 🚀 Roadmap

### Versão 1.0

- [x] Cadastro de clientes
- [x] Validação de CPF
- [x] Validação de nome
- [x] Validação de telefone
- [x] Validação de data de nascimento
- [x] Cadastro de produtos
- [x] Validação de código de barras
- [x] Controle de estoque
- [x] Reposição de estoque
- [x] Alteração de preço
- [x] Busca de produtos por nome
- [x] Busca de produtos por código
- [x] Carrinho com múltiplos produtos
- [x] Registro de vendas
- [x] Histórico de preços das vendas
- [x] Registro de data e hora
- [x] Formas de pagamento
- [x] Organização em módulos
- [x] Programação Orientada a Objetos

### 🔮 Próximas versões

- [ ] Persistência de dados
- [ ] Integração com MySQL
- [ ] Alteração de dados dos clientes
- [ ] Exclusão de clientes
- [ ] Alteração do nome de produtos
- [ ] Exclusão de produtos
- [ ] Preservação do nome histórico do produto nas vendas
- [ ] Testes automatizados
- [ ] Relatórios de vendas
- [ ] Melhorias na interface do terminal

---

## 📚 Aprendizados

Este projeto representa uma aplicação prática dos conhecimentos adquiridos durante meus estudos de Python.

Ao longo do desenvolvimento, foram trabalhados principalmente:

- organização de projetos;
- Programação Orientada a Objetos;
- separação de responsabilidades;
- reutilização de código;
- refatoração;
- tratamento de erros;
- validação de entradas;
- manipulação de datas;
- modelagem de regras de negócio;
- controle de estoque;
- construção de carrinho de compras;
- controle de versões com Git e GitHub;
- evolução incremental de software.

Uma das principais evoluções durante o desenvolvimento foi a refatoração da seleção de produtos.

A lógica de busca, que inicialmente estava diretamente dentro do fluxo de vendas, foi separada em uma função reutilizável:

```python
selecionar_produto()
```

Essa função passou a ser utilizada tanto nas vendas quanto nas operações de gerenciamento do estoque, reduzindo duplicação de código.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
| --- | --- |
| 🐍 Python | Desenvolvimento da aplicação |
| 📦 Git | Controle de versão |
| 🐙 GitHub | Hospedagem e versionamento do projeto |

---

## 👨‍💻 Autor

**Igor Lima**

Estudante de **Análise e Desenvolvimento de Sistemas**, aprofundando conhecimentos em **Python, Programação Orientada a Objetos, bancos de dados e desenvolvimento de software**.

Este projeto representa parte da minha evolução prática na área de desenvolvimento.

---

⭐ **Se este projeto foi útil ou interessante para você, considere deixar uma estrela no repositório!**