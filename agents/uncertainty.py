import random

def uncertainty(state):
    score = round(random.uniform(0.6, 0.9), 2)
    return {**state, "confidence": score}
