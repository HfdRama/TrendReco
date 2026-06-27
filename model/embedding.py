from sentence_transformers import SentenceTransformer

model = None

def get_model():
    global model
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def embed(texts):
    vecs = model.encode(texts)

    # force clean numpy array
    import numpy as np
    vecs = np.asarray(vecs)

    return vecs