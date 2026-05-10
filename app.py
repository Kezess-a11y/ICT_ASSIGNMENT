import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mechanical Toolset", page_icon="⚙️")

# --- HEADER SECTION ---
st.title("⚙️ Mechanical Engineering Toolset")
st.markdown("### **Developer Information**")
st.info(f"**Name:** Shah Muhammad  \n**Roll Number:** 25-ME-140")
st.markdown("---")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Tool Selection")
tool = st.sidebar.selectbox("Choose a Tool", ["Unit Converter", "Material Density Checker"])

# --- TOOL 1: UNIT CONVERTER ---
if tool == "Unit Converter":
    st.header("📏 Mechanical Unit Converter")
    
    category = st.selectbox("Category", ["Pressure", "Force", "Length"])
    
    col1, col2 = st.columns(2)
    
    if category == "Pressure":
        units = {"Pascal [Pa]": 1, "Bar": 1e5, "PSI": 6894.76}
        val = col1.number_input("Enter Value", value=1.0)
        from_u = col1.selectbox("From", list(units.keys()))
        to_u = col2.selectbox("To", list(units.keys()))
        # Conversion Logic
        result = val * (units[from_u] / units[to_u])
        col2.metric("Converted Value", f"{result:.4f} {to_u}")

    elif category == "Force":
        units = {"Newton [N]": 1, "Kilonewton [kN]": 1000, "Pound-force [lbf]": 4.44822}
        val = col1.number_input("Enter Value", value=1.0)
        from_u = col1.selectbox("From", list(units.keys()))
        to_u = col2.selectbox("To", list(units.keys()))
        result = val * (units[from_u] / units[to_u])
        col2.metric("Converted Value", f"{result:.4f} {to_u}")

    elif category == "Length":
        units = {"Meter [m]": 1, "Millimeter [mm]": 0.001, "Inch [in]": 0.0254, "Foot [ft]": 0.3048}
        val = col1.number_input("Enter Value", value=1.0)
        from_u = col1.selectbox("From", list(units.keys()))
        to_u = col2.selectbox("To", list(units.keys()))
        result = val * (units[from_u] / units[to_u])
        col2.metric("Converted Value", f"{result:.4f} {to_u}")

# --- TOOL 2: DENSITY CHECKER ---
else:
    st.header("🧪 Material Density Checker")
    st.write("Density ($\rho$) is defined as mass per unit volume:")
    st.latex(r"\rho = \frac{m}{V}")
    
    # Material Data
    data = {
        "Material": ["Steel", "Aluminum", "Copper", "Titanium", "Cast Iron", "Brass", "Water"],
        "Density (kg/m³)": [7850, 2700, 8960, 4500, 7200, 8500, 1000],
        "Specific Gravity": [7.85, 2.7, 8.96, 4.5, 7.2, 8.5, 1.0]
    }
    df = pd.DataFrame(data)
    
    search = st.selectbox("Select Material to Inspect", df["Material"].unique())
    selected_row = df[df["Material"] == search]
    
    st.table(selected_row)
    
    st.subheader("Full Comparison Table")
    st.dataframe(df.style.highlight_max(axis=0, subset=["Density (kg/m³)"], color='#ffa5a5'))

# --- FOOTER ---
st.markdown("---")
st.caption("ME-140 Assignment Project | Built with Streamlit")
