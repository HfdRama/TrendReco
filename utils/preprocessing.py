import re

try:
    from indoNLP.preprocessing import replace_slang
except:
    def replace_slang(text):
        return text

from rapidfuzz import process
from Sastrawi.StopWordRemover.StopWordRemoverFactory import (
    StopWordRemoverFactory
)

# ==================================
# STOPWORDS
# ==================================
factory = StopWordRemoverFactory()

STOPWORDS = set(
    factory.get_stop_words()
)

# ==================================
# GLOBAL VOCABULARY
# ==================================
VOCABULARY = []
VOCABULARY_SET = set()


def set_vocabulary(vocab):
    global VOCABULARY, VOCABULARY_SET

    clean_vocab = list(
        set(
            str(w).lower().strip()
            for w in vocab
            if str(w).strip()
        )
    )

    # Batasi maksimal 5000 kata
    VOCABULARY = clean_vocab[:5000]

    VOCABULARY_SET = set(VOCABULARY)

    print(f"Vocabulary Loaded: {len(VOCABULARY)} words")


def build_vocabulary(texts):

    vocab = set()

    for text in texts:

        text = cleaning(
            case_folding(text)
        )

        for word in text.split():

            if len(word) >= 3:
                vocab.add(word)

    return list(vocab)


# ==================================
# VALID TOPIC
# ==================================
def is_valid_topic(text):

    text = str(text).lower().strip()

    if len(text) < 5:
        return False

    if len(text.split()) > 8:
        return False

    if re.search(r'(.)\1{4,}', text):
        return False

    spam_words = [
        "slot",
        "gacor",
        "rtp",
        "maxwin",
        "login",
        "apk",
        "cyou",
        "musang",
        "xlme"
    ]

    if any(w in text for w in spam_words):
        return False

    digit_ratio = (
        sum(c.isdigit() for c in text)
        / max(len(text), 1)
    )

    return digit_ratio <= 0.3


# ==================================
# CASE FOLDING
# ==================================
def case_folding(text):

    if text is None:
        return ""

    return str(text).lower()


# ==================================
# CLEANING
# ==================================
def cleaning(text):

    if text is None:
        return ""

    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"www\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ==================================
# TYPO CORRECTION
# ==================================
def correct_typo(word):

    if len(word) <= 3:
        return word

    # Jika kata sudah ada di vocab
    if word in VOCABULARY_SET:
        return word

    # Hindari kata panjang
    if len(word) > 15:
        return word

    # Hanya koreksi kata pendek
    if len(word) > 8:
        return word

    # Tidak ada vocabulary
    if not VOCABULARY:
        return word

    try:

        match = process.extractOne(
            word,
            VOCABULARY,
            score_cutoff=90
        )

        if match:
            return match[0]

    except:
        pass

    return word


# ==================================
# WORD SEGMENTATION
# ==================================
def split_compound_word(word):

    # Nonaktifkan sementara
    return word


# ==================================
# NORMALIZATION
# ==================================
def normalization(text):

    if not text:
        return ""

    try:

        text = replace_slang(text)

        normalized_words = []

        for word in text.split():

            token = correct_typo(word)

            normalized_words.append(token)

        return " ".join(normalized_words)

    except Exception as e:

        print("Normalization Error:", e)

        return text


# ==================================
# TOKENIZATION
# ==================================
def tokenizing(text):

    if not text:
        return []

    return [
        token.strip()
        for token in text.split()
        if token.strip()
    ]


# ==================================
# STOPWORD REMOVAL
# ==================================
def stopword_removal(tokens):

    if not tokens:
        return []

    return [
        token
        for token in tokens
        if token not in STOPWORDS
    ]


# ==================================
# FULL PREPROCESS
# ==================================
def full_preprocess(text):

    text_cf = case_folding(text)

    text_clean = cleaning(text_cf)

    text_norm = normalization(text_clean)

    tokens = tokenizing(text_norm)

    tokens_no_stop = stopword_removal(tokens)

    if not tokens_no_stop:
        tokens_no_stop = tokens

    return {

        "case_folding": text_cf,

        "cleaning": text_clean,

        "normalization": text_norm,

        "tokenization": tokens,

        "tokens": tokens,

        "final_tokens": tokens_no_stop,

        "final_text": " ".join(tokens_no_stop)
    }