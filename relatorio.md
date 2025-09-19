
# Relatório de Testes de Software

## 1. Execução dos Testes

Os testes foram executados utilizando o comando:

```bash
python -m unittest discover tests -v
````

### Resultados dos Testes

| Teste                                  | Status |
| -------------------------------------- | ------ |
| test\_integracao\_historico\_resultado | ✅ ok   |
| test\_operacoes\_sequenciais           | ✅ ok   |
| test\_consistencia\_historico          | ✅ ok   |
| test\_divisao\_por\_zero               | ✅ ok   |
| test\_entrada\_saida\_divisao          | ✅ ok   |
| test\_entrada\_saida\_multiplicacao    | ✅ ok   |
| test\_entrada\_saida\_potencia         | ✅ ok   |
| test\_entrada\_saida\_soma             | ✅ ok   |
| test\_entrada\_saida\_subtracao        | ✅ ok   |
| test\_fluxos\_divisao                  | ✅ ok   |
| test\_inicializacao                    | ✅ ok   |
| test\_limite\_inferior                 | ✅ ok   |
| test\_limite\_superior                 | ✅ ok   |
| test\_mensagens\_erro                  | ✅ ok   |
| test\_modificacao\_historico           | ✅ ok   |
| test\_potencia\_indeterminada          | ✅ ok   |
| test\_tipagem\_invalida                | ✅ ok   |

**Resumo:**

* Total de testes executados: 17
* Testes aprovados: 17
* Testes com falha: 0

Todos os testes foram aprovados com sucesso.

---

## 2. Cobertura de Código

A cobertura de código foi verificada utilizando `coverage.py` com os comandos:

```bash
coverage run -m unittest discover tests
coverage report
```

### Resultado da Cobertura

| Arquivo                   | Linhas | Linhas Perdidas | Cobertura |
| ------------------------- | ------ | --------------- | --------- |
| src/calculadora.py        | 53     | 0               | 100%      |
| tests/test\_integracao.py | 44     | 1               | 98%       |
| tests/test\_unidade.py    | 148    | 5               | 97%       |
| **Total**                 | 245    | 6               | 98%       |

A cobertura total do projeto é de **98%**.

---

## 3. Problemas Encontrados

Durante a execução dos testes **não foram encontrados problemas**.
Todos os testes passaram e a cobertura de código está alta, garantindo boa confiabilidade do software.

---

## 4. Conclusão

O software testado apresenta:

* Todas as funcionalidades testadas funcionando corretamente.
* Alta cobertura de código (98%).
* Nenhum erro crítico ou falha detectada.

O sistema pode ser considerado **estável e confiável** com base nos testes realizados.


