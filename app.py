# import streamlit as st
# import joblib
# import numpy as np

# # Set the page configuration (must be the first Streamlit command)
# st.set_page_config(page_title="Mid Span Deflection Predictor", layout="centered")

# # Inject custom CSS styles
# st.markdown(
#     """
#     <style>
#     /* Page background and styling */
#     .stApp {
#         background-color: #808080; /* Light gray background */
#     }

#     /* Title styling */
#     .title {
#         font-size: 36px;
#         font-weight: bold;
#         color: #4CAF50; /* Greenish color */
#         text-align: center;
#         margin-top: 20px;
#         margin-bottom: 10px;
#     }

#     /* Description styling */
#     .description {
#         font-size: 18px;
#         color: #555; /* Grayish color */
#         text-align: center;
#         line-height: 1.6;
#         margin-bottom: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Use the styled HTML for the title and description
# st.markdown('<div class="title">Mid Span Deflection Prediction App Using Random Forest ML</div>', unsafe_allow_html=True)
# st.markdown('<div class="description">This app predicts the <strong>Mid Span Deflection</strong> of reinforced concrete beams based on input features.</div>', unsafe_allow_html=True)



# # yesssssssssssssssssss


# # Load the trained Random Forest model
# # model = joblib.load("random_forest_final_model.pkl")

# # # Must be the first Streamlit command
# # st.set_page_config(page_title="Mid Span Deflection Predictor", layout="centered")

# # st.title("Mid Span Deflection Prediction App Using Random Forest ML")
# # st.write(
# #     "This app predicts the **Mid Span Deflection** of reinforced concrete beams based on input features."
# # )

# # Sidebar for input features
# st.sidebar.header("Input Features")
# w_mm = st.sidebar.number_input("Beam Width (w in mm)", min_value=100, max_value=1000, value=200)
# h_mm = st.sidebar.number_input("Beam Height (h in mm)", min_value=100, max_value=1000, value=300)
# d_mm = st.sidebar.number_input("Effective Depth (d in mm)", min_value=100, max_value=1000, value=250)
# span_mm = st.sidebar.number_input("Beam C/C Span (mm)", min_value=500, max_value=10000, value=5000)
# shear_span_mm = st.sidebar.number_input("Shear Span (mm)", min_value=500, max_value=5000, value=1500)
# fct_mpa = st.sidebar.number_input("Tensile Strength (Fct in MPa)", min_value=1.0, max_value=10.0, value=3.2)
# fc_mpa = st.sidebar.number_input("Compressive Strength (Fc in MPa)", min_value=10.0, max_value=100.0, value=30.0)
# ec_gpa = st.sidebar.number_input("Elastic Modulus (Ec in GPa)", min_value=10.0, max_value=50.0, value=20.0)
# fy_mpa = st.sidebar.number_input("Yield Strength (Fy in MPa)", min_value=100, max_value=1000, value=500)
# es_gpa = st.sidebar.number_input("Steel Elastic Modulus (Es in GPa)", min_value=100, max_value=300, value=200)
# diameter_mm = st.sidebar.number_input("Rebar Diameter (Ø in mm)", min_value=5.0, max_value=50.0, value=16.0)
# num_rebars = st.sidebar.number_input("Number of Rebars", min_value=1, max_value=20, value=4)
# as_mm2 = st.sidebar.number_input("Area of Steel (As in mm²)", min_value=100.0, max_value=5000.0, value=800.0)
# load_kn = st.sidebar.number_input("Applied Load (KN)", min_value=0.0, max_value=200.0, value=50.0)

# # Combine all features into a single array
# input_features = [
#     w_mm, h_mm, d_mm, span_mm, shear_span_mm, fct_mpa, fc_mpa, ec_gpa,
#     fy_mpa, es_gpa, diameter_mm, num_rebars, as_mm2, load_kn
# ]

# # Add a Predict button

# if st.button("Predict"):

#     # Convert the features to a NumPy array and reshape for prediction

#     features_array = np.array(input_features).reshape(1, -1)
    
#     # Make a prediction using the model

#     prediction = model.predict(features_array)
    
#     # Display the result

#     st.success(f"Predicted Mid Span Deflection: {prediction[0]:.3f} mm")

# # Footer

# st.write("Developed by **Solomon Abe**")
# st.write("Adivisor **Tesfaye Alemu(Ph.D)**")






import streamlit as st
import joblib
import numpy as np

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Mid Span Deflection Predictor", layout="centered")

# Inject custom CSS styles
st.markdown(
    """
    <style>
    /* Background and overall layout */
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
        padding: 20px;
    }

    /* Title styling */
    .title {
        font-size: 40px;
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

    [data-testid="stSidebar"] input {
        border: 1px solid #e9c46a;
        border-radius: 5px;
        padding: 5px;
    }

    /* Buttons */
    button {
        background-color: #2a9d8f;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s ease;
    }

    button:hover {
        background-color: #e76f51; /* Highlight on hover */
        color: white;
    }

    /* Footer */
    .footer {
        font-size: 14px;
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

# Combine all features into a single array
input_features = [
    w_mm, h_mm, d_mm, span_mm, shear_span_mm, fct_mpa, fc_mpa, ec_gpa,
    fy_mpa, es_gpa, diameter_mm, num_rebars, as_mm2, load_kn
]

# Add a Predict button
if st.button("Predict"):
    # Mock model prediction (replace with actual model later)
    prediction = np.sum(input_features) / 100  # Example prediction logic
    
    # Display the result
    st.success(f"Predicted Mid Span Deflection: {prediction:.3f} mm")

# Footer
st.markdown('<div class="footer">Developed by <strong>Solomon Abe</strong> | Advisor: <strong>Tesfaye Alemu (Ph.D)</strong></div>', unsafe_allow_html=True)
