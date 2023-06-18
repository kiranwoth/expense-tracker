from fastapi import FastAPI

from . import schemas

app = FastAPI()

# will use dictionary until database is integrated
expenses = {
    "8509e457-f491-46b5-bad1-e8d0504db2bb": {
        "cost": 80.0,
        "description": "Gas fill up",
        "category": "Gas",
        "id": "8509e457-f491-46b5-bad1-e8d0504db2bb",
        "time_created": "2023-06-18T15:56:46.218431+00:00",
    }
}


@app.get("/")
async def root():
    return "Hello World"


@app.post("/expenses/", response_model=schemas.Expense)
async def create_expense(expense: schemas.ExpenseCreate):
    new_expense = schemas.Expense(**expense.dict())
    expenses[new_expense.id] = new_expense
    return new_expense
