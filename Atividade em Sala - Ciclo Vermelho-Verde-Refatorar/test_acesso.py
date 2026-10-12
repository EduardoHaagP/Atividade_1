# PLANO
# Componente: ControleDeAcesso.pode_estacionar(usuario, vaga) -> bool
# Origem: e-mail do cliente ("alunos às vezes estacionam em vagas
# reservadas para funcionários").
#
# Casos de teste (3 variações de comportamento):
#  1. Aluno: pode em vaga COMUM; NÃO pode em vaga RESERVADA_SERVIDOR
#  2. Servidor: pode em vaga COMUM e em vaga RESERVADA_SERVIDOR
#  3. Visitante: pode só em vaga COMUM e só com cadastro válido;
#     cadastro expirado é negado em qualquer vaga
#
# Padrão de projeto: Strategy
#  - Contexto: ControleDeAcesso
#  - Estratégia (interface): PoliticaDeAcesso
#  - Estratégias concretas: PoliticaAluno, PoliticaServidor, PoliticaVisitante
#  Por quê: cada tipo de usuário tem sua regra de acesso, e o Strategy
#  evita um if/elif que cresce a cada novo tipo de usuário.
#
# Tempo: Red 15 min | Green 10 min (marco dos 25 min) |
#        Refactor 40 min | conferência e autoavaliação 35 min
#
# IA: usei IA para gerar o código deste arquivo de testes a partir da tabela
#     de casos que defini acima. A implementação (green) e a refatoração
#     (Strategy) eu escrevo por conta própria.

from acesso import ControleDeAcesso, Usuario, Vaga


# ---------- Variação 1: Aluno ----------

def test_aluno_em_vaga_comum_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("aluno")
    vaga = Vaga("comum")
    assert controle.pode_estacionar(usuario, vaga) is True


def test_aluno_em_vaga_reservada_servidor_nao_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("aluno")
    vaga = Vaga("reservada_servidor")
    assert controle.pode_estacionar(usuario, vaga) is False


# ---------- Variação 2: Servidor ----------

def test_servidor_em_vaga_comum_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("servidor")
    vaga = Vaga("comum")
    assert controle.pode_estacionar(usuario, vaga) is True


def test_servidor_em_vaga_reservada_servidor_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("servidor")
    vaga = Vaga("reservada_servidor")
    assert controle.pode_estacionar(usuario, vaga) is True


# ---------- Variação 3: Visitante ----------

def test_visitante_valido_em_vaga_comum_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("visitante", cadastro_valido=True)
    vaga = Vaga("comum")
    assert controle.pode_estacionar(usuario, vaga) is True


def test_visitante_valido_em_vaga_reservada_nao_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("visitante", cadastro_valido=True)
    vaga = Vaga("reservada_servidor")
    assert controle.pode_estacionar(usuario, vaga) is False


def test_visitante_expirado_em_vaga_comum_nao_pode():
    controle = ControleDeAcesso()
    usuario = Usuario("visitante", cadastro_valido=False)
    vaga = Vaga("comum")
    assert controle.pode_estacionar(usuario, vaga) is False