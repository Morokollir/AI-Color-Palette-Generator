import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_color_palette(theme):
    prompt = (
        f"Generate a creative color palette for the following theme: '{theme}'. "
        "Return the hex color codes in a comma-separated list."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert color designer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    theme = input("Enter a theme or mood for the color palette: ")
    palette = generate_color_palette(theme)
    print("\nGenerated Color Palette:\n", palette)
