# Gerenciador de Tarefas em Python

Projeto simples para gerenciar tarefas com prioridades, status e validações. Inclui persistência em memória e testes automatizados.

---

## 📋 Funcionalidades

- Criação de tarefas com validação de título e prazo
- Enumerações para `Priority` (BAIXA, MEDIA, ALTA) e `Status` (PENDENTE, EM_PROGRESSO, CONCLUIDA)
- Armazenamento em memória com `InMemoryStorage`
- Repositório de tarefas (`TaskRepository`)
- Serviço para criação, listagem e atualização de tarefas (`TaskService`)
- Testes automatizados com `pytest` e mocks

---

## 🚀 Como executar

### 1. Criar ambiente virtual

```bash
python -m venv venv

.\venv\Scripts\activate

### 2. Instalar dependências
source venv/bin/activate

### 3. Rodar Testes 
pytest -v

### Relatório de Cobertura
pip install pytest-cov

## Estrutura do Projeto

Laboratorio_8/
├── task_manager/
│   ├── __init__.py
│   ├── task.py            # Definição de Task, Priority, Status
│   ├── storage.py         # InMemoryStorage
│   ├── repository.py      # TaskRepository
│   └── service.py         # TaskService
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_repository.py
│   └── test_service.py
├── requirements.txt
├── README.md
└── venv/                  # Ambiente virtual
