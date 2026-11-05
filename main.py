import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter PKR amount to convert", min_value=1)
target_currency = st.selectbox("Select target currency", ["USD", "EUR", "GBP", "JPY", "CAD"])
if st.button("Convert"):
    url= "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amount
        st.success(f"{amount} PKR is equal to {converted:.2f} {target_currency}")
    else:
        st.error("failed to fetch exchange rates. Please try again later.")