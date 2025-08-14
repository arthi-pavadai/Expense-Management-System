from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class dateRange(BaseModel):
    start_date : date
    end_date: date

app = FastAPI()
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses = db_helper.fetchall_for_exp_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve from db")
    return expenses

@app.post("/expenses/{expense_date}")
def add_update_expense(expense_date: date, expenses: List[Expense]):
    db_helper.delete_exp_for_exp_date(expense_date)
    for expense in expenses:
        db_helper.insert_expenses(expense_date, expense.amount, expense.category, expense.notes)

@app.post("/Analytics/")
def get_analytics(daterange : dateRange):
        expense_summary=db_helper.fetchall_exp_summary(daterange.start_date, daterange.end_date)
        if expense_summary is None:
            raise HTTPException(status_code=500, detail="Failed to retrieve from db")

        total=sum(row['total'] for row in expense_summary)
        breakdown = {}

        for row in expense_summary:
            percentage = (row['total']/total)*100 if row['total'] != 0 else 0
            breakdown[row['category']] = {
                'total': row['total'],
                'percentage': percentage
            }

        return breakdown
