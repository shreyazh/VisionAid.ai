# VisionAid.AI - AI-Powered Image ChatBot

## 🌟 Overview
VisionAid.AI is a powerful AI-driven image analysis tool built using Streamlit and Google's Gemini AI. This application allows users to upload images and interact with an AI chatbot that can describe, analyze, and respond to queries about the uploaded image.

## 🚀 Features
- **Image Upload & Analysis**: Upload images for AI-powered descriptions and analysis.
- **AI Chatbot**: Ask questions related to the uploaded image.
- **Text-to-Speech**: Converts AI-generated descriptions to audio.
- **Dynamic UI**: Aesthetic and interactive interface using custom CSS.
- **Seamless Navigation**: Start from a landing page and navigate easily.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI Model**: Google Gemini API (gemini-1.5-flash)
- **Backend**: Python
- **Audio Processing**: gTTS (Google Text-to-Speech)
- **Image Handling**: PIL (Pillow)

## 📌 Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/shreyazh/VisualAid.AI.git
   cd VisionAid-AI
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up API Key**
   - Replace `YOUR_GEMINI_API_KEY` in the script with your Google Gemini API key.

5. **Run the Application**
   ```sh
   streamlit run app.py
   ```

## 📷 Usage
1. **Launch the app** and start from the landing page.
2. **Click "Get Started"** to navigate to the Upload Image page.
3. **Upload an image**, and the AI will analyze it.
4. **View the AI-generated description** and listen to the text-to-speech output.
5. **Chat with the AI** about the image.

## 🎨 UI Enhancements
- Stylish **navigation bar**
- Animated **buttons and inputs**
- Responsive **image display**
- Custom **Streamlit styling**

## 🏗️ Future Improvements
- Add support for **real-time image processing**.
- Implement **multilingual support** for text-to-speech.
- Enhance chatbot responses with **contextual memory**.

## 🤝 Contributing
We welcome contributions! Feel free to fork the repo and submit PRs.

## 📜 License
This project is licensed under the MIT License.

---
🎯 **Developed with ❤️ using Python**

