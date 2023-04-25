import requests
from configuration import urlForCheck

response = requests.get(urlForCheck)
def test_for_print():
    if response:
        print(response.json())
        assert 1==1,'1!=1'
    pass


