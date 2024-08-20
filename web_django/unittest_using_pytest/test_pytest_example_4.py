"""
testing API
https://demoqa.com/utilities/weather/city/pune
"""
import requests

def test_api_city():
    response = requests.get("https://demoqa.com/utilities/weather/city/pune")
    response = response.json()
    assert "pune" in response.values()
    assert "City" in response.keys()
    assert ("City", "pune") in response.items()