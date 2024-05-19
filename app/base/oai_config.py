import os
import random

import autogen
from base.base_logger import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load settings from env
CACHE_SEED = int(os.environ.get("CACHE_SEED", random.randint(1, 1000000)))
logger.debug("CACHE_SEED: %s", CACHE_SEED)
TEMPERATURE = int(os.environ.get("TEMPERATURE", "0"))
logger.debug("TEMPERATURE: %s", TEMPERATURE)
TIMEOUT = int(os.environ.get("TIMEOUT", "300"))
logger.debug("TIMEOUT: %s", TIMEOUT)

# Log OpenAI model and API key info
logger.debug(autogen.config_list_from_json("OAI_CONFIG_LIST"))

# Load configs for desired GPT model
GPT_MODEL = os.environ.get("GPT_MODEL", "gpt-3.5-turbo")
if GPT_MODEL == "gpt-4-turbo":
    # Load OpenAI gpt4turbo model config from env, or file
    gpt_config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-4-turbo"],
        },
    )
elif GPT_MODEL == "gpt-4o":
    # Load OpenAI gpt4o model config from env, or file
    gpt_config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-4o"],
        },
    )
else:
    # Load OpenAI gpt35turbo model config from env, or file
    gpt_config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["gpt-3.5-turbo"],
        },
    )

# Log GPT model config
logger.debug(gpt_config_list)

# Set up GPT config
gpt_config = {
    "timeout": TIMEOUT,
    "cache_seed": CACHE_SEED,
    "config_list": gpt_config_list,
    "temperature": TEMPERATURE,
}

# Log GPT config
logger.debug("GPT Config: %s", gpt_config)

# Load configs for desired image model
IMAGE_MODEL = os.environ.get("IMAGE_MODEL", "dall-e-2")
if IMAGE_MODEL == "dall-e-3":
    # Load OpenAI dall-e-3 model config from env, or file
    image_config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["dall-e-3"],
        },
    )
else:
    # Load OpenAI gpt35turbo model config from env, or file
    image_config_list = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": ["dall-e-2"],
        },
    )

# Log GPT model config
logger.debug(image_config_list)

# Set up GPT config
image_config = {
    "timeout": TIMEOUT,
    "cache_seed": CACHE_SEED,
    "config_list": image_config_list,
    "temperature": TEMPERATURE,
}

# Log image config
logger.debug("Image Config: %s", image_config)
