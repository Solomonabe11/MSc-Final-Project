import streamlit as st
import joblib
import numpy as np
import pandas as pd  # Added to handle the DataFrame

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Mid Span Deflection Predictor", layout="centered")

# Inject custom CSS styles
st.markdown(
    """
    <style>
    /* App background with a green border */
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
        border: 5px solid green; /* Green border */
        border-radius: 15px; /* Rounded corners for the border */
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    /* Title styling */
    .title {
        font-size: 24px;
        font-weight: bold;
        color: #2a9d8f; /* Soothing green color */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
    }

    /* Description styling */
    .description {
        font-size: 18px;
        color: #264653; /* Dark teal */
        text-align: center;
        line-height: 1.8;
        margin-bottom: 20px;
        font-family: 'Verdana', sans-serif;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #264653; /* Dark teal */
        color: white;
    }

    [data-testid="stSidebar"] h1 {
        color: #e9c46a; /* Yellow accent for sidebar header */
        font-size: 22px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Result display styling */
    .result-container {
        background-color: #03fc9d; /* Black background */
        color: white; /* White text */
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
    }

    /* Buttons */
    button {
        background-color: #03fc9d;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s ease;
    }

    button:hover {
        background-color: #03fc9d; /* Highlight on hover */
        color: white;
    }



     /* Custom styling for the subheader */
    .user_input {
        font-size: 24px;
        text-align: center;
        padding-bottom:4px;
        font-weight: bold;
        color: #fcba03;
        margin-top: 20px;
        font-family: 'Arial', sans-serif;
    }


    /* Footer */
    .footer {
        font-size: 24px;
        color: #6c757d;
        text-align: center;
        margin-top: 40px;
        border-top: 1px solid #e9ecef;
        padding-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown('<div class="title">Mid Span Deflection Prediction App Using Random Forest ML</div>', unsafe_allow_html=True)
st.markdown('<div class="description">This app predicts the <strong>Mid Span Deflection</strong> of reinforced concrete beams based on input features. Adjust the values in the sidebar and click "Predict" to get started!</div>', unsafe_allow_html=True)

# Sidebar for input features
st.sidebar.header("Input Features")
w_mm = st.sidebar.number_input("Beam Width (w in mm)", min_value=100, max_value=1000, value=200)
h_mm = st.sidebar.number_input("Beam Height (h in mm)", min_value=100, max_value=1000, value=300)
d_mm = st.sidebar.number_input("Effective Depth (d in mm)", min_value=100, max_value=1000, value=250)
span_mm = st.sidebar.number_input("Beam C/C Span (mm)", min_value=500, max_value=10000, value=5000)
shear_span_mm = st.sidebar.number_input("Shear Span (mm)", min_value=500, max_value=5000, value=1500)
fct_mpa = st.sidebar.number_input("Tensile Strength (Fct in MPa)", min_value=1.0, max_value=10.0, value=3.2)
fc_mpa = st.sidebar.number_input("Compressive Strength (Fc in MPa)", min_value=10.0, max_value=100.0, value=30.0)
ec_gpa = st.sidebar.number_input("Elastic Modulus (Ec in GPa)", min_value=10.0, max_value=50.0, value=20.0)
fy_mpa = st.sidebar.number_input("Yield Strength (Fy in MPa)", min_value=100, max_value=1000, value=500)
es_gpa = st.sidebar.number_input("Steel Elastic Modulus (Es in GPa)", min_value=100, max_value=300, value=200)
diameter_mm = st.sidebar.number_input("Rebar Diameter (Ø in mm)", min_value=5.0, max_value=50.0, value=16.0)
num_rebars = st.sidebar.number_input("Number of Rebars", min_value=1, max_value=20, value=4)
as_mm2 = st.sidebar.number_input("Area of Steel (As in mm²)", min_value=100.0, max_value=5000.0, value=800.0)
load_kn = st.sidebar.number_input("Applied Load (KN)", min_value=0.0, max_value=200.0, value=50.0)

# Function to return user input as a DataFrame
def get_user_input():
    input_data = pd.DataFrame({
        'Beam Width (w in mm)': [w_mm],
        'Beam Height (h in mm)': [h_mm],
        'Effective Depth (d in mm)': [d_mm],
        'Beam C/C Span (mm)': [span_mm],
        'Shear Span (mm)': [shear_span_mm],
        'Tensile Strength (Fct in MPa)': [fct_mpa],
        'Compressive Strength (Fc in MPa)': [fc_mpa],
        'Elastic Modulus (Ec in GPa)': [ec_gpa],
        'Yield Strength (Fy in MPa)': [fy_mpa],
        'Steel Elastic Modulus (Es in GPa)': [es_gpa],
        'Rebar Diameter (Ø in mm)': [diameter_mm],
        'Number of Rebars': [num_rebars],
        'Area of Steel (As in mm²)': [as_mm2],
        'Applied Load (KN)': [load_kn]
    })
    return input_data

# Get user input
user_input = get_user_input()

# Display user input
# st.subheader('<div class="user_input">User Input Parameters</div>', unsafe_allow_html=True)

st.markdown('<div class="user_input">User Input Parameters</div>', unsafe_allow_html=True)
st.write(user_input)

# Combine all features into a single array
input_features = [
    w_mm, h_mm, d_mm, span_mm, shear_span_mm, fct_mpa, fc_mpa, ec_gpa,
    fy_mpa, es_gpa, diameter_mm, num_rebars, as_mm2, load_kn
]

# Add a Predict button
if st.button("Predict"):
    # Mock model prediction (replace with actual model later)
    prediction = np.sum(input_features) / 100  # Example prediction logic
    
    # Display the result with a styled container
    st.markdown(
        f"""
        <div class="result-container">
            Predicted Mid Span Deflection: <strong>{prediction:.3f} mm</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown('<div class="footer">Developed by <strong>Solomon Abe</strong> | Advisor: <strong>Tesfaye Alemu (Ph.D)</strong></div>', unsafe_allow_html=True)
