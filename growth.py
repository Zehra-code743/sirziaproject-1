import streamlit as st  # type: ignore # Streamlit for building the web app
import pandas as pd  # type: ignore # Pandas for handling data

# Function to provide a list of motivational quotes for neurosurgeons
def get_motivational_quote():
    quotes = [
        "Precision comes from practice. Keep refining your skills!",
        "Every challenge is an opportunity to grow. Stay resilient!",
        "The mind, like a muscle, strengthens with use. Keep learning!",
        "Great surgeons aren’t born, they are trained. Keep pushing forward!"
    ]
    return quotes

# Function to provide useful tips for neurosurgeons
def get_neurosurgeon_tip():
    tips = [
        "Always review surgical procedures before performing them.",
        "Maintain steady hands with regular dexterity exercises.",
        "Stay updated with the latest medical research and advancements.",
        "Practice mindfulness to improve concentration during surgery."
    ]
    return tips

# Main function to build the Streamlit app
def main():
    # Set page configuration
    st.set_page_config(page_title="NeuroThrive AI", layout="wide")

    # Apply attractive UI styling using CSS
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to right, #000428, #004e92);
                color: white;
            }
            .stButton>button {
                background-color: #FF5733;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(255, 87, 51, 0.4);
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 15px;
                box-shadow: 4px 4px 15px rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(10px);
            }
            .title-text {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #FFD700;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # App Title
    st.markdown("<h1 class='title-text'>🧠 NeuroThrive AI</h1>", unsafe_allow_html=True)
    st.subheader("Growth Mindset App for Neurosurgeons")

    # Motivational Quote Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📌 Daily Motivation")
    quote_list = get_motivational_quote()
    selected_quote = st.selectbox("Choose a Quote", quote_list)
    st.success(selected_quote)
    st.markdown('</div>', unsafe_allow_html=True)

    # Neurosurgeon Tip Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🩺 Neurosurgeon Pro Tip")
    tip_list = get_neurosurgeon_tip()
    selected_tip = st.selectbox("Select a Tip", tip_list)
    st.info(selected_tip)
    st.markdown('</div>', unsafe_allow_html=True)

    # Cognitive Exercise Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🧩 Cognitive Exercise")
    st.write("Improve your focus with this quick challenge:")
    num1, num2 = 27, 53  # Sample numbers for addition
    user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0)
    if st.button("Check Answer"):
        if user_answer == num1 + num2:
            st.success("Correct! Your mind is sharp.")
        else:
            st.error("Oops! Try again.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Progress Tracker Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Progress Tracker")
    st.write("Enter your productivity score for the last 7 days:")
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    scores = [st.number_input(day, min_value=0, max_value=100) for day in days]
    if st.button("Show Progress Data"):
        df = pd.DataFrame({"Day": days, "Productivity Score": scores})
        st.write(df)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer Section
    st.markdown(
        "<h4 style='text-align: center; color: #FFD700;'>© 2025 NeuroThrive AI | Created by Shan-E-Zehra</h4>",
        unsafe_allow_html=True
    )
    st.info("Stay consistent. The best neurosurgeons never stop learning!")

# Run the application
if __name__ == "__main__":
    main()
