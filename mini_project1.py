from langdetect import detect, detect_langs
from googletrans import Translator
import asyncio

# Common language codes -> readable names
LANGUAGES = {
	'en': 'English',
	'hi': 'Hindi',
	'es': 'Spanish',
	'de': 'German',
	'fr': 'French',
	'zh-cn': 'Chinese (Simplified)',
	'ja': 'Japanese',
	'pt': 'Portuguese',
	'ru': 'Russian',
}

NUMBERED_LANGS = {
	1: 'hi',
	2: 'es',
	3: 'de',
	4: 'fr',
	5: 'zh-cn',
	6: 'ja',
	7: 'en',
	8: 'pt',
	9: 'ru',
}


def detect_language(text):
	try:
		code = detect(text)
		return code
	except Exception:
		return None





def translate_text(text, dest_code):
	translator = Translator()
	try:
		res = translator.translate(text, dest=dest_code)

		# Some googletrans versions return a coroutine; await if so.
		if asyncio.iscoroutine(res):
			res = asyncio.run(res)

		# Return expected tuple (text, src, dest) safely
		text_out = getattr(res, 'text', str(res))
		src_out = getattr(res, 'src', None)
		dest_out = getattr(res, 'dest', dest_code)
		return text_out, src_out, dest_out
	except Exception:
		raise
def detect_probabilities(text):
	try:
		return detect_langs(text)
	except Exception:
		return []

def show_available_languages():
	print("Languages available for translation:")
	for n, code in NUMBERED_LANGS.items():
		print(f" {n}. {LANGUAGES.get(code, code)} ({code})")
	print("You may also enter a language code directly (for example: en, hi, es)")


def main():
	print("Mini Project — Language detector + translator+Probabilty viewer")
	print("Enter a short sentence or paragraph and I'll detect the language and optionally translate it.")
	text = input("\nEnter text: ").strip()
	if not text:
		print("No text entered. Exiting.")
		return

	code = detect_language(text)
	if not code:
		print("Could not detect language.")
		return

	print(f"Detected language code: {code}")
	print(f"Detected language name: {LANGUAGES.get(code, 'Unknown')}")

	see_probs = input("Do you want the detection probabilities for other languages? (y/n): ")
	if see_probs.lower().startswith('y'):
		probs = detect_probabilities(text)
		print("Probabilities:")
		for p in probs:
			# p is like 'en:0.99'
			print(f"  {p}")

	do_translate = input("Do you want to translate this text? (y/n): ")
	if not do_translate.lower().startswith('y'):
		print("Done. Thank you for using the mini-project.")
		return

	show_available_languages()
	dest = input("Choose target language number or language code: ")

	# try to interpret as number
	dest_code = None
	try:
		n = int(dest)
		dest_code = NUMBERED_LANGS.get(n)
	except Exception:
		# not a number — treat as code
		dest_code = dest.strip()

	if not dest_code:
		print("Invalid language selection. Exiting.")
		return

	try:
		translated_text, src, dest_used = translate_text(text, dest_code)
		print("\n--- Translation Result ---")
		print(f"Source language detected: {src}")
		print(f"Translated to: {LANGUAGES.get(dest_used, dest_used)} ({dest_used})")
		print(f"Translated text: {translated_text}")
	except Exception as e:
		print(f"Translation failed: {e}")


if __name__ == '__main__':
	main()

