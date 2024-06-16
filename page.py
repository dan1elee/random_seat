import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(
    page_title="主页",
    page_icon="👋",
    layout="wide"
)
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file,encoding='gbk')
    st.dataframe(df, width=600) 
    lines = df.shape[0]
    num_list = list(range(1, lines+1))
    name_column = st.selectbox('选择姓名列', df.columns)
    seat_column = st.text_input('输入座位号列的名称', value="座位号")
    if seat_column in df.columns:
        st.write("- 座位号列名称重复，请重新输入")
    else:
        allocate = st.button('开始随机分配')
        if allocate:
            progress_bar = st.progress(0)
            status_text = st.empty()
            for i in range(lines):
                random.seed(time.time())
                rand_seat = random.choice(num_list)
                num_list.remove(rand_seat)
                df.loc[i, seat_column] = rand_seat
                st.write(f'- 随机分配{df.loc[i, name_column]}同学到第{rand_seat}个座位')
                # 更新进度条
                progress = (i+1)/lines
                progress_bar.progress(progress)
                status_text.text(f'进度: {round(progress*100)}%')
                time.sleep(0.5)

            st.write("- 分配结果")
            st.dataframe(df, width=600)