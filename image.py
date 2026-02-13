import streamlit as st
from openai import OpenAI, OpenAIError
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="AI Image Generator", layout="centered")

IMAGE_DIR = "generated_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

st.title("🎨 AI Image Generator")
st.write("Generate high-quality images safely using AI")

prompt = st.text_input(
    "Enter your image prompt:",
    placeholder="A cute baby panda drinking bubble tea, ultra realistic, 4k"
)

img_format = st.selectbox("Select image format:", ["PNG", "JPG"])

def save_and_show_image(image: Image.Image, prompt: str, img_format: str):
    img_index = len(os.listdir(IMAGE_DIR)) + 1
    filename = f"{IMAGE_DIR}/image_{img_index}.{img_format.lower()}"

    if img_format == "JPG":
        image = image.convert("RGB")

    image.save(filename)

    st.image(image, caption=prompt, use_column_width=True)

    with open(filename, "rb") as f:
        st.download_button(
            label=f"⬇️ Download {img_format}",
            data=f,
            file_name=os.path.basename(filename),
            mime=f"image/{img_format.lower()}"
        )

    st.success(f"Image saved successfully: {filename}")

if st.button("🚀 Generate Image"):

    if not prompt.strip():
        st.warning("Please enter a prompt first.")
        st.stop()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error(
            "❌ OPENAI_API_KEY not found.\n\n"
            "Please add your API key to the .env file:\n"
            "OPENAI_API_KEY=your_api_key_here"
        )
        st.stop()

    try:
       
        client = OpenAI(api_key=api_key)

        with st.spinner("Generating image..."):
            result = client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )

        image_url = result.data[0].url
        image_bytes = requests.get(image_url, timeout=30).content
        image = Image.open(BytesIO(image_bytes))

        save_and_show_image(image, prompt, img_format)

    except OpenAIError as e:
        st.error(f"OpenAI Error: {e}")

    except requests.exceptions.RequestException:
        st.error("Image download failed. Please check your internet connection.")

    except Exception as e:
        st.error(f"Unexpected error: {e}")
