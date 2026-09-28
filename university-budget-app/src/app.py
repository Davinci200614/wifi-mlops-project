import streamlit as st

from utils import load_budget_data


st.set_page_config(page_title="University Budget App", page_icon="💰", layout="wide")
st.title("University Budget App")

budget_data = load_budget_data()

st.subheader("Overview")
st.write(f"Departments: {len(budget_data.get('departments', []))}")
st.write(f"Expenses: {len(budget_data.get('expenses', []))}")

st.info("Starter application scaffold is ready.")
