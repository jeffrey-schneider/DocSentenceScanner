
# DocSentenceScanner

DocSentenceScanner is a Python utility designed to assist writers in editing large story drafts by locating sentences containing specific words or phrases. It helps streamline the editing process by identifying sentences that may need rephrasing or revision.

## Features

- Scan `.docx` files for sentences containing target words.
- Outputs lists of matching sentences for easy review.
- Designed to work with manually downloaded documents.
- Simple and lightweight — no external dependencies except `python-docx` and `nltk`.
- Git-friendly project structure.

## Project Structure

```
DocSentenceScanner/
├── downloads/         # Place your .docx files here
├── output/            # Extracted sentences will be saved here
├── main.py            # Main script to scan documents
├── wordlist.txt       # List of words/phrases to search for
├── .gitignore         # Ignore venv and output folders
└── README.md          # Project description
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YourUsername/DocSentenceScanner.git
   cd DocSentenceScanner
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

*(Note: `requirements.txt` will be added in a future commit.)*

## Usage

1. Place your `.docx` documents in the `downloads/` folder.
2. List the target words you want to search for in `wordlist.txt` (one word/phrase per line).
3. Run the script:

   ```bash
   python main.py
   ```

4. Found sentences will be saved inside the `output/` folder, organized by document.

## Future Enhancements

- Add `.txt` file support.
- Improve word matching with word boundaries.
- Create a summary report combining all results.
- Optional: GUI front-end for easier usage.

## License

This project is licensed under the MIT License. Feel free to use and modify it!

## Author

Jeffrey Schneider

---

*DocSentenceScanner – Helping writers clean up their masterpieces one sentence at a time.*
```

