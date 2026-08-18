import streamlit as st

st.set_page_config(page_title="Quick AI Assistant", page_icon="⚡")

st.title("⚡ Study Assistant")
st.write("Welcome! This lightweight app runs directly in your browser.")

# User Input
user_name = st.text_input("What is your name?", "")

if user_name:
    st.success(f"Hello, {user_name}! Ready to get to work?")

# Interactive feature
subject = st.selectbox(
    "Choose a topic to review today:",
    ["Select topic...", "Python Development", "Organic Chemistry", "Mathematics", "General Science"]
)

if subject != "Select topic...":
    st.info(f"Great choice! Preparing quick study notes for **{subject}**.")
    st.button("Generate Practice Questions")
