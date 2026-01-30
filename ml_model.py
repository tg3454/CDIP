import random

def predict_future_pollution(base):
    factor = random.uniform(0.95, 1.1)
    return round(base * factor, 2)

def confidence_score():
    return round(random.uniform(0.75, 0.95), 2)
