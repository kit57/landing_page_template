import openai
import os
from langfuse import observe
import langfuse
from logger import init_logger
from dotenv import load_dotenv
from settings import Settings

from prompts import (
                        LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT,
                        LANDING_GENERAL_PAGE_TEMPLATE_PROMPT,
                        ROLE_PROMPT
                    )

logger = init_logger()
logger.info("OpenAI")
settings = Settings()

load_dotenv()

# Initialize OpenAI client with api key
client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

LANGFUSE_PUBLIC_KEY = os.getenv(settings.LANGFUSE_PUBLIC_KEY)
LANGFUSE_SECRET_KEY = os.getenv(settings.LANGFUSE_SECRET_KEY)

# Optional with defaults
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")


@observe(name='openai_call')
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

    with langfuse.start_as_current_generation(
                                        name="landing_page-generation",
                                        model="gpt-4o",
                                        input={"user_query": user_input}
                                    ) as generation:

        response = client.chat.completions.create(
                                    model="gpt-4o",
                                    messages=[
                                        {"role": "system", "content": ROLE_PROMPT},
                                        {"role": "user", "content": prompt}
                                    ],
                                    max_tokens=2500
                                    )

        generation.update(output=response,)
    
    return response.choices[0].message.content