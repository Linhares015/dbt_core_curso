# Caminho de Aprendizagem

Siga o curso em sequência. Cada marco representa uma evolução do projeto Northstar Analytics.

## 1. Ambiente e dados brutos

- Rode `python3 scripts/setup_course.py --verify` (Windows: `py`).
- Entenda `DATA_GUIDE.md`.
- Identifique grão, chaves e status dos quatro datasets.

## 2. Sources e staging

- Declare sources em YAML.
- Crie modelos staging limpos.
- Use `ref()` para dependências.

## 3. Modelagem em camadas

- Crie um modelo intermediate para regras de negócio.
- Crie dimensão de clientes e fato de pedidos.
- Construa marts de cliente e produto/receita.

## 4. Qualidade e documentação

- Adicione testes genéricos e customizados.
- Documente modelos e colunas.
- Gere documentação e navegue o lineage.

## 5. Execução e depuração

- Escolha entre `run`, `test` e `build`.
- Rode subconjuntos de modelos.
- Isole e corrija erros de SQL, configuração e qualidade.

## 6. Capstone

- Entregue o projeto documentado, testado e reproduzível.
- Valide em ambiente limpo.
- Explique decisões, trade-offs e próximos passos.

## Checkpoint inicial

Antes de avançar, confirme `dbt debug`, `dbt seed` e `dbt parse` funcionando e explique o grão de cada seed.
