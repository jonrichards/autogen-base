import autogen
from autogen import ConversableAgent
from autogen.agentchat.contrib import img_utils
from autogen.agentchat.contrib.capabilities import generate_images
from autogen.agentchat.contrib.capabilities.generate_images import ImageGeneration
from autogen.cache import Cache
from autogen.oai import openai_utils
from base.base_logger import logger
from base.oai_config import gpt_config, image_config
from dotenv import load_dotenv
from IPython.display import display
from PIL.Image import Image

# Load environment variables
load_dotenv()

# Example of using the ConversableAgent class
gpt_agent = ConversableAgent("chatbot", llm_config=gpt_config, human_input_mode="NEVER")
reply = gpt_agent.generate_reply(
    messages=[{"content": "Tell me a joke.", "role": "user"}]
)
logger.debug(reply)
print(reply)
