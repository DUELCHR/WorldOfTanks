import classes.application_class as application_class 
import os
import streamlit as st

application_id = st.secrets["application_id"]

app = application_class.Application( id = application_id )
app.run()
