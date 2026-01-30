# only sample data for testing real data will be used in production
DEVICE_POWER = {
    "split_ac": 1.5,
    "central_ac": 1.0,
    "fan": 0.07,
    "light": 0.02,
    "solar": 0.05,
    "generator": 2.5
}

EMISSION_FACTOR = 0.7  # kg CO2 per kWh

HOURS_PER_DAY = 8
DAYS_PER_MONTH = 30

EFFICIENCY_SCORE = {
    "central_ac": 0.9,
    "split_ac": 0.6,
    "solar": 1.0,
    "fan": 0.95,
    "generator": 0.3
}
