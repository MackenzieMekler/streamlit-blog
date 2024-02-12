import streamlit as st

# doing the sidebar stuff
sidebar = st.sidebar

with st.sidebar:
    st.header("somephdstudent")
    st.subheader("Mackenzie Mekler")
    st.button("Home")
    st.button("About Me")
    st.button("Posts")
    st.caption("Made with Streamlit")

# homepage

st.write("Exploring Academia")
st.write("Sharing my educational experiences and scientific work with you. Join me in my adventure")
st.button("Learn More")


