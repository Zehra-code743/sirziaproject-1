import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import os
import matplotlib.pyplot as plt # type: ignore
from io import BytesIO

# Page Configuration
st.set_page_config(page_title="Data Sweeper - Sterling Integrator", page_icon="🧹", layout="wide")

# Custom CSS for an Attractive UI
st.markdown(
    """
    <style>
        .stApp {
            background-color: #1e1e2f;
            color: #ffffff;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #ffcc00;
            text-shadow: 3px 3px 10px rgba(255, 255, 0, 0.7);
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #cccccc;
            margin-bottom: 20px;
        }
        .stButton > button {
            background-color: #ffcc00;
            color: black;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background-color: #ffaa00;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="title">🧹 Data Sweeper - Sterling Integrator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Transform, clean, and visualize your data efficiently!</p>', unsafe_allow_html=True)

# File Upload Section
uploaded_files = st.file_uploader("📂 Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read Data
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # Display Data
        st.subheader(f"📊 Preview of {file.name}")
        st.dataframe(df.head())

        # Data Cleaning Options
        st.subheader("🛠 Data Cleaning Options")
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"🗑 Remove Duplicates - {file.name}"):
                df.drop_duplicates(inplace=True)
                st.success("✅ Duplicates removed!")

        with col2:
            if st.button(f"🛠 Fill Missing Values - {file.name}"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("✅ Missing values filled!")

        # Column Selection
        st.subheader("🎯 Select Columns to Keep")
        selected_columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]

        # Data Visualization
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"📊 Show Vertical Bar Chart for {file.name}"):
            num_cols = df.select_dtypes(include='number').columns
            if len(num_cols) >= 2:
                fig, ax = plt.subplots()
                df.plot(kind='bar', x=num_cols[0], y=num_cols[1], ax=ax, color='#ffcc00')
                ax.set_title("Vertical Bar Chart")
                ax.set_xlabel(num_cols[0])
                ax.set_ylabel(num_cols[1])
                st.pyplot(fig)
            else:
                st.warning("⚠️ Not enough numeric columns to generate a bar chart.")

        # File Conversion
        st.subheader("🔄 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"📥 Convert & Download {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False, engine='xlsxwriter')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            buffer.seek(0)
            st.download_button(
                label=f"📥 Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
            st.success("✅ File converted and ready for download!")

# Footer
st.markdown("---")
st.markdown('<p style="text-align:center; font-size:16px;">💡 Built with ❤️ by SHAN-E-ZEHRA using Streamlit</p>', unsafe_allow_html=True)
