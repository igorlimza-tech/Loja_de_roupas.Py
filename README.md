# 👕 Loja de Roupas

> Sistema de gerenciamento de uma loja de roupas desenvolvido em **Python**, com foco em **Programação Orientada a Objetos, modularização, validação de dados e boas práticas de desenvolvimento**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 📌 Sobre o projeto

O **Loja de Roupas** é um sistema desenvolvido em Python para simular operações básicas de uma loja através do terminal.

O projeto foi criado como parte da minha evolução nos estudos de **Python e Programação Orientada a Objetos**, permitindo colocar em prática conceitos como classes, objetos, métodos, funções, modularização, validação de dados e organização de código.

O desenvolvimento está sendo realizado de forma incremental, adicionando novas funcionalidades e aprimorando a estrutura do sistema conforme avanço nos estudos.

---

## ⚙️ Funcionalidades

### 👤 Gerenciamento de clientes

* Cadastro de clientes
* Validação de CPF
* Validação de nome
* Validação de telefone
* Verificação de CPF já cadastrado
* Listagem de clientes

### 👕 Gerenciamento de produtos

* Cadastro de produtos
* Código de barras
* Nome do produto
* Valor
* Quantidade em estoque
* Verificação de código de barras duplicado
* Listagem do estoque

### 🛒 Gerenciamento de vendas

* Identificação do cliente por CPF
* Identificação do produto por código de barras
* Definição da quantidade de produtos
* Verificação de estoque disponível
* Atualização automática do estoque
* Cálculo do valor total
* Registro da forma de pagamento
* Listagem das vendas realizadas

### 💳 Formas de pagamento

* Dinheiro
* Cartão de débito
* Cartão de crédito
* Pix

---

## 🧠 Conceitos aplicados

O desenvolvimento do projeto permite praticar diferentes conceitos da linguagem Python:

* **Programação Orientada a Objetos (POO)**
* Classes e objetos
* Construtores (`__init__`)
* Atributos e métodos
* Funções
* Modularização
* Listas e iteração
* Estruturas condicionais
* Estruturas de repetição
* Tratamento de exceções
* Validação de dados
* Busca de objetos
* Organização de responsabilidades entre módulos

---

## 🏗️ Estrutura do projeto

```text
Loja-de-Roupas/
│
├── main.py
├── clientes.py
├── produtos.py
├── vendas.py
├── utilidades.py
└── README.md
```

### `main.py`

Responsável pelo fluxo principal da aplicação e pelo menu de interação com o usuário.

### `clientes.py`

Responsável pelo gerenciamento dos clientes e contém a classe `Cliente`.

### `produtos.py`

Responsável pelo gerenciamento dos produtos e do estoque, contendo a classe `Produto`.

### `vendas.py`

Responsável pelo registro das vendas e contém a classe `Venda`.

### `utilidades.py`

Centraliza funções reutilizáveis para entrada e validação de dados:

```text
ler_int()
ler_float()
ler_cpf()
ler_nome()
ler_telefone()
```

---

## 🔐 Validação de dados

Uma das partes trabalhadas no projeto é a criação de funções específicas para validar entradas fornecidas pelo usuário.

### CPF

A validação realiza:

* Limpeza da formatação;
* Verificação da quantidade de dígitos;
* Verificação se contém apenas números;
* Bloqueio de CPFs com todos os dígitos iguais;
* Cálculo e validação dos dois dígitos verificadores.

### Nome

A função `ler_nome()` verifica se:

* O campo não está vazio;
* O nome contém apenas letras e espaços;
* Caracteres acentuados são aceitos.

### Telefone

A função `ler_telefone()` aceita telefones com **10 ou 11 dígitos** e permite que o usuário informe formatos como:

```text
(11) 99999-9999
11 99999-9999
11999999999
```

A formatação é removida antes da validação.

---

## 🖥️ Funcionamento

O sistema utiliza uma interface simples através do terminal.

```text
========== LOJA DE ROUPAS.PY ==========
1- Cadastrar cliente
2- Listar clientes
3- Cadastrar produto
4- Listar estoque
5- Realizar venda
6- Listar vendas
7- Sair do Programa
```

O usuário escolhe uma opção e o sistema executa a operação correspondente.

---

## 🔄 Fluxo básico

```text
              ┌──────────────┐
              │    main.py   │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
     ┌─────────┐ ┌─────────┐ ┌─────────┐
     │Clientes │ │Produtos │ │ Vendas  │
     └────┬────┘ └────┬────┘ └────┬────┘
          │           │           │
          └───────────┼───────────┘
                      ▼
              ┌──────────────┐
              │ utilidades.py│
              └──────────────┘
```

A ideia é separar as responsabilidades do sistema em diferentes módulos, evitando concentrar toda a lógica em um único arquivo.

---

## ▶️ Como executar

### Pré-requisitos

* Python 3.x
* Git

### Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### Acesse a pasta

```bash
cd Loja-de-Roupas
```

### Execute o programa

```bash
python main.py
```

---

## 🚀 Roadmap

O projeto continuará evoluindo conforme novos conceitos forem estudados.

### Atualmente

* [x] Cadastro de clientes
* [x] Validação de CPF
* [x] Validação de nome
* [x] Validação de telefone
* [x] Cadastro de produtos
* [x] Controle de estoque
* [x] Registro de vendas
* [x] Formas de pagamento
* [x] Organização em módulos
* [x] Programação Orientada a Objetos

### Próximas etapas

* [ ] Melhorar as validações
* [ ] Implementar edição de clientes
* [ ] Implementar exclusão de clientes
* [ ] Implementar edição de produtos
* [ ] Implementar exclusão de produtos
* [ ] Adicionar persistência de dados
* [ ] Integrar com MySQL
* [ ] Implementar testes automatizados
* [ ] Adicionar relatórios de vendas
* [ ] Melhorar a interface do sistema

---

## 📚 Aprendizados

Este projeto está sendo utilizado como uma aplicação prática dos conhecimentos adquiridos durante meus estudos de Python.

Além de desenvolver funcionalidades, o projeto também tem como objetivo praticar:

* Organização de projetos;
* Separação de responsabilidades;
* Reutilização de código;
* Tratamento de erros;
* Validação de entradas;
* Controle de versões com Git;
* Evolução incremental de software.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização                            |
| ---------- | ------------------------------------- |
| 🐍 Python  | Desenvolvimento da aplicação          |
| 📦 Git     | Controle de versão                    |
| 🐙 GitHub  | Versionamento e hospedagem do projeto |

---

## 👨‍💻 Autor

**Igor Lima**

Estudante de **Análise e Desenvolvimento de Sistemas**, atualmente aprofundando meus conhecimentos em **Python, Programação Orientada a Objetos, bancos de dados e desenvolvimento de software**.

Este projeto representa parte da minha evolução prática na área de desenvolvimento.

---

⭐ **Se este projeto foi útil ou interessante para você, considere deixar uma estrela no repositório!**
