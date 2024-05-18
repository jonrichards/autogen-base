import copy
import logging
import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get logging level
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "WARNING")

# Create logger
logger = logging

# Set logging level
logger.basicConfig(format="%(levelname)s:%(message)s", level=LOGGING_LEVEL)

# Masking constants
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
    logger.getLogger().addFilter(SensitiveDataFilter())
