import requests
from configuration import urlForCheck
from src.baseclasses.response import Response
from src.schemas.user import User

def test_getting_users_list():
    response = requests.get(urlForCheck)
    rest_object = Response(response)
    rest_object.assert_status_code(300).validate(User)

def test_for_print():
    response = requests.get(urlForCheck)
    if response:
        print(response.json())
        assert 1==1,'1!=1'
    pass


