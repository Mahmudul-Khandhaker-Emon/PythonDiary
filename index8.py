import streamlit as st

import io 

from PIL import Image 

import google.generativeai as genai

import os

from dotenv import  load_dotenv

load_dotenv()

API_KEY = os.getenv("api_key") 


genai.configure(api_key=API_KEY)



Baby_model=genai.GenerativeModel("models/gemini-2.5-flash")

st.title("Welcome to You Our Mini-Chatgpt model")

st.markdown("**This model will always help You.**")


st.write("**Say Your Statement/Opinion:**")


User_question_Prompt= st.text_input("Baby Lekho")

User_uploaded_image=st.file_uploader("Baby Upload koro Image")


if User_uploaded_image is not None:
    image_object=Image.open(User_uploaded_image)
    st.image(image_object)

    if User_question_Prompt.strip().lower()=="what is your name":
       st.write("**My Name is Baby Bolo I love You---MINICHATGPT**")
   
    elif  User_question_Prompt:
        response = Baby_model.generate_content([User_question_Prompt,image_object])
        st.write(response.text)


else:
    if User_question_Prompt.strip().lower()=="what is your name":
       st.write("**My Name is Baby Bolo I love You---MINICHATGPT**")

    elif User_question_Prompt:
     response=Baby_model.generate_content([User_question_Prompt])
     st.write(response.text)