import streamlit as st  # type: ignore # Import Streamlit for building the web app
import pandas as pd  # type: ignore # Import Pandas for handling tabular data

# Function to provide motivational quotes for neurosurgeons
def get_motivational_quote():
    quotes = [
        "Precision comes from practice. Keep refining your skills!",
        "Every challenge is an opportunity to grow. Stay resilient!",
        "The mind, like a muscle, strengthens with use. Keep learning!",
        "Great surgeons aren’t born, they are trained. Keep pushing forward!"
    ]
    return quotes  # Returns a list of motivational quotes

# Function to provide a tip for neurosurgeons
def get_neurosurgeon_tip():
    tips = [
        "Always review surgical procedures before performing them.",
        "Maintain steady hands with regular dexterity exercises.",
        "Stay updated with the latest medical research and advancements.",
        "Practice mindfulness to improve concentration during surgery."
    ]
    return tips  # Returns a list of neurosurgical tips

# Main function to build the Streamlit app
def main():
    # Set the page title and layout style
    st.set_page_config(page_title="NeuroThrive AI", layout="wide")

    # Sidebar - Dark and Light Mode Toggle
    mode = st.sidebar.radio("Choose Theme:", ["Light Mode", "Dark Mode"])

    # Apply different styles for Dark Mode and Light Mode
    if mode == "Dark Mode":
        st.markdown(
            """
            <style>
                body {background-color: #121212; color: white;}
                .stButton>button {background-color: #BB86FC; color: white; box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);}
                .stSuccess, .stInfo {color: #03DAC6; font-weight: bold;}
                .card {
                    background-color: #1E1E1E; 
                    padding: 15px; 
                    border-radius: 10px; 
                    box-shadow: 4px 4px 15px rgba(255, 255, 255, 0.2);
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                body {background-color: #F5F5F5;}
                .stButton>button {
                    background-color: #007BFF; 
                    color: white; 
                    font-size: 16px; 
                    padding: 10px; 
                    border-radius: 10px; 
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
                }
                .stSuccess, .stInfo {color: green; font-weight: bold;}
                .card {
                    background-color: white; 
                    padding: 15px; 
                    border-radius: 10px; 
                    box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
                }
            </style>
            """,
            unsafe_allow_html=True
        )

    # App Title and Subtitle
    st.title("🧠 NeuroThrive AI")  # Main title of the app
    st.subheader("Growth Mindset App for Neurosurgeons")  # Short description of the app

    # Motivational Quote Section
    st.markdown("---")  # Creates a horizontal line separator
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Apply card styling
    st.header("📌 Daily Motivation")  # Section header
    quote_list = get_motivational_quote()  # Fetch list of quotes
    selected_quote = st.selectbox("Choose a Quote", quote_list)  # Dropdown to select a quote
    st.success(selected_quote)  # Displays the selected quote
    st.markdown('</div>', unsafe_allow_html=True)  # Close card

    # Neurosurgeon Tip Section
    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Apply card styling
    st.header("🩺 Neurosurgeon Pro Tip")  # Section header for neurosurgeon tips
    tip_list = get_neurosurgeon_tip()  # Fetch list of tips
    selected_tip = st.selectbox("Select a Tip", tip_list)  # Dropdown to select a tip
    st.info(selected_tip)  # Displays the selected tip
    st.markdown('</div>', unsafe_allow_html=True)  # Close card

    # Cognitive Exercise Section
    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Apply card styling
    st.header("🧩 Cognitive Exercise")  # Section header for cognitive exercise
    st.write("Improve your focus with this quick challenge:")
    
    # Fixed math problem instead of generating random numbers
    num1, num2 = 27, 53  
    user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0)  # User input field
    
    # Check if the answer is correct when the button is pressed
    if st.button("Check Answer"):
        if user_answer == num1 + num2:
            st.success("Correct! Your mind is sharp.")  # Success message if correct
        else:
            st.error("Oops! Try again.")  # Error message if incorrect
    st.markdown('</div>', unsafe_allow_html=True)  # Close card

    # Progress Tracker Section with User Input
    st.markdown("---")
    st.markdown('<div class="card">', unsafe_allow_html=True)  # Apply card styling
    st.header("📊 Progress Tracker")  # Section header
    st.write("Enter your productivity score for the last 7 days:")

    # Create input fields for users to enter their daily productivity scores
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    scores = [st.number_input(day, min_value=0, max_value=100) for day in days]  # Input boxes for each day

    # Button to display the entered data
    if st.button("Show Progress Data"):
        df = pd.DataFrame({"Day": days, "Productivity Score": scores})  # Convert user input to a DataFrame
        st.write(df)  # Display the DataFrame
    st.markdown('</div>', unsafe_allow_html=True)  # Close card

    # Footer Section
    st.markdown("---")
    st.markdown(
        "<h4 style='text-align: center;'>© 2025 NeuroThrive AI | Empowering Neurosurgeons for Excellence | Created by Shan-E-Zehra</h4>", 
        unsafe_allow_html=True
    )  # Copyright notice with centered text
    st.info("Stay consistent. The best neurosurgeons never stop learning!")  # Encouraging message

# Ensures that the script runs only if executed directly (not when imported as a module)
if __name__ == "__main__":
    main()
