import streamlit as st

import os

import google.generativeai as genai

from PIL import Image

from gtts import gTTS

import io

from dotenv import load_dotenv

load_dotenv()



API_KEY = os.getenv("api_key")





genai.configure(api_key=API_KEY)



Baby_model = genai.GenerativeModel("models/gemini-2.5-flash")



st.title("Chat-gpt Mini Model-version2 🏃")

st.markdown("**Think better, acquire success.**")



logo_url = "https://i.pinimg.com/236x/75/96/ca/7596ca7de195b18377e4aece6d077aeb.jpg"



st.logo(logo_url)



image_url="https://i.pinimg.com/236x/75/96/ca/7596ca7de195b18377e4aece6d077aeb.jpg"



st.image(image=image_url,caption="**Go Ahed on Your Specific Goal**",use_container_width=True)



def speak_text(text_to_speak):
    tts =gTTS(text=text_to_speak,lang='en')
    audio_buffer= io.BytesIO()

    tts.write_to_fp(audio_buffer)

    audio_buffer.seek(0)
    st.markdown("**🔊 Listen to the response:**")
    st.audio(audio_buffer, format='audio/mp3')


user_Prompt = st.text_input("**Write Your Statement:**")

if user_Prompt.strip().lower() == "what is your name?":



    st.write("😚My name is Baby Gemini, your mini AI assistant!")

elif user_Prompt:

    st.warning("আমি এই সংস্করণে শুধু 'what is your name?' প্রশ্নের উত্তর দিতে পারি।")

user_uploaded_images = st.file_uploader("**Upload your image Here:**", type=["jpg", "jpeg", "png"])

if user_uploaded_images:

    image_object = Image.open(user_uploaded_images)
    

    st.image(image_object, caption="Uploaded Image", width=300)
    
    if st.button("Generate 5 Mcq 📝"):
        with st.spinner("Generating MCQs from your image..."):
            Baby_instruction = "Analyze this image and create 5 high-quality Multiple Choice Questions (MCQs) with options and the correct answers."
            
            response = Baby_model.generate_content([Baby_instruction, image_object])
            
            st.success("Successfully Generated!")
            st.write(response.text)
            st.write(response.text)
            speak_text(response.text)



