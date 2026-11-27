import os

from openai import OpenAI
from dotenv import load_dotenv

# Load environments
load_dotenv()

# Models Defined
MODEL = "openai/gpt-oss-120b"
DEFAULT_EMBEDDING_MODEL = "nvidia/nemotron-3.5-embed-8b:free"



def create_embeddings(texts):
    # Client built on first use, so the app and offline tests import without a key
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY") or os.getenv("OPEN_ROUTER_KEY"),
    )
    response = client.embeddings.create(
        model=os.getenv("EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL),
        input=texts,
        encoding_format="float",
    )
    return [item.embedding for item in response.data]
