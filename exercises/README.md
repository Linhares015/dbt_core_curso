# Checklist do Exercício Capstone

## Entrega

Construa um projeto dbt documentado e testado que transforme os dados sintéticos da Northstar Analytics em modelos confiáveis de clientes, pedidos e produtos.

## Modelos obrigatórios

- Sources para os quatro arquivos brutos.
- Modelos staging para clientes, pedidos, itens de pedido e produtos.
- Modelo intermediate que centraliza enriquecimento de pedidos.
- `dim_customers`.
- `fct_orders`.
- Um mart de valor do cliente.
- Um mart de receita/produto.

## Qualidade obrigatória

- Chaves importantes com `not_null` e `unique`.
- Relações principais com testes de relacionamento.
- Status de pedido com valores aceitos.
- Pelo menos uma regra de negócio em teste SQL customizado.
- Modelos e colunas importantes documentados.

## Critério de aceite

Em um checkout limpo, o projeto deve configurar, carregar seeds, executar modelos/testes e gerar documentação sem erros esperados. Explique o grão de cada mart e as regras de negócio aplicadas.

## Regra

Não procure a solução antes de tentar. Use o erro, o guia de dados e os checkpoints como material de aprendizagem.
