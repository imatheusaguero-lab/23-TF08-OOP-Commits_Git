# TF08 — Programação Orientada a Objetos: Histórico de Commits

Projeto desenvolvido para a **Aula 08 de Engenharia de Software**, com o objetivo de representar um histórico de commits do Git utilizando **programação orientada a objetos (POO)** em Python.

O programa simula um repositório em memória. Cada commit armazena seus próprios dados e uma referência ao commit anterior, formando uma cadeia que pode ser percorrida do mais recente ao mais antigo.

## Objetivos de aprendizagem

- Criar classes e instanciar objetos em Python.
- Utilizar o construtor `__init__` e o parâmetro `self`.
- Trabalhar com atributos que guardam referências a outros objetos.
- Aplicar recursividade para exibir um histórico.
- Utilizar `while` para contar os commits existentes.
- Diferenciar um simulador de commits dos commits reais registrados pelo Git.

## Estrutura do projeto

```text
tf-08/
├── .git/           # Histórico real do Git (diretório oculto)
├── .venv/          # Ambiente virtual local (ignorado pelo Git)
├── .gitignore      # Arquivos e pastas que o Git não deve rastrear
├── commit.py       # Classes e execução de exemplo
└── README.md       # Documentação do projeto
```

> O nome da pasta local pode ser diferente de `tf-08`. O importante é executar os comandos dentro da pasta que contém `commit.py`.

## Como funciona

O projeto possui duas classes, definidas no arquivo `commit.py`.

### Classe `Commit`

Representa **um commit individual**. Seu construtor recebe quatro informações:

| Atributo | Descrição |
| --- | --- |
| `id` | Identificador numérico sequencial, como `1`, `2` ou `3`. |
| `mensagem` | Descrição da alteração representada pelo commit. |
| `autor` | Nome e RA de quem realizou o commit simulado. |
| `pai` | Referência ao commit anterior; será `None` no primeiro commit. |

O método `historico()` imprime o commit atual no formato:

```text
#3 Adiciona controle do historico (Matheus Aguero - 6326149)
```

Em seguida, chama `historico()` do seu `pai`. A recursão termina quando o commit não possui pai (`None`).

### Classe `Repositorio`

Representa **um repositório simulado** e administra a sequência de commits.

| Atributo ou método | Responsabilidade |
| --- | --- |
| `nome` | Guarda o nome do repositório. |
| `autor` | Identifica o autor usado nos novos commits. |
| `head` | Aponta para o commit mais recente; começa em `None`. |
| `contador` | Controla o próximo identificador, iniciando em `0`. |
| `commitar(mensagem)` | Incrementa o contador, cria um novo `Commit` com o `head` anterior como pai e atualiza o `head`. |
| `log()` | Exibe `Nenhum commit ainda` se o histórico estiver vazio; caso contrário, inicia a impressão a partir do `head`. |
| `total_de_commits()` | Conta os commits percorrendo a cadeia de pais com um `while`, sem depender do contador. |

### Relação entre os objetos

Após criar três commits, as referências ficam assim:

```text
Repositorio.head
      |
      v
Commit #3 ──pai──> Commit #2 ──pai──> Commit #1 ──pai──> None
  (novo)                                          (primeiro)
```

Ao chamar `repositorio.log()`, a impressão segue essa cadeia: **#3 → #2 → #1**. Ao chamar `repositorio.total_de_commits()`, o laço também caminha de pai em pai e retorna `3`.

## Requisitos

- **WSL com Linux** para desenvolver e executar o trabalho, conforme a atividade.
- **Python 3** com suporte ao módulo `venv`.
- **Git**, para versionar e publicar o projeto.

Não há bibliotecas externas nem instruções `import` no código.

## Como executar

Abra o terminal do **WSL**, entre na pasta do projeto e ative o ambiente virtual:

```bash
cd /mnt/d/OneDrive/Documentos/05-Faculdade/04-ADS-UNIFAAT/23-Engenharia_de_Software/23-TF08-OOP-Commits_Git
source .venv/bin/activate
python3 commit.py
```

Se o ambiente virtual ainda não existir, crie-o antes:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> O caminho acima corresponde à pasta do projeto mostrada no terminal do Windows. Se você mover a pasta, ajuste o caminho. O programa não requer instalar pacotes adicionais.

### Exemplo de saída

Com as mensagens de teste exemplificadas no projeto:

```text
Nenhum commit ainda
#3 Adiciona controle do historico (Matheus Aguero - 6326149)
#2 Implementa a estrutura de commits (Matheus Aguero - 6326149)
#1 Inicia o projeto de orientacao a objetos (Matheus Aguero - 6326149)
3
```

A saída exata dependerá das mensagens e do autor definidos no trecho de teste de `commit.py`.

## Exemplo de uso das classes

No final de `commit.py`, o bloco de teste pode criar um repositório, registrar commits e consultar o histórico:

```python
if __name__ == "__main__":
    repositorio = Repositorio("tf-08", "Matheus Aguero - 6326149")

    repositorio.log()
    repositorio.commitar("Cria estrutura inicial")
    repositorio.commitar("Organiza as classes")

    repositorio.log()
    print("Total:", repositorio.total_de_commits())
```

**Resultado esperado desse exemplo:**

```text
Nenhum commit ainda
#2 Organiza as classes (Matheus Aguero - 6326149)
#1 Cria estrutura inicial (Matheus Aguero - 6326149)
Total: 2
```

O bloco `if __name__ == "__main__":` executa os testes somente quando `commit.py` é iniciado diretamente, sem alterar as classes.

## Regras atendidas pela implementação

- Uso de classes `Commit` e `Repositorio`, sem bibliotecas importadas.
- Identificadores numéricos atribuídos pelo repositório.
- Histórico exibido por chamadas recursivas aos commits anteriores.
- Total calculado percorrendo os objetos com `while`.
- Ausência de `else` e `elif`.
- Nomes de métodos e variáveis descritivos.
- Comentários explicativos no código.

## Versionamento com Git

A atividade solicita **pelo menos três commits reais**, realizados progressivamente:

```bash
# 1. Depois de criar a classe Commit
git add .
git commit -m "Cria a classe Commit"

# 2. Depois de adicionar a classe Repositorio
git add .
git commit -m "Cria a classe Repositorio"

# 3. Depois de adicionar o teste
git add .
git commit -m "Testa o repositorio de commits"
```

Confira o histórico real do projeto:

```bash
git log --oneline
```

E os arquivos rastreados:

```bash
git ls-files
```

O `.gitignore` deve conter:

```gitignore
.venv/
__pycache__/
```

A pasta `.venv` **não deve ser enviada ao GitHub**. Após adicionar este README, ele pode ser registrado em um commit adicional:

```bash
git add README.md
git commit -m "Documenta o projeto TF08"
git push
```

> **Importante:** `repositorio.commitar()` cria objetos em memória dentro do programa. Já `git commit` é o comando real do Git, que registra alterações no histórico do repositório. São operações diferentes.

## Identificação acadêmica

- **Disciplina:** Engenharia de Software — TF08 (OOP)
- **Instituição:** UniFAAT
- **Aluno:** Matheus Aguero
- **RA:** 6326149

---

Este projeto tem finalidade didática: demonstra a estrutura de referências entre objetos e o percurso recursivo de um histórico simplificado de commits.
