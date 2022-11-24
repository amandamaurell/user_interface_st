import streamlit as st

import numpy as np
import pandas as pd
from pages.page_01 import page1
from pages.page_02 import page2

st.markdown("""# This is a header
## This is a sub header
This is text
----
- this
- is
- a
- list
""")
with st.echo(): # I will have both the line of code and result
    st.checkbox('please, check me!')
 
df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df