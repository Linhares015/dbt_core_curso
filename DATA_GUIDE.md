# Guia dos Dados

Todos os dados são **sintéticos** e representam o e-commerce fictício Northstar Analytics. Não há dados reais de clientes ou empresas.

## `raw_customers.csv`

**Grão:** uma linha por cliente.
**Chave:** `customer_id`.

Campos principais: nome, email, país, data de cadastro e segmento.

## `raw_orders.csv`

**Grão:** uma linha por pedido.
**Chave:** `order_id`.
**Relação:** `customer_id` aponta para cliente.

Campos principais: data, status, subtotal, desconto, frete e total.

**Regra importante:** pedidos `completed` representam receita concluída. Pedidos `pending` e `cancelled` não devem ser tratados como receita concluída.

## `raw_order_items.csv`

**Grão:** uma linha por item de um pedido.
**Chave:** `order_item_id`.
**Relações:** `order_id` aponta para pedidos; `product_id` aponta para produtos.

Campos principais: quantidade, preço unitário e desconto.

## `raw_products.csv`

**Grão:** uma linha por produto.
**Chave:** `product_id`.

Campos principais: nome, categoria, custo e preço de lista.

## Perguntas antes de modelar

1. Qual é o grão desta tabela?
2. Qual campo identifica uma linha unicamente?
3. Quais relacionamentos a tabela possui?
4. Que regra de negócio altera o significado analítico do dado?
5. Um join pode duplicar linhas? Por quê?
