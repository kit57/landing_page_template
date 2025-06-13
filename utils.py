import openai
import os
from logger import init_logger
from dotenv import load_dotenv

from prompts import (
                        LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT,
                        LANDING_GENERAL_PAGE_TEMPLATE_PROMPT,
                        ROLE_PROMPT
                    )

logger = init_logger()
logger.info("OpenAI")

load_dotenv()

# Initialize OpenAI client with api key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_landing_page(user_input: str) -> str:
    """
    Generates a landing page HTML string based on user input.
    """

    if user_input.strip():
        logger.info('Generating landing page with custom prompt')
        prompt = LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT
    else:
        logger.info('Generating landing page with general prompt')
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