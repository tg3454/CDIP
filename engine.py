from data import DEVICE_POWER, EMISSION_FACTOR, HOURS_PER_DAY, DAYS_PER_MONTH, EFFICIENCY_SCORE
from utils import extract_quantity, detect_device
from ml_model import predict_future_pollution

def calculate_pollution(text, months):
    qty = extract_quantity(text)
    device = detect_device(text)
    
    power = DEVICE_POWER[device]
    
    energy = qty * power * HOURS_PER_DAY * DAYS_PER_MONTH * months
    pollution = energy * EMISSION_FACTOR
    
    predicted = predict_future_pollution(pollution)
    
    return round(predicted, 2), qty, device


def generate_option_c(optionA, optionB, months):
    qtyA = extract_quantity(optionA)
    qtyB = extract_quantity(optionB)
    
    central = max(1, qtyA // 2)
    split = max(1, qtyB // 2)
    
    text = f"{central} central ac + {split} split ac"
    pollution, _, _ = calculate_pollution(text, months)
    
    return text, pollution


def compare_options(pollA, pollB):
    if pollA < pollB:
        percent = ((pollB - pollA) / pollB) * 100
        return "better", round(percent, 2)
    else:
        percent = ((pollA - pollB) / pollA) * 100
        return "worse", round(percent, 2)


def explain_reason(devA, devB):
    if devA == devB:
        return "Both options use similar technology, but quantity affects energy consumption."
    if EFFICIENCY_SCORE[devA] > EFFICIENCY_SCORE[devB]:
        return f"{devA.replace('_', ' ')} is more energy efficient than {devB.replace('_', ' ')}."
    return f"{devB.replace('_', ' ')} consumes less energy than {devA.replace('_', ' ')}."
