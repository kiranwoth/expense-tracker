from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"


def test_read_expenses():
    response = client.get("/expenses/")
    assert response.status_code == 200
    assert response.json() == {
        "8509e457-f491-46b5-bad1-e8d0504db2bb": {
            "cost": 80.0,
            "description": "Gas fill up",
            "category": "Gas",
            "id": "8509e457-f491-46b5-bad1-e8d0504db2bb",
            "time_created": "2023-06-18T15:56:46.218431+00:00",
        }
    }


def test_read_expense():
    response = client.get("/expenses/8509e457-f491-46b5-bad1-e8d0504db2bb/")
    assert response.status_code == 200
    assert response.json() == {
        "cost": 80.0,
        "description": "Gas fill up",
        "category": "Gas",
        "id": "8509e457-f491-46b5-bad1-e8d0504db2bb",
        "time_created": "2023-06-18T15:56:46.218431+00:00",
    }


def test_read_expense_item_not_found():
    response = client.get("/expenses/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Expense not found"}


def test_create_expense():
    expense = {"cost": 1400, "description": "Rent money for July", "category": "Rent"}
    response = client.post("/expenses", json=expense)
    assert response.status_code == 200
    new_expense = response.json()
    # remove `time_created` and `id` from response since they are generated
    # upon creation
    new_expense.pop("time_created")
    new_expense.pop("id")
    assert new_expense == {
        "cost": 1400,
        "description": "Rent money for July",
        "category": "Rent",
    }


def test_delete_expense():
    response = client.delete("/expenses/8509e457-f491-46b5-bad1-e8d0504db2bb")
    assert response.status_code == 204


def test_delete_expense_item_not_found():
    response = client.delete("/expenses/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Expense not found"}
