from unit_converter.converter import meters_to_kilometers

def test_meters_to_kilometers():
    assert meters_to_kilometers(1000) == 1.0
    assert meters_to_kilometers(500) == 0.5