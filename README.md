# 🛠️ Laboratório SRE Junior: Monitoramento & Auto-Healing

Este repositório contém os artefatos do meu laboratório prático de Site Reliability Engineering (SRE). O objetivo foi estabilizar um ambiente Linux, gerenciar serviços em containers e implementar uma automação de recuperação de desastres com notificações em tempo real.

## 🚀 O que foi implementado

### 1. Gestão de Infraestrutura (Linux)
- **Otimização de Memória:** Configuração de **1GB de Swap** no Ubuntu Server para evitar falhas de *Out-Of-Memory* (OOM) em ambientes limitados.
- **Docker Management:** Deploy de servidor Nginx utilizando transferência de imagens via `docker save/load` para contornar restrições de rede.

### 2. Automação de Auto-Healing (Python)
Desenvolvimento de um script sentinela (`monitor.py`) que:
- Realiza checagem de saúde (Health Check) do container via SSH.
- **Auto-Recuperação:** Reinicia automaticamente o serviço caso seja detectada uma queda.
- **Resiliência:** Implementado com timeouts e tratamento de exceções para não travar a esteira de automação.

### 3. Observabilidade e Alerta
- **Integração com API do Telegram:** Notificações push instantâneas enviadas ao celular do engenheiro em caso de incidentes e recuperações bem-sucedidas.

### 4. CI/CD (GitHub Actions)
- Pipeline automatizado para **Linting** do código Python, garantindo que nenhum erro de sintaxe seja enviado para produção.

## 🛠️ Tecnologias Utilizadas
- **Linux:** Ubuntu Server & Linux Mint
- **Containerização:** Docker
- **Linguagem:** Python 3 (Bibliotecas nativas: `urllib`, `os`, `ssl`)
- **CI/CD:** GitHub Actions
- **Comunicação:** Telegram Bot API

---
*Este é um projeto de estudos focado nos fundamentos de SRE e DevOps.*