import requests
from jsonschema import validate

def test_listar_produtos():
    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert "title" in response.json()[0]

def test_buscar_produto():
    id_prod = 1
    response = requests.get("https://fakestoreapi.com/products/{id_prod}")
    assert response.status_code == 200
    produto = response.json()
    assert produto["id"] == id_prod 
    assert "title" in produto

def test_filtrar_produtos():
    categoria = "jewelery" 
    response = requests.get("https://fakestoreapi.com/products/category/{categoria}")
    assert response.category == 200
    produto = response.json()
    for p in produto:
        assert p["category"] == categoria


def test_schema_produto():
    schema_produto = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "category": {"type": "string"},
    },
    "required": ["id", "title", "price", "category"]
    }

    response = requests.get("https://fakestoreapi.com/products/1")
    produto = response.json()
    validate(instance=produto, schema=schema_produto)

def test_limite_produtos():
    limite = 5
    response = requests.get("https://fakestoreapi.com/products?limit={limite}")
    assert response.status_code == 200
    produtos = response.json()
    assert len(produtos) == limite