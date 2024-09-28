# 🌐 Localhost ETL Project

Bem-vindo ao projeto **Localhost ETL**! 🚀 Este é um sistema completo de **Extração, Transformação e Carga (ETL)**, desenvolvido para processar dados a partir de arquivos Excel e armazená-los de forma eficiente em um banco de dados **MySQL**.

## 📚 Visão Geral

O projeto **Localhost ETL** foi criado para automatizar o processo de integração de dados, detectando automaticamente novos arquivos Excel, realizando a limpeza e transformação dos dados, e armazenando-os no banco de dados.

### 🎯 Objetivos do Projeto

- 👀 Monitorar continuamente um diretório em busca de novos arquivos Excel.
- 🧹 Realizar a limpeza e transformação dos dados conforme necessário.
- 💾 Armazenar os dados limpos em um banco de dados **MySQL**.
- 📝 Gerar logs detalhados de erros e sucessos durante o processamento.

## 🏗️ Arquitetura do Projeto

Abaixo está a estrutura do projeto `localhost-etl`, que inclui todos os arquivos e diretórios principais:

```bash
localhost-etl/
├── etl_project/
│   ├── src/
│   │   ├── config.py                  # Configurações e variáveis de ambiente
│   │   ├── database.py                # Configuração do banco de dados e operações
│   │   ├── etl/
│   │   │   ├── etl_processor.py        # Processamento ETL
│   │   │   ├── data_cleaning.py        # Funções de limpeza de dados
│   │   │   ├── error_handling.py       # Tratamento de erros
│   │   ├── logging/
│   │   │   ├── logger.py               # Configuração de logging
│   │   ├── file_monitor.py             # Monitoramento de arquivos Excel
│   │   ├── utils.py                    # Funções utilitárias
│   │   ├── error_files/                # Diretório para arquivos com erros
│   ├── config/
│   │   └── sheet_mappings.json         # Mapeamento entre Excel e Banco de Dados
│   ├── .env                         # Variáveis de ambiente
│   ├── requirements.txt                # Dependências do projeto
├── README.md                           # Documentação do projeto
```

## ⚙️ Como Funciona

- **Monitoramento de Arquivos**: O script `file_monitor.py` utiliza a biblioteca `watchdog` para monitorar um diretório específico em busca de novos arquivos Excel.
- **Processamento ETL**: Ao detectar um novo arquivo, a função `run_etl` é chamada para extrair, transformar e carregar os dados.
- **Limpeza de Dados**: Funções no módulo `data_cleaning.py` realizam a limpeza e formatação dos dados.
- **Armazenamento no Banco de Dados**: Os dados transformados são inseridos em um banco de dados **MySQL**.
- **Logs de Erros**: Qualquer erro é registrado em arquivos JSON no diretório `error_files`.

## 📊 Mapeamento de Dados

O projeto utiliza o arquivo `sheet_mappings.json` para mapear os dados do Excel para as tabelas do banco de dados MySQL. Abaixo está o mapeamento entre as abas do Excel e as tabelas do banco:

| 📄 **Aba do Excel**           | 🛢️ **Tabela no Banco**          | 📋 **Descrição**                           |
|-----------------------------|---------------------------------|---------------------------------------------|
| **processos seletivos**      | `dim_recruitment_processes`     | Processos seletivos e seus detalhes         |
| **vagas**                   | `dim_jobs`                      | Informações das vagas abertas               |
| **candidatos**              | `dim_candidates`                | Detalhes dos candidatos                    |
| **contratações**            | `fact_hirings`                  | Registro das contratações feitas            |
| **entrevistas**             | `fact_applications`             | Informações sobre entrevistas e aplicações  |
| **avaliacao de candidatos** | `fact_applications`             | Avaliações dos candidatos                   |
| **feedbacks**               | `fact_applications`             | Feedbacks dados ao longo do processo        |
| **rh**                      | `dim_recruiters`                | Informações dos recrutadores                |
| **acoes do processo**       | `fact_applications`             | Ações realizadas no processo seletivo       |

## 🛠️ Pré-requisitos

Para garantir que o projeto funcione corretamente, certifique-se de ter o seguinte instalado:

- **Python 3.x**
- **MySQL**
- Bibliotecas Python necessárias (instaladas via `pip`)


## 🚀 Como Executar o Projeto

### 1. Clone o Repositório:
```bash
git clone https://github.com/seu_usuario/localhost-etl.git
cd localhost-etl/etl_project
```

### 2. Configurações:
* Edite o arquivo env.env para definir as variáveis de ambiente necessárias, como a URI do banco de dados e diretórios de log.


### 3. 📦 Instalação das Dependências:
* Na raiz do projeto, dentro da pasta `etl_project`, você encontrará o arquivo `requirements.txt`. Para instalar todas as dependências necessárias, execute o comando abaixo:

```bash
pip install -r requirements.txt
```

### 4. Execute o Script Principal:

```bash
python src/main.py
```

### 5. Monitore o Diretório:
* Coloque seus arquivos Excel no diretório especificado nas variáveis de ambiente. O sistema irá processá-los automaticamente.



### 📊 Estrutura de Dados
Os dados são mapeados a partir do arquivo sheet_mappings.json, que define como os dados nas abas do Excel devem ser carregados nas tabelas do banco de dados.