# 🏫 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask**, **SQLAlchemy** e **SQLite**, como parte de uma arquitetura baseada em **microsserviços**.

---

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** responsável exclusivamente pelo gerenciamento das reservas de salas por turma. Ela depende da API de **Gerenciamento Escolar**, que fornece os dados das turmas.

### 🔗 Integração com a API de Turmas

Esta API realiza uma requisição HTTP (`GET /turmas/<id>`) para validar se a **turma informada** existe antes de permitir uma nova reserva.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- Requests

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/laura-dsouza/APIReservaSalas.git
cd APIReservaSalas 
```

### 2. (Opcional) Crie um ambiente virtual

``` bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

``` bash
pip install -r requirements.txt
```

### 4. Execute a api

``` bash
python app.py
```

### A aplicação estará disponível em:

``` bash
http://localhost:5002
```
---

## 📡 Endpoints Disponíveis

### 🔍 GET /reservas
Retorna todas as reservas cadastradas.

### ➕ POST /reservas
Cria uma nova reserva. A API realiza as seguintes validações:

- Verifica se a turma existe na API externa.

- Verifica se a sala já está reservada na data e horário informados.

- Verifica se o número de salas disponíveis já foi atingido (padrão: 13 salas).

### Corpo da requisição:
``` json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-25",
  "hora_inicio": "09:00",
  "hora_fim": "11:00"
}
```

---
## 🔗 Dependência externa

Certifique-se de que a API de Gerenciamento Escolar esteja rodando em:

``` bash
http://localhost:5000
```

E que o endpoint de GET /turmas/<id> esteja funcionando corretamente para que a validação seja feita com sucesso.

---

## 🛠️ Estrutura do Projeto

``` bash
ReservaSala/
│
├── instance/
│   └── reserva.db               
├── reserva/          
│   ├── reserva_model.py           
│   └── reserva_route.py
├── app.py    
├── config.py                
├── requirements.txt    
├── Dockerfile          
└── README.md        
```
---

## 🐳 Docker (Execução com container)

### 1. Build da imagem

``` bash
docker build -t reservasala .
```

### 2. Executar o container

``` bash
docker run -d -p 5002:5002 reservasala
```
---

## 🔒 Validações Implementadas

- ❌ Reserva em sala já ocupada no mesmo horário

- ❌ Quantidade máxima de salas atingida

- ❌ Tentativa de reserva para turma inexistente

---

## 📌 Observações
- A formatação de horário na resposta da API é HH:MM, mas o banco armazena como HH:MM:SS por padrão do SQLite.

- O banco de dados (reservas.db) é criado automaticamente na primeira execução.

---

## 🛠️ Futuras melhorias

- Implementação dos endpoints:

    - GET /reservas/<id>

    - PUT /reservas/<id>

    - DELETE /reservas/<id>

---

## 👩‍💻 Autoras

Projeto desenvolvido por [Geovanna Toso](https://github.com/geovannatoso), [Laura Dias](https://github.com/laura-dsouza) e [Talita Yuki](https://github.com/taltsolyu), como parte de estudos com Flask, microsserviços e integração entre APIs.

