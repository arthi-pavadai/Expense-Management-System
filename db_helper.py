import pymysql
from contextlib import contextmanager
from logging_setup import setup_logging

logger = setup_logging("db_helper")

@contextmanager
def get_db_cursor(commit = False):
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "MySQL2024@Home",
        database = "expense_manager",
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def fetchall_for_exp_date(exp_date):
    logger.info("fetch expenses for date: {}".format(exp_date))
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (exp_date,))
        expense = cursor.fetchall()
        return expense

def fetchall_exp_summary(start, end):
    logger.info(f"fetch expenses summary for date start from: {start} and {end}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT category, sum(amount) as total FROM expenses WHERE expense_date BETWEEN %s and %s group by category", (start, end))
        expense = cursor.fetchall()
        return expense

def fetchall_exp_btw_exp_date(start, end):
    logger.info(f"fetch expenses for date start from: {start} and {end}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date BETWEEN %s and %s", (start, end))
        expense = cursor.fetchall()
        return expense

def delete_exp_for_exp_date(exp_date):
    logger.info(f"delete expenses for date: {exp_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s", (exp_date,))

def insert_expenses(exp_date,amount,category, notes):
    logger.info(f"insert expenses for date: {exp_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT into expenses(expense_date, amount, category, notes) VALUES(%s, %s, %s, %s)", (exp_date,amount,category,notes))
        print("Inserted expenses successfully")

if __name__ == '__main__':
    print(fetchall_for_exp_date("2024-08-01"))