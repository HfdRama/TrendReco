from sentence_transformers import SentenceTransformer
import numpy as np

model = None

def get_model():
    global model

    if model is None:
        print("Loading SentenceTransformer...")
        model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

    return model


def embed(texts):

    model = get_model()

    # bersihkan data kosong
    texts = [
        str(t).strip()
        for t in texts
        if t is not None and str(t).strip()
    ]

    if len(texts) == 0:
        return np.array([])

    vecs = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=False
    )

    return np.asarray(vecs)