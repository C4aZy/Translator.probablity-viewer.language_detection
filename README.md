# Mini Project: Language Detector + Translator

This small project combines language detection (using `langdetect`) and translation (using `googletrans`).

Files:
- `mini_project1.py` — interactive CLI: detects language and optionally translates to a chosen language.
- `language_detection.py` — original language-detection script (left unchanged).
- `ai_try.py` — original translation example (left unchanged).
- `requirements.txt` — Python dependencies.

Quick start

1. Create a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the mini project runner:

```bash
python mini_project1.py
```

Notes
- `googletrans` is an unofficial client for Google Translate and may behave intermittently. If you hit issues, try again later or use an alternative translation API.
- If you only need detection, `language_detection.py` can be used directly.

Feel free to tell me if you want this converted to a small CLI with argparse, a GUI, or a web interface.
