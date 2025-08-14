import streamlit as st
from add_update import get_add_update
from Analytics import get_analytics

st.title("Expense Tracking System")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    get_add_update()
with tab2:
    get_analytics()

