from enum import Enum


class TipoVaga(Enum):
    COMUM = "comum"
    IDOSO = "idoso"
    PCD = "pcd"
    MOTO = "moto"
    ELETRICO = "eletrico"


class Vaga:
    def __init__(self, numero: int, tipo: TipoVaga):
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            raise ValueError(f"Vaga {self.numero} já está ocupada")
        self.ocupada = True

    def liberar(self):
        self.ocupada = False

    def __repr__(self):
        estado = "ocupada" if self.ocupada else "livre"
        return f"Vaga({self.numero}, {self.tipo.value}, {estado})"


class Estacionamento:
    def __init__(self, vagas: list[Vaga]):
        self.vagas = vagas

    def vagas_disponiveis(self, tipo: TipoVaga | None = None) -> list[Vaga]:
        """Retorna as vagas livres, opcionalmente filtrando por tipo."""
        return [
            v for v in self.vagas
            if not v.ocupada and (tipo is None or v.tipo == tipo)
        ]

    def resumo_disponiveis(self) -> dict[TipoVaga, int]:
        """Quantidade de vagas livres por tipo."""
        resumo = {}
        for v in self.vagas_disponiveis():
            resumo[v.tipo] = resumo.get(v.tipo, 0) + 1
        return resumo

    def estacionar(self, tipo: TipoVaga) -> Vaga | None:
        """Ocupa a primeira vaga livre do tipo pedido, ou retorna None."""
        livres = self.vagas_disponiveis(tipo)
        if not livres:
            return None
        vaga = livres[0]
        vaga.ocupar()
        return vaga