import streamlit as st
import google.generativeai as gen_ai
from PIL import Image
import os
from gtts import gTTS
import base64
import re
from datetime import datetime

# Configure Gemini API
gen_ai.configure(api_key="YOUR_API_BRO")
gemini = gen_ai.GenerativeModel("gemini-1.5-flash")

def strip_markdown(text):
    """Removes Markdown syntax."""
    return re.sub(r"[*_~]", "", text)

def text_to_speech(text):
    """Generates an audio player from text."""
    plain_text = strip_markdown(text)
    tts = gTTS(text=plain_text, lang='en')
    audio_file_path = "temp_audio.mp3"
    tts.save(audio_file_path)
    
    with open(audio_file_path, 'rb') as audio_file:
        audio_bytes = audio_file.read()
    
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    os.remove(audio_file_path)
    
    return f"""
        <audio controls>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #F8F9FA;
            font-family: 'Arial', sans-serif;
        }
        .navbar {
            background-color: #2C3E50;
            padding: 15px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #16A085;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #138D75;
        }
        .stFileUploader input {
            border: 2px solid #2C3E50;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation State
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Home Page
if st.session_state.page == "Home":
    st.markdown("<div class='navbar'>VisionAid.ai - AI Image Based Educator</div>", unsafe_allow_html=True)
    st.title("🔍 Welcome to VisionAid.ai")
    #st.image("14086516.jpg", width=100)
    st.markdown("### AI-powered Image Analysis VisualEd Technology!")
    st.markdown("#### The educational apllication that allows users understand the input images with the availabilty of audio, giving a personalised touch.")
    st.markdown('#### Created by Shreyash Srivastva for fellow Humans.')
    if st.button("Get Started 🚀"):
        st.session_state.page = "Upload Image"
        
# Code Block to Upload Image
if st.session_state.page == "Upload Image":
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    if uploaded_image:
        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())
        
        image = Image.open(image_path)
        st.image(image, caption="Uploaded Image", width=300)

        # image analysis
        with st.spinner("Analyzing image..."):
            gemini_file = gen_ai.upload_file(path=image_path, display_name=os.path.basename(image_path))
            response = gemini.generate_content([gemini_file, "Describe this image."])
            description = response.text

        # Results
        st.success("Analysis Complete!")
        st.markdown(f"**AI Description:** {description}")
        st.markdown(text_to_speech(description), unsafe_allow_html=True)
        
        os.remove(image_path)
    else:
        st.info("Upload an image to get started!")
