
"""
Module docstring: This module handles translations between English and French.
"""

import os
from dotenv import load_dotenv
# import json
# from ibm_watson import LanguageTranslatorV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

def english_to_french(english_text):
    """Function to translate English text to French."""
    if english_text is None:
        raise ValueError("Input text cannot be None")
    # write the code here
    french_text = "dummy french text"  # define the frenchText before returning
    return french_text

def french_to_english(french_text):
    """Function to translate French text to English."""
    if french_text is None:
        raise ValueError("Input text cannot be None")
    # write the code here
    english_text = "dummy english text"  # define the englishText before returning
    return english_text


