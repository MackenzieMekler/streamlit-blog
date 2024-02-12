import streamlit as st

# doing the sidebar stuff
sidebar = st.sidebar

with st.sidebar:
    st.markdown("<h1 style='color:#1473f7;'>somephdstudent</h1>", unsafe_allow_html=True)
    st.subheader("Mackenzie Mekler")
    st.button("About Me")
    st.button("Posts")
    st.caption("Made with Streamlit")

# homepage

st.write("Exploring Academia")
st.markdown(""" Hi everyone! My name is Mackenzie Mekler and I am an undergraduate at the University of Florida. I am graduating in the spring of 2024 with a degree in Microbiology and Cell Science and moving forwards into a Ph.D. program in Cancer Biology (most likely). I am passionate about teaching and researching the sciences. This has led me to pursue a Ph.D. as well as start this blog. When I am not researching I am typically playing any of a hundred different sports or neck deep in a random project. 

In this blog I am hoping to document my journey through academia from my undergraduate (and maybe even high school) all the way through my PhD and into whatever steps await me next. I noticed that there are not a lot of resources online about applying to Ph.D. programs and when compared to medicine or other disciplines in the sciences, there is just not a lot of information period. I am hoping to change this a little by adding my journey through this field, what I learn, what path I choose to take, what paths I don’t choose to take, and anything else I encounter on the way. Hopefully this can serve to help whoever finds it to begin exploring different possibilities and careers within the sciences as well as warn for the downsides of these paths. 

Along the way I hope to share some of my passions including my research, my coding projects, and any of my other passions. 

Thank you for giving me some of your time and I hope you enjoy!!

""")

