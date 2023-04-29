import requests
from configuration import urlForCheck
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users, get_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(get_number)


def test_for_print():
    response = requests.get(urlForCheck)
    if response:
        print(response.json())
        assert 1 == 1, '1!=1'
    pass


