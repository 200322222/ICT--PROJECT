import streamlit as st

# --- HEADER SECTION ---
st.set_page_config(page_title="Mechanical Unit & Density Tool", layout="centered")
st.title("🛠️ Mechanical Unit Converter & Density Checker")
st.subheader("Developed by: Adil Nadeem")
st.info("Roll Number: 25-ME176")

# --- MATERIAL DENSITY CHECKER ---
st.header("1. Material Density Checker")
density_data = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Cast Iron": 7200,
    "Concrete": 2400,
    "Water": 1000
}

material = st.selectbox("Select a Material:", list(density_data.keys()))
st.write(f"The density of **{material}** is **{density_data[material]} kg/m³**.")

# --- UNIT CONVERTER ---
st.header("2. Unit Converter")

category = st.radio("Choose Category:", ["Length", "Pressure", "Energy"])

if category == "Length":
    val = st.number_input("Enter Value (Meters):", value=1.0)
    col1, col2 = st.columns(2)
    col1.metric("Feet", round(val * 3.28084, 4))
    col2.metric("Inches", round(val * 39.3701, 4))

elif category == "Pressure":
    val = st.number_input("Enter Value (Pascal):", value=101325.0)
    col1, col2 = st.columns(2)
    col1.metric("Bar", round(val / 100000, 4))
    col2.metric("PSI", round(val * 0.000145038, 4))

elif category == "Energy":
    val = st.number_input("Enter Value (Joules):", value=1.0)
    col1, col2 = st.columns(2)
    col1.metric("Calories", round(val / 4.184, 4))
    col2.metric("BTU", round(val / 1055, 6))

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write(f"**User:** Adil Nadeem")
st.sidebar.write(f"**Roll No:** 25-ME176")
