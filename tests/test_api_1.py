import requests
from pydantic import BaseModel


class Response(BaseModel):
    rates: dict
    code: int


class TestEndpoint:
    def test_pair(self):
        uri = "https://www.freeforexapi.com/api/live?pairs=USDRUB"
        response = Response(**requests.get(uri).json())
        value = response.rates.get("USDRUB").get("rate")
        print()
        print(f"Rate: {value}")
        print(f"Response: {response.code}")
        assert value < 100
        assert response.code == 200
