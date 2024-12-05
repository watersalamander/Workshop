import streamlit as st

st.set_page_config(page_title="Allocation",
                   layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://moneyexpo.net/wp-content/uploads/2024/04/Merkel.jpg", use_column_width=True)
  
st.title("Workshop 1")

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
    total_return = ((gold*135)+(bitcoin*400000)+(reits*140)+(stock*128)+(bond*63))*0.01
    st.write("10Y Return: ", total_return, "%")

    volatility = ((gold*25)+(bitcoin*83)+(reits*74)+(stock*35)+(bond*54))*0.01
    st.write("Maximum Drawdown: ", volatility, "%")
