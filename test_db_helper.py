import pytest
from Backend import db_helper

def test_fetch_exp_btw_exp_date():
     expenses=db_helper.fetchall_exp_btw_exp_date("2024-08-02","2024-08-03")
     assert len(expenses)==11
     assert expenses[0]["amount"]== 50.0

def test_fetchall_for_exp_date():
     expense=db_helper.fetchall_for_exp_date("2024-08-01")
     assert len(expense)==4