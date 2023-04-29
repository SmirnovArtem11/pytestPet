'''fixtures uses for prerequizets'''
import pytest
import requests
from configuration import urlForCheck
@pytest.fixture(scope='session', autouse='True')     # код выполняется каждый раз, если сешн, тогда выполняется 1 раз и кэшируется
def get_users():
    response = requests.get(urlForCheck)
    return response

