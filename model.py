import pandas as pd
import numpy as np
import re
from collections import defaultdict
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

# --------------------
# Load dataset
# --------------------
df = pd.read_csv("data/goemotions_1.csv")

emotion_columns = [
    "admiration","amusement","anger","annoyance","approval",
    "caring","confusion","curiosity","desire","disappointment",
    "disapproval","disgust","embarrassment","excitement","fear",
    "gratitude","grief","joy","love","nervousness",
    "optimism","pride","realization","relief",
    "remorse","sadness","surprise","neutral"
]

def tokenize(text):
    tokens = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return [t for t in tokens if t not in ENGLISH_STOP_WORDS]

# --------------------
# Train word → emotion vectors
# --------------------
word_map = defaultdict(list)

for _, row in df.iterrows():
    vec = row[emotion_columns].values.astype(float)
    for token in tokenize(row["text"]):
        word_map[token].append(vec)

word_vectors = {
    w: np.mean(v, axis=0)
    for w, v in word_map.items()
}

emotion_basis = np.eye(len(emotion_columns))

# --------------------
# Public function
# --------------------
def get_emotion_scores(text):
    tokens = tokenize(text)
    vectors = [word_vectors[t] for t in tokens if t in word_vectors]

    if not vectors:
        return np.zeros(len(emotion_columns))

    sent_vec = np.mean(vectors, axis=0)
    scores = cosine_similarity(sent_vec.reshape(1, -1), emotion_basis)[0]
    return scores