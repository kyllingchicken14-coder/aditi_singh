import numpy as np

# --------------------------------------------------
# 1. Rule table (THIS is where you add 100+ inputs)
# --------------------------------------------------

REPLY_RULES = [
    {
        "emotions": ["sadness", "grief", "remorse"],
        "replies": [
            "That sounds heavy, yaar. Want to talk about it?",
            "Damn, that’s rough. I’m here if you want to vent.",
            "Sounds like you’ve been carrying a lot lately."
        ]
    },
    {
        "emotions": ["anger", "annoyance"],
        "replies": [
            "Oof, that would piss anyone off. What happened?",
            "Yeah nah, that’s annoying as hell.",
            "I get why you’re mad. What set this off?"
        ]
    },
    {
        "emotions": ["joy", "excitement"],
        "replies": [
            "Haha niceee, that’s good vibes.",
            "Love that energy. What happened?",
            "Okay wait, that sounds fun."
        ]
    },
    {
        "emotions": ["fear", "nervousness"],
        "replies": [
            "That sounds stressful. Take a breath.",
            "Yeah I’d be nervous too, honestly.",
            "It’s okay to feel anxious about that."
        ]
    },
    {
        "emotions": ["love", "gratitude"],
        "replies": [
            "That’s actually really sweet.",
            "Aww, that’s nice to hear.",
            "That’s wholesome, not gonna lie."
        ]
    }
]

FALLBACK_REPLIES = [
    "Hmm. Tell me more.",
    "I’m listening.",
    "Go on.",
    "Yeah?"
]

# --------------------------------------------------
# 2. Main function (USED by FastAPI)
# --------------------------------------------------

def generate_reply(scores, emotion_columns):
    top_emotion = emotion_columns[np.argmax(scores)]

    for rule in REPLY_RULES:
        if top_emotion in rule["emotions"]:
            return np.random.choice(rule["replies"])

    return np.random.choice(FALLBACK_REPLIES)