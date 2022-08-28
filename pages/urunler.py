import streamlit as st
st.set_page_config(layout="wide")
st.header("Ürünler")
from functions import *

with st.expander("Ürün Ekle"):
    with st.form("urunekle", clear_on_submit=True):
        isim=st.text_input("Ürün İsmi")
        model=st.selectbox("Model seç",listele("modeller"))
        model=str(model)
        fiyat=st.number_input("Fiyat Giriniz")
        submitted=st.form_submit_button("Ürün ekle")
        if submitted:
         urunekle(isim,model,fiyat)

tabloyap("urunler",["İsim","Model","Fiyat"])