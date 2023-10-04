from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_revenue_valid():
    # Prueba un escenario válido
    order_request = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"}
        ],
        "criterion": "completed"
    }

    response = client.post("/solution", json=order_request)
    assert response.status_code == 201
    assert response.json() == "999.99"

def test_calculate_revenue_negative_price():
    # Prueba un escenario con precio negativo
    order_request = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": -999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"}
        ],
        "criterion": "completed"
    }

    response = client.post("/solution", json=order_request)
    assert response.status_code == 422
    assert response.json() == {"detail": [
    {
      "loc": [
        "body",
        "orders",
        0,
        "price"
      ],
      "msg": "ensure this value is greater than or equal to 0.01",
      "type": "value_error.number.not_ge",
      "ctx": {
        "limit_value": 0.01
      }
    }
  ]}



