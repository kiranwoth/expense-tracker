from typing import Dict

from fastapi import FastAPI, HTTPException, Response, status

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


@app.get("/expenses/", response_model=Dict[str, schemas.Expense])
async def read_expenses():
    return expenses


@app.get("/expenses/{expense_id}/", response_model=schemas.Expense)
async def read_expense(expense_id: str):
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expenses[expense_id]


@app.post("/expenses/", response_model=schemas.Expense)
async def create_expense(expense: schemas.ExpenseCreate):
    new_expense = schemas.Expense(**expense.dict())
    expenses[new_expense.id] = new_expense
    return new_expense


@app.patch("/expenses/{expense_id}", response_model=schemas.Expense)
async def update_expense(expense_id: str, expense_partial: schemas.ExpenseUpdate):
    # remove parts of expense that are None (not updated)
    updated_expense = expense_partial.dict(exclude_unset=True)
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense = expenses[expense_id]
    # update expense values
    for key, value in updated_expense.items():
        expense[key] = value
    expenses[expense_id] = expense
    return expense


@app.delete("/expenses/{expense_id}/", response_class=Response)
async def delete_expense(expense_id: str):
    if expense_id not in expenses:
        raise HTTPException(status_code=404, detail="Expense not found")
    del expenses[expense_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
