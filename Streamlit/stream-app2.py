import streamlit as st
import pandas as pd
import pickle
from PIL import Image

st.markdown(
    """
    <h1 style='text-align: center;'>Evaluation Later or Audit !?</h1>
    """,
    unsafe_allow_html=True
)

st.divider()

# Create a 4x2 grid for radio buttons
col1, col2 = st.columns(2)

# Define radio button options
ratings = ["1", "2", "3", "4", "5"]

# Column 1
with col1:

    ENTRANCE_DOORS_WINDOWS = st.radio(
        "***Score your apartment entrance doors/windows:***",
        ratings, key="entrance_doors_windows",
        horizontal=True
    )

    ENTRANCE_LOBBY = st.radio(
        "***Score your apartment entrance lobby:***",
        ratings, key="entrance_lobby",
        horizontal=True
    )

    EXTERIOR_GROUNDS = st.radio(
        "***Score your apartment exterior grounds:***",
        ratings, key="exterior_grounds",
        horizontal=True
    )

    INTERIOR_LIGHTING_LEVELS = st.radio(
        "***Score your apartment interior lighting levels:***",
        ratings, key="interior_lighting_levels",
        horizontal=True
    )

# Column 2
with col2:

    INTERIOR_WALL_CEILING_FLOOR = st.radio(
        "***Score your apartment wall, ceiling, and floor:***",
        ratings, key="interior_wall_ceiling_floor",
        horizontal=True
    )

    STAIRWELLS = st.radio(
        "***Score your apartment stairwells:***",
        ratings, key="stairwells",
        horizontal=True
    )

    WATER_PEN_EXT_BLDG_ELEMENTS = st.radio(
        "***Score your apartment water infiltration in building components:***",
        ratings, key="water_pen_ext_bldg_elements",
        horizontal=True
    )

    SECURITY = st.radio(
        "***Score your apartment security:***",
        ratings, key="security",
        horizontal=True
    )

# Create the input DataFrame
input_data = {
    'ENTRANCE_DOORS_WINDOWS': ENTRANCE_DOORS_WINDOWS,
    'ENTRANCE_LOBBY': ENTRANCE_LOBBY,
    'INTERIOR_WALL_CEILING_FLOOR': INTERIOR_WALL_CEILING_FLOOR,
    'WATER_PEN_EXT_BLDG_ELEMENTS': WATER_PEN_EXT_BLDG_ELEMENTS,
    'EXTERIOR_GROUNDS': EXTERIOR_GROUNDS,
    'INTERIOR_LIGHTING_LEVELS': INTERIOR_LIGHTING_LEVELS,
    'STAIRWELLS': STAIRWELLS,
    'SECURITY': SECURITY
}
input_df = pd.DataFrame([input_data])

# Load the model
with open('../models/dt_model23.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Predict
predicted_result = loaded_model.predict(input_df)

st.divider()


# Determine the message based on predicted_result
if predicted_result[0] == 0:
    message = "<span style='color:red;'>Building Audit</span>"
elif predicted_result[0] == 1:
    message = "Evaluation needs to be conducted in 1 year"
elif predicted_result[0] == 2:
    message = "Evaluation needs to be conducted in 2 years"
elif predicted_result[0] == 3:
    message = "Evaluation needs to be conducted in 3 years"
else:
    message = "Unexpected prediction result"

# Display the predicted score and message to the user
st.markdown(
    f"""
    <div style="text-align: center;">
        <h2>Predicted Apartment result:</h2>
        <h3>{message}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.divider()
st.divider()

image = Image.open('decisiontree.png')

st.image(image)
