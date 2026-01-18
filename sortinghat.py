import re
from model import get_emotion_scores, emotion_columns
import numpy as np

def parse_whatsapp(text):
    messages = {}

    pattern = r"- (.?): (.)"

    for line in text.splitlines():
        match = re.search(pattern, line)
        if match:
            name, msg = match.groups()
            messages.setdefault(name, []).append(msg)

    return messages


def assign_character(avg_scores):
    top = emotion_columns[np.argmax(avg_scores)]

    if top in ["bravery", "anger", "confidence"]:
        return "Harry Potter"
    if top in ["curiosity", "intelligence"]:
        return "Hermione Granger"
    if top in ["caring", "love", "gratitude"]:
        return "Cedric Diggory"
    if top in ["pride", "desire"]:
        return "Draco Malfoy"
    if top in ["neutral", "surprise"]:
        return "Luna Lovegood"

    return "Neville Longbottom"


def sorting_hat(text):
    people = parse_whatsapp(text)
    results = {}

    for name, msgs in people.items():
        scores = []
        for m in msgs:
            s = get_emotion_scores(m)
            if s.any():
                scores.append(s)

        if scores:
            avg = np.mean(scores, axis=0)
            results[name] = assign_character(avg)

    return results