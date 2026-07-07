import streamlit as st

st.title("welcome to my website")
st.header("python")
st.subheader("javascript")
st.markdown("i love python")
name = st.text_input("enter your name")
fname = st.text_input("enter your fathers name")
adr = st.text_area("enter your text")
classdata = st.selectbox("enter your class :",(1,2,3,4,5))

button = st.button("done ")
if button:
    st.markdown(f"""
    Name : {name}
    fathers name : {fname}
    address : {adr}
    class : {classdata}""")

     
