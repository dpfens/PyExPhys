def temperature(seconds, farenheit):
    """
    args:
        seconds: time of performance
        farenheit (float): ambient temperature during the performance, given in farenheit

    Returns:
        float: time of performance, adjusted for temperature
    """
    factors = {
        "60": 1,
        "65": 1.0075,
        "70": 1.015,
        "75": 1.0225,
        "80": 1.03,
        "85": 1.0375,
        "90": 1.045,
        "95": 1.0525,
        "100": 1.06
    }
    return seconds * factors[seconds]
