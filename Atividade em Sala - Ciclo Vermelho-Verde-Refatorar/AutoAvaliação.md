
---------------------------------------------------------------------------
SAÍDA DO PYTEST (pytest -v, após a refatoração)
test_acesso.py::test_aluno_em_vaga_comum_pode PASSED                     [ 14%]
test_acesso.py::test_aluno_em_vaga_reservada_servidor_nao_pode PASSED    [ 28%]
test_acesso.py::test_servidor_em_vaga_comum_pode PASSED                  [ 42%]
test_acesso.py::test_servidor_em_vaga_reservada_servidor_pode PASSED     [ 57%]
test_acesso.py::test_visitante_valido_em_vaga_comum_pode PASSED          [ 71%]
test_acesso.py::test_visitante_valido_em_vaga_reservada_nao_pode PASSED  [ 85%]
test_acesso.py::test_visitante_expirado_em_vaga_comum_nao_pode PASSED    [100%]
============================== 7 passed in 0.03s ===============================

AUTOAVALIAÇÃO
Critérios atingidos:
 1. Testes em arquivo separado (test_acesso.py), com testes para as 3 variações.
 2. Histórico com três commits: red, green e refactor.
 3. O commit red contém só os testes, sem a implementação.
 4. Strategy aplicado e nomeado no topo do arquivo, com os participantes
    do domínio (Contexto, Estratégia e Estratégias concretas).
 5. Os 7 testes passam depois da refatoração (saída acima).
Critérios não atingidos: nenhum.

O que mudou entre o verde e o refatorado:
 No verde, ControleDeAcesso.pode_estacionar tinha um if/elif com a regra de
 cada tipo de usuário. No refatorado, cada regra virou uma classe
 (PoliticaAluno, PoliticaServidor, PoliticaVisitante) que implementa
 PoliticaDeAcesso, e o ControleDeAcesso apenas escolhe a política pelo tipo
 do usuário e delega. Um novo tipo de usuário agora é uma nova classe, sem
 mexer no ControleDeAcesso. O comportamento observável não mudou.

Qual parte deu mais trabalho: Tive um pouco de dificuldade de realmente entender o que era pra fazer, no chat da IA tem uns 4/5 prompts que me ajudaram a entender

Uso de IA: Usei a IA para entender o projeto e gerar os códigos dos testes (a partir da tabela de casos que
defini), o green e a refatoração. Ajudou a ter um ciclo completo rápido e a entender o Strategy. 