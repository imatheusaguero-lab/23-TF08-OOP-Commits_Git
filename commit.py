
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
