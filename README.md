# Gera Arquivos Mergeados em PDF

Executa um merge em dois ou mais arquivos pdf passados


## Estrutura do arquivo .env

### Seção DATABASE

Nesta seção estao definidas as configurações do banco de dados

> O banco de dados deve ser MySQL


```ini

[DATABASE]
DB_PORT = ''
DB_HOST = ''
DB_USER = ''
DB_DATABASE = ''
DB_PASSWORD = ''

```

## Gerar arquivo executável com o Pyinstaller

```bash

pyinstaller --onefile --name PdfMerger main.py  

```

