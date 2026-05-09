import pint

ureg = pint.UnitRegistry()

def meters_to_kilometers(meters: float) -> float:
    """Konwertuje metry na kilometry."""
    distance = meters * ureg.meter
    return distance.to(ureg.kilometer).magnitude