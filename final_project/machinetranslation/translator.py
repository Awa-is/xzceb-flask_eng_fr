import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('apikey')
url = os.getenv('url')

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(text):
    if text is None:
        return None
    elif text == '':
        return ''

    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def french_to_english(text):
    if text is None:
        return None
    elif text == '':
        return ''

    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation
