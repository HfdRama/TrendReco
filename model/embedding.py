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


def embed(texts, batch_size=2):

    model = get_model()

    all_vectors = []

    for i in range(0, len(texts), batch_size):

        batch = texts[i:i + batch_size]

        print(
            f"Embedding batch {i+1} - {i+len(batch)}"
        )

        vectors = model.encode(
            batch,
            batch_size=batch_size,
            show_progress_bar=False,
            convert_to_numpy=True
        )

        all_vectors.extend(vectors)

    return np.array(all_vectors)