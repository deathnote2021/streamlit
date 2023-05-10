# cd /Users/yuxiangzhang/SynologyDrive/python/功能类/web_api/streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import os
import oss2
st.title("streamlit demo") #最上面的标题

# 交互
## 输入框
name = st.text_input('请输入姓名', value='',key='name') #输一个就会刷新一次
score = st.text_input('请输入成绩', value='',key='score')
output = st.empty()
savepath= 'database.csv'
if not os.path.exists(savepath):
    file_handle=open(savepath,mode='w',encoding='utf-8')  
    file_handle.write('name,value'+'\n') # 记得换行
    file_handle.close()   #关了 当前才会保存 
if st.button('提交'):
#if len(name)>0:
    output = "hello " + name
    st.write(output)
## 计入数据库 
    file_handle=open(savepath,mode='a',encoding='utf-8')  
    file_handle.write(f'{name},{score}'+'\n') 
    file_handle.close()
    
st.markdown('---')
## slider
x = st.slider('x')
st.write(x, 'squared is', x * x)

# box展示
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# markdown
st.markdown('---')
mark = f"""
# markdown一级标题
普通文字
### markdown三级标题
***markdown粗斜体***
- hello 
- world
- China
"""
st.markdown(mark)

#可视化
## hist
import matplotlib.pyplot as plt
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

## 柱状图
data = {'date': ['2022-05-01', '2022-05-02', '2022-05-03', '2022-05-04', '2022-05-05'],
        'count': [10, 20, 15, 30, 25]}
df = pd.DataFrame(data)
fig, ax = plt.subplots(figsize=(10, 6)) # 创建一个新的图形
ax.bar(df['date'], df['count']) # 创建柱状图
ax.set_xlabel('Date') # 设置 x 轴标签
ax.set_ylabel('Count') # 设置 y 轴标签
ax.set_title('Daily Count') # 设置标题
st.pyplot(fig)

## 线图
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 数据table
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)
## 读取现成的
df = pd.read_csv(savepath)
st.write(df)
