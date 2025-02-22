import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import plotly.express as px # type: ignore

def main():
    st.set_page_config(page_title="NeuroThrive AI", layout="wide")
    
    # Persistent Theme Toggle
    if "theme" not in st.session_state:
        st.session_state["theme"] = "Light Mode"
    
    theme = st.sidebar.radio("Choose Theme:", ["Light Mode", "Dark Mode"], index=(0 if st.session_state["theme"] == "Light Mode" else 1))
    st.session_state["theme"] = theme
    
    bg_color = "#F5F5F5" if theme == "Light Mode" else "#1E1E1E"
    text_color = "black" if theme == "Light Mode" else "white"
    card_bg = "rgba(255, 255, 255, 0.1)" if theme == "Dark Mode" else "#FFFFFF"
    
    st.markdown(f"""
        <style>
            body {{ background: {bg_color}; color: {text_color}; }}
            .stButton>button {{
                background-color: #FF5733;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(255, 87, 51, 0.4);
            }}
            .card {{
                background: {card_bg};
                padding: 15px;
                border-radius: 15px;
                box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(10px);
                margin-bottom: 20px;
            }}
            .title-text {{
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #FFD700;
            }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title-text'>🧠 NeuroThrive AI</h1>", unsafe_allow_html=True)
    st.subheader("Growth Mindset App for Neurosurgeons")
    
    # Motivational Quote Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📌 Daily Motivation")
    st.success("Excellence is a habit, not an act. Keep going!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Neurosurgeon Tip Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🩺 Neurosurgeon Pro Tip")
    st.info("Always review surgical procedures before performing them.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Cognitive Exercise Section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🧩 Cognitive Exercise")
    user_answer = st.number_input("What is 25 + 37?", min_value=0)
    if st.button("Check Answer"):
        if user_answer == 62:
            st.success("Correct! Your mind is sharp.")
        else:
            st.error("Oops! Try again.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Progress Tracker Section with Graph
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Progress Tracker")
    st.write("Enter your productivity scores for the last 7 days:")
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    scores = [st.number_input(day, min_value=0, max_value=100) for day in days]
    
    if st.button("Show Progress Chart"):
        df = pd.DataFrame({"Day": days, "Productivity Score": scores})
        fig = px.line(df, x="Day", y="Productivity Score", title="Your Productivity Over the Week", markers=True)
        st.plotly_chart(fig)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional Neurosurgical Facts
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🧠 Neurosurgical Fact")
    st.warning("The human brain has about 86 billion neurons, making it one of the most complex structures in the universe!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(
        "<h4 style='text-align: center; color: #FFD700;'>© 2025 NeuroThrive AI | Created by Shan-E-Zehra</h4>",
        unsafe_allow_html=True
    )
    st.info("Stay consistent. The best neurosurgeons never stop learning!")

if __name__ == "__main__":
    main()
