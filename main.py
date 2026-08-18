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
    
    # Add logic inside the button block
    if st.button("Generate Practice Questions"):
        st.subheader(f"📝 Practice Questions: {subject}")
        
        if subject == "Python Development":
            st.write("1. What is the difference between a list and a tuple?")
            st.write("2. How does a `for` loop differ from a `while` loop?")
            st.write("3. What is a Streamlit session state?")
            
        elif subject == "Organic Chemistry":
            st.write("1. Explain the difference between SN1 and SN2 reactions.")
            st.write("2. What functional group is identified by the 2,4-DNP test?")
            st.write("3. Define structural isomerism with an example.")
            
        elif subject == "Mathematics":
            st.write("1. What is the derivative of $f(x) = x^3 + 2x$?")
            st.write("2. Solve for $x$: $2x + 5 = 15$.")
            st.write("3. Define the Pythagorean theorem.")
            
        else:
            st.write("1. What is Newton's second law of motion?")
            st.write("2. Explain the process of photosynthesis.")
            st.write("3. What is the pH scale used for?")
