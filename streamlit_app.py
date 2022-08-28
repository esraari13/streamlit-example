import streamlit as st
st.set_page_config(layout="wide")
st.header("Ana sayfa")
from functions import *
st.subheader("Günün Randevuları")
gununrandevu()

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
