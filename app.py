import os
from google import genai
from google.genai import types
import streamlit as st

# Page setup
st.set_page_config(page_title="Agri Awareness Bot")
st.title("🌾 Agricultural Awareness Chatbot")


st.write("This bot explains crop life cycles and farming processes for educational purposes only.")




def generate():
    client = genai.Client(
        API_KEY = os.getenv("GOOGLE_API_KEY"),  
    )

    model = "gemini-3-flash-preview"
    # User input
    user_input = st.text_input("Ask about crop lifecycle or farming process:")
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="Explain crop lifecycle simply")
            ],
        )
    ]

    response = client.models.generate_content(
        model=model,
        contents=contents,
    )

    st.write(response.text)


if __name__ == "__main__":
    generate()
