# dbt_core_curso — Repositório Starter do Aluno

Este é o ambiente prático do curso **dbt Core para Analistas de Dados**. Ele contém automações de ambiente, dados sintéticos, exercícios e guias — mas não contém as respostas finais do projeto.

## O que você vai construir

Você atuará como analytics engineer da empresa fictícia Northstar Analytics. A jornada transforma dados brutos de clientes, pedidos, itens de pedido e produtos em modelos de analytics testados e documentados.

## Configuração rápida

Leia o [SETUP.md](SETUP.md) para instruções de Windows, macOS e Linux.

macOS/Linux:
```bash
python3 scripts/setup_course.py --verify
```

Windows PowerShell:
```powershell
py scripts/setup_course.py --verify
```

O comando cria o ambiente local, valida a conexão dbt/DuckDB, carrega dados sintéticos e valida a estrutura inicial do projeto.

## Estrutura

- `seeds/`: dados sintéticos de entrada.
- `models/`: onde você criará staging, intermediate e marts.
- `macros/`: helpers Jinja reutilizáveis.
- `tests/`: testes de qualidade de dados.
- `exercises/`: checklist do capstone.
- `scripts/`: automação de setup e reset.
- `DATA_GUIDE.md`: grão, chaves e regras dos dados.
- `LEARNING_PATH.md`: sequência do curso e checkpoints.

## Comandos úteis

```bash
python3 scripts/setup_course.py --verify
python3 scripts/reset_course.py --reseed
.venv/bin/dbt debug --profiles-dir .
.venv/bin/dbt seed --profiles-dir .
.venv/bin/dbt parse --profiles-dir .
```

No Windows, use os scripts com `py`; o executável dbt fica em `.venv\Scripts\dbt.exe`.

## Suporte

Ao pedir ajuda, envie: sistema operacional, versão do Python, `uv --version`, comando completo e todo o texto do erro. Não envie apenas um recorte da última linha.

## Regra de aprendizado

Construa cada etapa antes de procurar a referência final. O valor do curso está em tomar decisões, testar hipóteses, errar com segurança e entender o projeto — não apenas copiar SQL.
