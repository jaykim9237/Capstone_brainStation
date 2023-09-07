import streamlit as st
import pandas as pd
import pickle
from PIL import Image


st.markdown(
    """
    <h1 style='text-align: center;'>Evaluate Your Apartment</h1>
    """,
    unsafe_allow_html=True
)
# Apply Markdown styling to the titles

st.divider()

# Create a 3x2 grid for sliders
col1, col2 = st.columns(2, gap="medium")

# Column 1
with col1:

    ENTRANCE_LOBBY = st.slider(
        "***Score your apartment entrance lobby:***",
        1, 5, key="entrance_lobby"
    )

    EXTERIOR_GROUNDS = st.slider(
        "***Score your apartment exterior grounds:***",
        1, 5, key="exterior_grounds"
    )

    STAIRWELLS = st.slider(
        "***Score your apartment stairwells:***",
        1, 5, key="stairwells"
    )

# Column 2
with col2:
    INTERIOR_WALL_CEILING_FLOOR = st.slider(
        "***Score your apartment wall, ceiling, and floor:***",
        1, 5, key="interior_wall_ceiling_floor"
    )

    INTERIOR_LIGHTING_LEVELS = st.slider(
        "***Score your apartment interior lighting levels:***",
        1, 5, key="interior_lighting_levels"
    )

    WATER_PEN_EXT_BLDG_ELEMENTS = st.slider(
        "***Score your apartment water infiltration in building components:***",
        1, 5, key="water_pen_ext_bldg_elements"
    )

df = pd.DataFrame([['ENTRANCE_LOBBY', 'EXTERIOR_GROUNDS', 'STAIRWELLS', 'INTERIOR_WALL_CEILING_FLOOR', 'INTERIOR_LIGHTING_LEVELS', 'WATER_PEN_EXT_BLDG_ELEMENTS']])

input_data = {
    'ENTRANCE_LOBBY': ENTRANCE_LOBBY,
    'EXTERIOR_GROUNDS': EXTERIOR_GROUNDS,
    'STAIRWELLS': STAIRWELLS,
    'INTERIOR_WALL_CEILING_FLOOR': INTERIOR_WALL_CEILING_FLOOR,
    'INTERIOR_LIGHTING_LEVELS': INTERIOR_LIGHTING_LEVELS,
    'WATER_PEN_EXT_BLDG_ELEMENTS': WATER_PEN_EXT_BLDG_ELEMENTS
}
input_df = pd.DataFrame([input_data])


# load the model
with open('../models/rf_model8.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# predict
predicted_score = loaded_model.predict(input_df)
rounded_predicted_score = round(predicted_score[0], 2)


st.divider()

# Display the predicted score to the user
st.markdown(
    """
    <div style="text-align: center;">
        <h2>Predicted Apartment Score:</h2>
        <h3>{:.2f} %</h3>
    </div>
    """.format(rounded_predicted_score),
    unsafe_allow_html=True
)


st.divider()
st.divider()
st.divider()

image = Image.open('rf-regression.png')

st.image(image)