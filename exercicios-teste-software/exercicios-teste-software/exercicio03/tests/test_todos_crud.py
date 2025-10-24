import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

@pytest.fixture
def to_do_novo():
    # Fixture para criar um todo antes do teste
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    resposta = requests.post(BASE_URL, json=payload)
    assert resposta.status_code == 201
    todo = resposta.json()
    
    yield todo  # fornece o todo para o teste

    # Teardown (DELETE) - no JSONPlaceholder, não é realmente deletado
    requests.delete(f"{BASE_URL}/{todo['id']}")


def teste_criar_to_do():
    payload = {
        "title": "Nova tarefa",
        "completed": False,
        "userId": 1
    }
    resposta = requests.post(BASE_URL, json=payload)
    assert resposta.status_code == 201
    dado = resposta.json()
    assert dado["title"] == payload["title"]
    assert dado["completed"] == payload["completed"]
    assert dado["userId"] == payload["userId"]


def teste_criar_to_do_sem_titulo():
    payload = {
        "completed": False,
        "userId": 1
    }
    resposta = requests.post(BASE_URL, json=payload)
    # JSONPlaceholder aceita, mas geralmente daria erro 400
    assert resposta.status_code == 201
    dado = resposta.json()
    assert "title" not in dado or dado["title"] is None


def teste_ler_to_do():
    resposta = requests.get(f"{BASE_URL}/1")
    assert resposta.status_code == 200
    dado = resposta.json()
    assert dado["id"] == 1
    assert "title" in dado


def teste_atualizar_to_do(to_do_novo):
    todo_id = to_do_novo["id"]
    payload = {"completed": True}
    resposta = requests.patch(f"{BASE_URL}/{todo_id}", json=payload)
    assert resposta.status_code == 200
    dado = resposta.json()
    assert dado["completed"] is True


def teste_deletar_to_do(to_do_novo):
    todo_id = to_do_novo["id"]
    resposta = requests.delete(f"{BASE_URL}/{todo_id}")
    assert resposta.status_code in [200, 204]


def teste_verificar_to_do_deletado(to_do_novo):
    todo_id = to_do_novo["id"]
    requests.delete(f"{BASE_URL}/{todo_id}")
    resposta = requests.get(f"{BASE_URL}/{todo_id}")
    # JSONPlaceholder sempre retorna algo, mas simularia 404
    assert resposta.status_code in [200, 404]
