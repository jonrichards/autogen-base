from autogen import ConversableAgent
from base.base_logger import logger
from base.oai_config import gpt_config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Example of using the ConversableAgent class
agent = ConversableAgent("chatbot", llm_config=gpt_config, human_input_mode="NEVER")
reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
logger.debug(reply)
print(reply)
