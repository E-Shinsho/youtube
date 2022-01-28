import streamlit as st 
import numpy as np 
import pandas as pd 
from PIL import Image
import time 
st.title('Streamlit')
st.write('DataFrame')
'Start !'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# left_column, right_column = st.columns(2)

# button = left_column.button('right column')
# if button:
#     right_column.write('aaaaa')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')