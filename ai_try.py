import asyncio
from googletrans import Translator


def language_model_prompt():
    print("The languages available are :\n 1. Hindi\n 2. Spanish\n 3. German\n 4. French\n 5. Chinese\n 6. Japanese\n 7. English")
    number = input("Enter the language number you want to convert the prompt to: ")
    prompt = input("Enter the prompt you want to convert: ")

    # Initialize the translator
    translator = Translator()

    # Dictionary mapping numbers to language codes
    language_codes = {
        1: 'hi',  # Hindi
        2: 'es',  # Spanish
        3: 'de',  # German
        4: 'fr',  # French
        5: 'zh-cn', # Chinese
        6: 'ja',  # Japanese
        7: 'en'   # English
    }

    # Validate numeric input
    try:
        number = int(number)
    except ValueError: 
        print("Invalid input: Please enter a valid number (1-7)")
        return

    if number not in language_codes:
        print("Invalid input: Please choose a number between 1 and 7")
        return

    try:
        # Translate the text
        lang_code = language_codes[number]
        translated = translator.translate(prompt, dest=lang_code)

        # Some versions of the googletrans client return a coroutine (async)
        # while others return a synchronous object. Handle both.
        if asyncio.iscoroutine(translated):
            translated = asyncio.run(translated)

        print(f"\nOriginal text: '{prompt}'")
        # translated may be an object with .text and .dest attributes
        text_out = getattr(translated, 'text', str(translated))
        dest_out = getattr(translated, 'dest', lang_code)
        print(f"Translated text: '{text_out}'")
        print(f"Translated to: {dest_out}")
    except Exception as e:
        print(f"An error occurred during translation: {e}")


if __name__ == "__main__":
    language_model_prompt()