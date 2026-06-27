import re

from indoNLP.preprocessing import replace_slang
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
# Akan diisi dari dataset
# ==================================
VOCABULARY = []


def set_vocabulary(vocab):

    global VOCABULARY

    VOCABULARY = list(
        set(vocab)
    )


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

    text = re.sub(
        r"http\S+",
        " ",
        text
    )

    text = re.sub(
        r"www\S+",
        " ",
        text
    )

    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ==================================
# TYPO CORRECTION
# ==================================
def correct_typo(word):

    if len(word) <= 3:
        return word

    if not VOCABULARY:
        return word

    match = process.extractOne(
        word,
        VOCABULARY,
        score_cutoff=85
    )

    if match:
        return match[0]

    return word


# ==================================
# WORD SEGMENTATION
# ==================================
def split_compound_word(word):

    if len(word) <= 8:
        return word

    if not VOCABULARY:
        return word

    result = []

    temp = word

    while len(temp) > 0:

        found = False

        for vocab in sorted(
            VOCABULARY,
            key=len,
            reverse=True
        ):

            if temp.startswith(vocab):

                result.append(vocab)

                temp = temp[len(vocab):]

                found = True

                break

        if not found:
            return word

    return " ".join(result)


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

            segmented = split_compound_word(
                word
            )

            for token in segmented.split():

                token = correct_typo(
                    token
                )

                normalized_words.append(
                    token
                )

        return " ".join(
            normalized_words
        )

    except Exception:

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

    text_clean = cleaning(
        text_cf
    )

    text_norm = normalization(
        text_clean
    )

    tokens = tokenizing(
        text_norm
    )

    tokens_no_stop = stopword_removal(
        tokens
    )

    if not tokens_no_stop:
        tokens_no_stop = tokens

    return {

        "case_folding": text_cf,

        "cleaning": text_clean,

        "normalization": text_norm,

        "tokenization": tokens,

        "tokens": tokens,

        "final_tokens": tokens_no_stop,

        "final_text": " ".join(
            tokens_no_stop
        )
    }