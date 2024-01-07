from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

model=genai.GenerativeModel("gemini-pro-Image") 

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Promethean Advisor")
st.header("Promethean Advisor with Image recognizance")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Go With Promethean Advisor")

## If ask button is clicked

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)