

import os
from dotenv import load_dotenv

class Settings:
    def __init__(self):
        # Load .env file
        load_dotenv()

        # Required variables
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
        self.LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
        self.LANGFUSE_HOST = os.getenv("LANGFUSE_HOST")


    def _validate(self):
        missing = []
        if not self.OPENAI_API_KEY:
            missing.append("OPENAI_API_KEY")
        if not self.LANGFUSE_PUBLIC_KEY:
            missing.append("LANGFUSE_PUBLIC_KEY")
        if not self.LANGFUSE_SECRET_KEY:
            missing.append("LANGFUSE_SECRET_KEY")

        if missing:
            raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")