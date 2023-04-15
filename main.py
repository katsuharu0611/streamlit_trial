import streamlit as st

import time


st.title("momimomi")

"プレぐれすばーの表示"

latest_iteration = st.empty()
bar=st.progress(50)

for i in range(100):
    latest_iteration.text(f"Iterartion{i+1}")
    bar.progress(i+1)
    time.sleep(0.02)

"done!!"



left_column,right_column=st.columns(2)

button=left_column.button("display the number on right column")
if button:
    right_column.write("kokohamigicolumn")


expander=st.expander("問い合わせ")
expander.write("toiawasenaiyouwokaku")


option=st.selectbox(
    "好きな数字を選べ",
    list(range(1,11))
)
"あなたの好きな数字は",option,"です"

text=st.text_input("telll me your hobby")
"your hobby:",text

condition=st.slider("あなたの今の調子は？",0,100,50)
"your condition:",condition