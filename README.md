# ETLCommoditiesDW
Projeto de monitoramento de preços de commodities utilizando Python.
- colocando o ambiente.
Utilizando: Python, SQl, Postgres e DBT-Core

## Comandos terminal:
- python -m venv .venv
- source .venv/Scripts/activate
- pip install pandas sqlalchemy python-dotenv psycopg2-binary yfinance
- python src/extract_load.py
- pip install dbt-postgres //pois vou usar o postgres
- dbt init
### Observar se tudo deu certo:
- cd dbsales_fz80
- dbt debug
### Executar cte
cd dbsales_fz80
dbt run
### Colocar tabela da pasta seeds dentro do banco
dbt seed