import streamlit as st
from datetime import datetime
import requests
API_Url = "http://127.0.0.1:8000"

def get_add_update():
    selected_date=st.date_input("Enter Expense date", datetime(2024,8,1),label_visibility="collapsed")
    response=requests.get(f"{API_Url}/expenses/{selected_date}")
    if response.status_code == 200:
        expenses= response.json()
    else:
        st.error("Failed to fetch expense")
        expenses = []
    categories = ["Rent","Entertainment","Food","Shopping","Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            col1.subheader("Amount")
        with col2:
            col2.subheader("Categories")
        with col3:
            col3.subheader("Notes")
        new_expenses = []
        for i in range(5):
            if i < len(expenses):
                amount = expenses[i]["amount"]
                category = expenses[i]["category"]
                notes = expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""
            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input=st.number_input(label="amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}",label_visibility="collapsed")
            with col2:
                category_input=st.selectbox(label="category", options=categories, index=categories.index(category), key=f"category+{i}",label_visibility="collapsed")
            with col3:
                notes_input=st.text_input(label="notes", value=notes, key=f"notes_{i}",label_visibility="collapsed")

            new_expenses.append({
                'amount' : amount_input,
                'category' : category_input,
                'notes' : notes_input}
            )
        submitted = st.form_submit_button(label="Submit")
        if submitted:
            filtered_expenses = [expense for expense in new_expenses if expense['amount'] > 0]
            response=requests.post(f"{API_Url}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code ==200:
                st.success("Successfully submitted expense")
            else:
                st.error("Failed to submit expense")