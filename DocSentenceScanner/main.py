import re
import os
import docx
import nltk

def ensure_nltk_data():
    """Ensure required NLTK data is available"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab/english.pickle')
    except LookupError:
        nltk.download('punkt_tab')

#Download NLTK's punkt tokenizaer if it hasn't been downloaded before
nltk.download('punkt')

#---Configuration ---
DOWNLOADS_FOLDER = os.path.join(os.getcwd(),'downloads')
OUTPUT_FOLDER = os.path.join(os.getcwd(),'output')
WORDLIST_FILE = os.path.join(os.getcwd(),"wordlist.txt")


def load_wordlist(filename):
    """Load search words from wordlist.txt"""
    with open(filename,'r',encoding='utf-8') as f:
        return [word.strip().lower() for word in f if word.strip()]

def extract_text_from_docx(filepath):
    """Extract all text from a .docx file."""
    doc = docx.Document(filepath)
    return '\n'. join([para.text for para in doc.paragraphs if para.text.strip()])



def find_sentences(text, wordlist):
    """Find and return sentences containing any full word from the wordlist, ignoring matches inside quotes."""
    sentences = nltk.sent_tokenize(text)
    matches = []

    for sentence in sentences:
        lowered = sentence.lower()

        # Remove text inside quotation marks before matching
        no_quotes = re.sub(r'(["“”])(.*?)\1', '', lowered)

        for word in wordlist:
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, no_quotes):
                matches.append((word, sentence))
                break  # Only record once even if multiple words match

    return matches


def find_sentences_bkup(text, wordlist):
    """Find and return sentences containing any full word from the wordlist."""
    sentences = nltk.sent_tokenize(text)
    matches = []

    for sentence in sentences:
        lowered = sentence.lower()
        for word in wordlist:
            pattern = r'\b' + re.escape(word) + r'\b'
            if re.search(pattern, lowered):
                matches.append((word, sentence))
                break  # Only record the first matching word per sentence

    return matches

def save_matches(output_path, matches):
    """Save matched sentences to a text file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for word, sentence in matches:
            #f.write(f"[{word} :-> {sentence}\n")
            f.write(f" reword this sentence: `{sentence}` to remove the word `{word}`\n")
            f.write("\n\n")

# --- main program ---

def main():
    ensure_nltk_data()
    wordlist = load_wordlist(WORDLIST_FILE)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for filename in os.listdir(DOWNLOADS_FOLDER):
        if filename.endswith('.docx'):
            filepath = os.path.join(DOWNLOADS_FOLDER, filename)
            print(f"Processing {filename}....")
            text = extract_text_from_docx(filepath)
            matches = find_sentences(text, wordlist)

            if matches:
                output_filename = filename.replace('.docx', '_matches.txt')
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)
                save_matches(output_path, matches)
                print(f"Matches found in {filename}, saved to {output_filename}")
            else:
                print(f"No matches found in {filename}")

if __name__ == "__main__":
    main()

