# cd /Users/yuxiangzhang/SynologyDrive/python/功能类/web_api/streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.title("streamlit demo")

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)


import matplotlib.pyplot as plt
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

mark = f"""
# markdown一级标题
普通文字
### markdown三级标题
***markdown粗斜体***
- hello 
- world
- China
"""
st.markdown(mark )

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)