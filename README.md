# 🎨 AI Image Generator

A **Streamlit app** to generate stunning images using OpenAI's DALL·E 3 / GPT Image API.  
Users can enter a prompt, select image format (PNG/JPG), and download the generated images.

---

## 🔑 Features

- Generate high-quality AI images with custom prompts
- Save images locally in `generated_images` folder
- Download images directly from the app
- Supports PNG and JPG formats
- Safe `.env`-based API key handling
- Robust error handling: missing key, invalid prompt, network errors

---

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/<username>/image-generator.git
cd image-generator


2. Create a virtual environment

python -m venv venv
source venv/bin/activate 
venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt


Create a .env file in the root folder with your OpenAI API key:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

## 🚀 Run the App

streamlit run image.py


- Enter your prompt in the text box
- Select image format (PNG or JPG)
- Click Generate Image
- View and download the generated image

Recommended Prompts

- A cute baby panda drinking bubble tea, ultra realistic, 4k
- A futuristic cyberpunk city at night with neon lights, flying cars, cinematic
- A magical forest with glowing plants and floating lights, digital art

Add: ultra detailed, high resolution, cinematic lighting, 4k for best results
