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
