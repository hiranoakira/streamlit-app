'''
import streamlit as st 
import random
if st.button("label"):
    random.number = random.randint(1,100)
'''    

import streamlit as st 
import random
if st.button("label"):
    number = random.randint(1,1000)
    st.write(number)