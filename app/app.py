import copy
import logging
import os
import random

import autogen
from dotenv import load_dotenv

# Configure logging
load_dotenv()
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "WARNING")
logging.basicConfig(format="%(levelname)s:%(message)s", level=LOGGING_LEVEL)
MASKED_KEY = "api_key"
MASKED_VALUE = "********"
LOGGING_MASKING = os.environ.get("LOGGING_MASKING", "True")


# Filter API keys from logs
class SensitiveDataFilter(logging.Filter):

    # Filter log records
    def filter(self, record):
        if isinstance(record.msg, list):
            record.msg = self.mask_list(record.msg)
        elif isinstance(record.args, dict):
            for key, value in record.args.items():
                if isinstance(value, list):
                    record.args[key] = self.mask_list(value)
                elif isinstance(value, str):
                    if MASKED_KEY in key:
                        record.args[key] = MASKED_VALUE
        return True

    # Mask API keys in a list
    def mask_list(self, list_to_mask):
        new_msg = []
        for item in list_to_mask:
            if isinstance(item, dict) and MASKED_KEY in item:
                item = copy.deepcopy(item)
                item[MASKED_KEY] = MASKED_VALUE
            new_msg.append(item)
        return new_msg


# Add the API key filter to the logger if masking is enabled
if LOGGING_MASKING == "True":
    logging.getLogger().addFilter(SensitiveDataFilter())

# Load OpenAI model and API key info
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")
logging.debug(config_list)

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
logging.debug(config_list)

# Load LLM settings from env
CACHE_SEED = int(os.environ.get("CACHE_SEED", random.randint(1, 1000000)))
logging.debug("CACHE_SEED: %s", CACHE_SEED)

TEMPERATURE = int(os.environ.get("TEMPERATURE", "0"))
logging.debug("TEMPERATURE: %s", TEMPERATURE)

TIMEOUT = int(os.environ.get("TIMEOUT", "300"))
logging.debug("TIMEOUT: %s", TIMEOUT)

# Set up GPT config
gpt_config = {
    "timeout": TIMEOUT,
    "cache_seed": CACHE_SEED,
    "config_list": config_list,
    "temperature": TEMPERATURE,
}

logging.debug("GPT Config: %s", gpt_config)
