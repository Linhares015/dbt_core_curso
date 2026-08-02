# Guia de Configuração

O curso usa **dbt Core + DuckDB localmente**. Você não precisa de conta cloud, senha de banco, API key ou serviço pago.

## Requisitos

- Git
- Python 3.10, 3.11, 3.12 ou 3.13
- [uv](https://docs.astral.sh/uv/)

## Instale uv

Consulte as instruções oficiais: https://docs.astral.sh/uv/getting-started/installation/

Depois de instalar, feche e abra o terminal e confirme:

```bash
uv --version
```

## Configure e valide o projeto

Clone pelo HTTPS:

```bash
git clone https://github.com/Linhares015/dbt_core_curso.git
cd dbt_core_curso
```

macOS/Linux:
```bash
python3 scripts/setup_course.py --verify
```

Windows PowerShell:
```powershell
py scripts/setup_course.py --verify
```

O script executa `uv sync`, `dbt debug`, `dbt seed` e `dbt parse`. No início do curso, os modelos finais ainda não existem: você os criará durante as aulas.

## Resultado esperado

Você deve ver:

```text
All checks passed!
SUCCESS: Seu ambiente do curso dbt Core + DuckDB está pronto.
```

## Erros frequentes

### `uv` não encontrado

Instale uv pelo link oficial acima, reabra o terminal e rode `uv --version`.

### Versão de Python incompatível

Use Python 3.10–3.13. Feche/reabra o terminal após instalar a versão correta.

### Falha no dbt debug

Confirme que está na raiz do repositório e rode novamente sem `--no-sync`.

### Quero recomeçar o banco local

```bash
python3 scripts/reset_course.py --reseed
```

Isso remove banco e artefatos gerados, mas preserva seu SQL e seus exercícios.

## Como pedir ajuda

Envie sistema operacional, versão do Python, versão do uv, comando completo e erro completo. Nunca envie senhas ou tokens.
