#pip install googletrans==4.0.0-rc1
from googletrans import Translator

# Create a Translator object
translator = Translator()

def translate_text():
    print("Welcome to the Language Translator!")
    text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

    try:
        # Translate the text
        translated = translator.translate(text, dest=target_language)
        print(f"\nOriginal Text: {text}")
        print(f"Translated Text ({target_language}): {translated.text}")
    except Exception as e:
        print(f"Error: {e}")
        print("Ensure that you entered a valid target language code.")

# Run the translation function
if __name__ == "__main__":
    translate_text()
"""
en: English
fr: French
es: Spanish
de: German
zh-cn: Chinese (Simplified)
hi: Hindi
ar: Arabic
"""