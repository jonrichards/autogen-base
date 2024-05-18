import os
import random

import autogen
from base.base_logger import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load OpenAI model and API key info
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")
logger.debug(config_list)

# Load configs for desired model
GPT_MODEL = os.environ.get("GPT_MODEL", "gpt-3.5-turbo")
if GPT_MODEL == "gpt-4-turbo":
    # Load OpenAI gpt4turbo model config from env, or file
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-4-turbo"],
        },
    )
elif GPT_MODEL == "gpt-4o":
    # Load OpenAI gpt4o model config from env, or file
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-4o"],
        },
    )
else:
    # Load OpenAI gpt35turbo model config from env, or file
    config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-3.5-turbo"],
        },
    )

# Log model config
logger.debug(config_list)

# Load LLM settings from env
CACHE_SEED = int(os.environ.get("CACHE_SEED", random.randint(1, 1000000)))
logger.debug("CACHE_SEED: %s", CACHE_SEED)

TEMPERATURE = int(os.environ.get("TEMPERATURE", "0"))
logger.debug("TEMPERATURE: %s", TEMPERATURE)

TIMEOUT = int(os.environ.get("TIMEOUT", "300"))
logger.debug("TIMEOUT: %s", TIMEOUT)

# Set up GPT config
gpt_config = {
    "timeout": TIMEOUT,
    "cache_seed": CACHE_SEED,
    "config_list": config_list,
    "temperature": TEMPERATURE,
}

logger.debug("GPT Config: %s", gpt_config)
