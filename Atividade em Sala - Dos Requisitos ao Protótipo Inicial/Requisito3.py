from abc import ABC
from datetime import date, timedelta
from enum import Enum


class TipoVaga(Enum):
    COMUM = "comum"
    IDOSO = "idoso"
    PCD = "pcd"
    MOTO = "moto"
    ELETRICO = "eletrico"


# ---------- Veículos ----------
class Veiculo(ABC):
    def __init__(self, placa: str):
        self.placa = placa

    def tipos_vaga_compativeis(self) -> set[TipoVaga]:
        raise NotImplementedError


class Carro(Veiculo):
    def __init__(self, placa: str, eletrico: bool = False):
        super().__init__(placa)
        self.eletrico = eletrico

    def tipos_vaga_compativeis(self) -> set[TipoVaga]:
        tipos = {TipoVaga.COMUM}
        if self.eletrico:
            tipos.add(TipoVaga.ELETRICO)
        return tipos


class Moto(Veiculo):
    def tipos_vaga_compativeis(self) -> set[TipoVaga]:
        return {TipoVaga.MOTO}


# ---------- Usuários ----------
class Usuario(ABC):
    def __init__(self, nome: str, idade: int, pcd: bool, veiculo: Veiculo):
        self.nome = nome
        self.idade = idade
        self.pcd = pcd
        self.veiculo = veiculo

    def cadastro_valido(self) -> bool:
        return True

    def vagas_permitidas(self) -> set[TipoVaga]:
        """Interseção entre o que o veículo aceita e o que o usuário tem direito."""
        tipos = set(self.veiculo.tipos_vaga_compativeis())
        if isinstance(self.veiculo, Carro):  # vagas especiais valem para carro
            if self.idade >= 60:
                tipos.add(TipoVaga.IDOSO)
            if self.pcd:
                tipos.add(TipoVaga.PCD)
        return tipos


class Aluno(Usuario):
    def __init__(self, nome, idade, pcd, veiculo, ra: str):
        super().__init__(nome, idade, pcd, veiculo)
        self.ra = ra


class Servidor(Usuario):
    def __init__(self, nome, idade, pcd, veiculo, siape: str):
        super().__init__(nome, idade, pcd, veiculo)
        self.siape = siape

## criou uma restrição para o usuário ser temporario
class Visitante(Usuario):
    def __init__(self, nome, idade, pcd, veiculo, dias_validade: int = 1):
        super().__init__(nome, idade, pcd, veiculo)
        self.validade = date.today() + timedelta(days=dias_validade)

    def cadastro_valido(self) -> bool:
        return date.today() <= self.validade