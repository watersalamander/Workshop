import streamlit as st

st.set_page_config(page_title="Allocation",
                   layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://moneyexpo.net/wp-content/uploads/2024/04/Merkel.jpg", use_column_width=True)

col4, col5, col6 = st.columns([1,1,1])
with col5:
    st.header("Workshop 1")

gold = st.number_input('Percentage in Gold',
                       min_value=0.0,
                       max_value=100.0,
                       value=20.0,
                       step=10.0)
bitcoin = st.number_input('Percentage in Bitcoin',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=10.0)
reits = st.number_input('Percentage in REITs',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=10.0)
stock = st.number_input('Percentage in Stock',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=10.0)
bond = st.number_input('Percentage in Bond',
                        min_value=0.0,
                        max_value=100.0,
                        value=20.0,
                        step=10.0)

button = st.button('Calculate')

if button:
    total_return = ((gold*29.52)+(bitcoin*143.95)+(reits*12.34)+(stock*22.08)+(bond*4.45))*0.01
    st.write("1-Year Return: ", total_return, "%")

    volatility = ((gold*15)+(bitcoin*72.9)+(reits*22.7)+(stock*19.6)+(bond*6.4))*0.01
    st.write("1-Year Volatility: ", volatility, "%")
