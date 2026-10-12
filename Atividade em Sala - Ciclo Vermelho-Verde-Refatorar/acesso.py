# Padrão de projeto aplicado: Strategy
#  - Contexto: ControleDeAcesso (escolhe a política pelo tipo do usuário e delega)
#  - Estratégia (interface): PoliticaDeAcesso
#  - Estratégias concretas: PoliticaAluno, PoliticaServidor, PoliticaVisitante


class Vaga:
    def __init__(self, tipo):
        self.tipo = tipo  # "comum" ou "reservada_servidor"


class Usuario:
    def __init__(self, tipo, cadastro_valido=True):
        self.tipo = tipo  # "aluno", "servidor" ou "visitante"
        self.cadastro_valido = cadastro_valido


class PoliticaDeAcesso:
    """Estratégia (interface): decide se um usuário pode ocupar uma vaga."""

    def permite(self, usuario, vaga):
        raise NotImplementedError


class PoliticaAluno(PoliticaDeAcesso):
    def permite(self, usuario, vaga):
        return vaga.tipo == "comum"


class PoliticaServidor(PoliticaDeAcesso):
    def permite(self, usuario, vaga):
        return vaga.tipo in ("comum", "reservada_servidor")


class PoliticaVisitante(PoliticaDeAcesso):
    def permite(self, usuario, vaga):
        return usuario.cadastro_valido and vaga.tipo == "comum"


class ControleDeAcesso:
    """Contexto: delega a decisão à política do tipo do usuário."""

    def __init__(self):
        self._politicas = {
            "aluno": PoliticaAluno(),
            "servidor": PoliticaServidor(),
            "visitante": PoliticaVisitante(),
        }

    def pode_estacionar(self, usuario, vaga):
        politica = self._politicas.get(usuario.tipo)
        if politica is None:
            return False  # tipo de usuário desconhecido é negado
        return politica.permite(usuario, vaga)
