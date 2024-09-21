# 🌐 Localhost ETL Project

Projeto **Localhost ETL**! Este é um sistema de extração, transformação e carga (ETL) desenvolvido para processar dados de arquivos Excel e armazená-los em um banco de dados MySQL.

## 📚 Visão Geral

O **Localhost ETL** foi projetado para automatizar o processo de integração de dados. Ele monitora um diretório específico em busca de arquivos Excel, limpa os dados, os transforma conforme necessário e os carrega em um banco de dados.

### 🎯 Objetivos do Projeto

- Monitorar continuamente um diretório em busca de novos arquivos Excel.
- Realizar a limpeza e transformação dos dados contidos nesses arquivos.
- Armazenar os dados limpos em um banco de dados MySQL.
- Gerar logs detalhados de erros e sucessos durante o processamento.

## 🏗️ Arquitetura do Projeto

O projeto está organizado da seguinte maneira:
### Estrutura do Projeto

Abaixo está a estrutura do projeto `localhost-etl`, que inclui todos os arquivos e diretórios relevantes:

```bash
localhost-etl/
├── etl_project/
│   ├── src/
│   │   ├── config.py                  # Configurações e variáveis de ambiente
│   │   ├── database.py                # Configuração do banco de dados e operações
│   │   ├── etl/
│   │   │   ├── etl_processor.py        # Processamento do ETL
│   │   │   ├── data_cleaning.py        # Funções de limpeza de dados
│   │   │   ├── error_handling.py       # Mapeamento de erros
│   │   ├── logging/
│   │   │   ├── logger.py               # Configuração do logging
│   │   ├── file_monitor.py             # Monitoramento de arquivos Excel
│   │   ├── utils.py                    # Funções utilitárias
│   │   ├── error_files/                # Diretório para arquivos com erros
│   │   │   └── ERROR_DIRECTORY_PATH/    # Caminho para arquivos de erro
│   │   │   └── LOG_ERRORS_JSON          # Caminho para arquivos de json de erros
│   │   ├── completed_files/            # Diretório para arquivos processados com sucesso
│   │   │   └── COMPLETED_DIRECTORY_PATH/ # Caminho para arquivos processados
│   │   └── main.py                     # Execução do script principal
│   ├── config/
│   │   └── sheet_mappings.json         # Arquivo JSON com os mapeamentos
│   ├── env.env                         # Arquivo de variáveis de ambiente
│   ├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação do projeto 
```


## ⚙️ Como Funciona

1. **Monitoramento de Arquivos**: O script `file_monitor.py` utiliza a biblioteca `watchdog` para monitorar um diretório específico em busca de novos arquivos Excel.

2. **Processamento ETL**: Quando um novo arquivo é detectado, a função `run_etl` é chamada, iniciando o processo de extração, transformação e carga dos dados.

3. **Limpeza de Dados**: O módulo `data_cleaning.py` contém funções para limpar e formatar os dados conforme as regras definidas.

4. **Armazenamento no Banco de Dados**: Os dados transformados são armazenados em um banco de dados MySQL, conforme definido nas configurações.

5. **Logs de Erros**: Erros durante o processamento são registrados em arquivos JSON no diretório `error_files`.


## 📊Mapeamento de Dados

Abaixo está o mapeamento entre as abas do arquivo Excel e as tabelas do banco de dados, juntamente com uma breve descrição de cada uma.

| Aba do Excel                | Tabela no Banco                | Descrição                                   |
|-----------------------------|---------------------------------|---------------------------------------------|
| **processos seletivos**      | `dim_recruitment_processes`     | Contém os processos seletivos               |
| **vagas**                   | `dim_jobs`                      | Informações sobre as vagas disponíveis      |
| **candidatos**              | `dim_candidates`                | Detalhes dos candidatos                     |
| **contratações**            | `fact_hirings`                  | Registro das contratações feitas            |
| **entrevistas**             | `fact_applications`             | Dados sobre as entrevistas e aplicações     |
| **avaliacao de candidatos** | `fact_applications`             | Resultados das avaliações dos candidatos    |
| **feedbacks**               | `fact_applications`             | Feedbacks recebidos durante o processo      |
| **rh**                      | `dim_recruiters`                | Informações sobre os recrutadores           |
| **acoes do processo**       | `fact_applications`             | Registro das ações realizadas no processo   |


## 🛠️ Dependências

Certifique-se de que você tem as seguintes dependências instaladas. Você pode instalar todas as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```


## 🚀 Como Executar o Projeto

### 1. Clone o Repositório:
```bash
git clone https://github.com/seu_usuario/localhost-etl.git
cd localhost-etl/etl_project
```

### 2. Configurações:
* Edite o arquivo env.env para definir as variáveis de ambiente necessárias, como a URI do banco de dados e diretórios de log.

### 3. Execute o Script Principal:

```bash
python src/main.py
```

### 4. Monitore o Diretório:
* Coloque seus arquivos Excel no diretório especificado nas variáveis de ambiente. O sistema irá processá-los automaticamente.



### 📊 Estrutura de Dados
Os dados são mapeados a partir do arquivo sheet_mappings.json, que define como os dados nas abas do Excel devem ser carregados nas tabelas do banco de dados.