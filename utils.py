import openai
import os

from prompts import LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT, LANDING_GENERAL_PAGE_TEMPLATE_PROMPT, ROLE_PROMPT

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI()

def generate_landing_page(user_input):

    if user_input.strip():
        prompt = LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT
    else:
        prompt = LANDING_GENERAL_PAGE_TEMPLATE_PROMPT

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": ROLE_PROMPT},
        {"role": "user", "content": prompt}
    ],
    max_tokens=2500
    )
    
    return response.choices[0].message.content