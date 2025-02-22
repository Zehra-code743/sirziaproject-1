import streamlit as st # type: ignore
import random
import pandas as pd # type: ignore

# Function to provide motivational quotes for neurosurgeons
def get_motivational_quote():
    quotes = [
        "Precision comes from practice. Keep refining your skills!",
        "Every challenge is an opportunity to grow. Stay resilient!",
        "The mind, like a muscle, strengthens with use. Keep learning!",
        "Great surgeons aren’t born, they are trained. Keep pushing forward!"
    ]
    return random.choice(quotes)

# Function to generate random productivity progress data for visualization
def generate_progress_data():
    days = [f"Day {i}" for i in range(1, 8)]
    scores = [random.randint(40, 100) for _ in range(7)]
    return pd.DataFrame({'Day': days, 'Productivity Score': scores})

# Function to provide a tip for neurosurgeons
def get_neurosurgeon_tip():
    tips = [
        "Always review surgical procedures before performing them.",
        "Maintain steady hands with regular dexterity exercises.",
        "Stay updated with the latest medical research and advancements.",
        "Practice mindfulness to improve concentration during surgery."
    ]
    return random.choice(tips)

# Main function to build the Streamlit app
def main():
    st.set_page_config(page_title="NeuroThrive AI", layout="wide")
    
    # Dark and Light Mode Toggle
    mode = st.sidebar.radio("Choose Theme:", ["Light Mode", "Dark Mode"])
    
    if mode == "Dark Mode":
        st.markdown(
            """
            <style>
                body {background-color: #121212; color: white;}
                .stButton>button {background-color: #BB86FC; color: white;}
                .stSuccess {color: #03DAC6; font-weight: bold;}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                body {background-color: #eef2f3;}
                .stButton>button {background-color: #007BFF; color: white; font-size: 16px; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);}
                .stSuccess {color: green; font-weight: bold;}
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # App Title and Subtitle
    st.title("🧠 NeuroThrive AI")
    st.subheader("Growth Mindset App for Neurosurgeons")
    
    # Motivational Quote Section
    st.markdown("---")
    st.header("📌 Daily Motivation")
    if st.button("Get Inspiration"):
        st.success(get_motivational_quote())
    
    # Neurosurgeon Tip Section
    st.markdown("---")
    st.header("🩺 Neurosurgeon Pro Tip")
    if st.button("Get a Tip"):
        st.info(get_neurosurgeon_tip())
    
    # Cognitive Exercise Section
    st.markdown("---")
    st.header("🧩 Cognitive Exercise")
    st.write("Improve your focus with this quick challenge:")
    num1, num2 = random.randint(10, 99), random.randint(10, 99)
    user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0)
    if st.button("Check Answer"):
        if user_answer == num1 + num2:
            st.success("Correct! Your mind is sharp.")
        else:
            st.error("Oops! Try again.")
    
    # Progress Tracker Section with Visualization
    st.markdown("---")
    st.header("📊 Progress Tracker")
    df = generate_progress_data()
    st.line_chart(df.set_index('Day'))
    
    # Footer Section
    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>© 2025 NeuroThrive AI | Empowering Neurosurgeons for Excellence | Created by Shan-E-Zehra</h4>", unsafe_allow_html=True)
    st.info("Stay consistent. The best neurosurgeons never stop learning!")

if __name__ == "__main__":
    main()
