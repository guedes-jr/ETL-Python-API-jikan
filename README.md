
# 🌐 ETL Python consuminfo API Jikan
<div align="center">
<p align="center">
  <a href="https://github.com/guedes-jr/ETL-Python-API-jikan">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/guedes-jr/ETL-Python-API-jikan">
  </a>
  <a href="https://github.com/guedes-jr/ETL-Python-API-jikan/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/guedes-jr/ETL-Python-API-jikan">
  </a>
  <a href="https://github.com/guedes-jr/ETL-Python-API-jikan/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/guedes-jr/ETL-Python-API-jikan">
  </a>
  <a href="https://github.com/guedes-jr/ETL-Python-API-jikan/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/guedes-jr/ETL-Python-API-jikan">
  </a>
  <a href="https://github.com/guedes-jr/ETL-Python-API-jikan/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/github/license/guedes-jr/ETL-Python-API-jikan">
  </a>
</p>

## 📝 Sumário

- [Sobre o Projeto](#%EF%B8%8Fsobre-o-projeto)
- [Tecnologias Utilizadas](#-tecnologias-e-apis)
- [Funcionalidades](#-funcionalidades)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação-e-execução)
- [Estrutura de Pastas](#-estrutura-de-pastas)
- [Licença](#-licença)
- [Contato](#-contato)

## 🛠️Sobre o Projeto

Este projeto é um **ETL (Extract, Transform, Load)** que coleta dados de animes da **API Jikan**, transforma as informações e armazena os resultados em diferentes formatos (**SQLite, JSON ou CSV**). O objetivo é facilitar a análise e manipulação de dados de animes populares. O usuário pode escolher o formato de saída usando **flags na linha de comando**. Ideal para quem deseja automatizar a extração de informações do MyAnimeList. 🚀

## 🧰 Tecnologias e APIs

- [Python 3](https://www.python.org/downloads/release/python-315/) - Linguagem de progração
- [API Jikan](https://jikan.moe/) - API para consulta de dados de animes
- [JSON](https://www.json.org/json-en.html) - Formato leve de troca de dados.
- [Sqlite](https://www.sqlite.org/) - Banco de dados
- [CSV](https://pt.wikipedia.org/wiki/Comma-separated_values) - Arquivos de Textos com formato Regular.

## ✨ Funcionalidades

- Consulta Top animes da API da Jikan
- Determina o formado de saída dos dados (Sqlite, CSV e JSON)

## 📋 Requisitos

- [Python 3](https://www.python.org/downloads/release/python-315/)


## 🚀 Instalação e Execução

### Clonando o Repositório

```bash
# Clonando o Repositório
git clone https://github.com/guedes-jr/ETL-Python-API-jikan.git
```

### Criando e ativando ambiente virtual
```bash
# Criando ambiente virtual
python -m venv venv

# Ativando ambiente virtual
source venv/bin/activate
```

### Instalando requerimentos
```bash
# Instalando requerimentos
pip install -r requeriments.txt
```

### Executando
```bash
# Extraindo arquivo sqlite
python anime.py --output sqlite

# Extraindo arquivo csv
python anime.py --output csv

# Extraindo arquivo json
python anime.py --output json
```

## 📁 Estrutura de Pastas

```plaintext
.
├── anime.py
├── README.md
├── requeriments.txt
└── venv
    └── ...
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

👤 **Seu Nome**

- Github: [@guedes-jr](https://github.com/guedes-jr)
- LinkedIn: [João Guedes](https://www.linkedin.com/in/jo%C3%A3o-guedes-36a440135)
- Email: joao.guedes.developer@gmail.com

---

Desenvolvido com profissionalismo por [João Guedes](https://github.com/guedes-jr) 🤖.