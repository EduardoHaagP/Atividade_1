class Vaga:
    def __init__(self, tipo):
        self.tipo = tipo  # "comum" ou "reservada_servidor"


class Usuario:
    def __init__(self, tipo, cadastro_valido=True):
        self.tipo = tipo  # "aluno", "servidor" ou "visitante"
        self.cadastro_valido = cadastro_valido


class ControleDeAcesso:
    def pode_estacionar(self, usuario, vaga):
        if usuario.tipo == "aluno":
            return vaga.tipo == "comum"
        elif usuario.tipo == "servidor":
            return True
        elif usuario.tipo == "visitante":
            return usuario.cadastro_valido and vaga.tipo == "comum"
        return False