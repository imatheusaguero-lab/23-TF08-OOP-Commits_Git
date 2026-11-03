
class Commit:
    # O construtor recebe as informacoes de cada commit.
    # O pai e opcional, pois o primeiro commit nao possui anterior.
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Exibe o commit atual e percorre os anteriores.
    # Exemplo: commit 3 -> commit 2 -> commit 1 -> None
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        # Quando nao existir pai, a recursao termina.
        if self.pai is None:
            return

        # Pede ao commit anterior que apresente seu historico.
        self.pai.historico()


class Repositorio:
    # Inicializa o repositorio sem commits.
    # Exemplo: head = None e contador = 0
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    # Cria um commit e atualiza o HEAD.
    def commitar(self, mensagem):
        # Gera um novo identificador sequencial.
        # Exemplo: 0 -> 1 -> 2 -> 3
        self.contador += 1

        # O HEAD antigo passa a ser o pai do novo commit.
        novo_commit = Commit(
            self.contador,
            mensagem,
            self.autor,
            self.head
        )

        # O HEAD passa a apontar para o commit mais recente.
        self.head = novo_commit

    # Apresenta o historico do mais recente ao mais antigo.
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    # Conta os commits percorrendo as referencias dos pais.
    def total_de_commits(self):
        total = 0
        atual = self.head

        # Continua ate encontrar o commit sem pai.
        while atual is not None:
            total += 1
            atual = atual.pai

        return total


# Executa os testes apenas quando o arquivo for iniciado diretamente.
if __name__ == "__main__":

    # Cria um repositorio utilizando nome e RA do aluno.
    repositorio = Repositorio(
        "tf-08",
        "Matheus Aguero - 6326149"
    )

    # Testa o historico de um repositorio vazio.
    repositorio.log()

    # Simula tres commits com mensagens sobre o projeto.
    repositorio.commitar("Inicia o projeto de orientacao a objetos")
    repositorio.commitar("Implementa a estrutura de commits")
    repositorio.commitar("Adiciona controle do historico")

    # Exibe os commits do mais recente ao mais antigo.
    repositorio.log()

    # Apresenta a quantidade total de commits.
    print(repositorio.total_de_commits())


# EXECUCAO:
# python3 commit.py
