from Requisito3 import TipoVaga, Aluno, Servidor, Visitante, Carro, Moto
from Requisito1 import Vaga, Estacionamento


def tentar_estacionar(estac, usuario):
    try:
        vaga = estac.estacionar(usuario)
    except ValueError as e:
        print(f"  [ERRO] {e}")
        return
    if vaga:
        print(f"  {usuario.nome} estacionou na {vaga}")
    else:
        print(f"  Sem vaga disponível para {usuario.nome}")


def main():
    vagas = [
        Vaga(1, TipoVaga.COMUM),
        Vaga(2, TipoVaga.COMUM),
        Vaga(3, TipoVaga.IDOSO),
        Vaga(4, TipoVaga.PCD),
        Vaga(5, TipoVaga.MOTO),
        Vaga(6, TipoVaga.ELETRICO),
    ]
    estac = Estacionamento(vagas)
    print("Vagas livres no início:", {t.value: n for t, n in estac.resumo_disponiveis().items()})

    aluno = Aluno("Ana", 20, False, Carro("ABC-1234"), ra="2345678")
    servidor = Servidor("Carlos", 45, False, Carro("DEF-5678", eletrico=True), siape="1234567")
    idoso = Servidor("Seu João", 65, False, Carro("GHI-9012"), siape="7654321")
    pcd = Aluno("Bia", 22, True, Carro("JKL-3456"), ra="8765432")
    motociclista = Aluno("Leo", 19, False, Moto("MNO-7890"), ra="1112223")
    visitante_ok = Visitante("Marta", 30, False, Carro("PQR-1111"), dias_validade=2)
    visitante_expirado = Visitante("Pedro", 35, False, Carro("STU-2222"), dias_validade=-1)

    print("\n--- Cenário normal ---")
    for u in [aluno, servidor, motociclista, pcd, idoso]:
        tentar_estacionar(estac, u)

    print("\nVagas livres agora:", {t.value: n for t, n in estac.resumo_disponiveis().items()})

    print("\n--- Visitante válido (estacionamento sem vaga comum) ---")
    tentar_estacionar(estac, visitante_ok)

    print("\n--- Visitante com cadastro expirado ---")
    tentar_estacionar(estac, visitante_expirado)

    print("\n--- Liberando a vaga 1 e tentando de novo ---")
    vagas[0].liberar()
    tentar_estacionar(estac, visitante_ok)

    print("\nEstado final:")
    for v in vagas:
        print(" ", v)


if __name__ == "__main__":
    main()