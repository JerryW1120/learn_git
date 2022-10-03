import streamlit as st

# 创建两个日期选择模块，一个是起始日期，一个是结束日期
st.header("开始日期")
start_date = st.date_input('选择起始日期')
st.header("结束日期")
end_date = st.date_input('选择结束日期')
# 计算两个日期差了多少天
delta = end_date - start_date
# 在网页上打印结果
st.header('相差 `%s` 天' % delta.days)