import re

def extract_quantity(text):
    nums = re.findall(r'\d+', text)
    return int(nums[0]) if nums else 1

def detect_device(text):
    text = text.lower()
    
    if "central" in text:
        return "central_ac"
    if "split" in text:
        return "split_ac"
    if "solar" in text:
        return "solar"
    if "generator" in text:
        return "generator"
    if "fan" in text:
        return "fan"
    
    return "split_ac"
