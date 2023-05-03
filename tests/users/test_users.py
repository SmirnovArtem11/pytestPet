import pytest
import requests
from configuration import urlForCheck
from src.baseclasses.response import Response
from src.schemas.user import User


@pytest.mark.production
@pytest.mark.development
def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)


@pytest.mark.skip('ISSUE-23414 Issue with network connection')
def test_for_print():
    response = requests.get(urlForCheck)
    if response:
        print(response.json())
        assert 1 == 1, '1!=1'
    pass


@pytest.mark.development
@pytest.mark.parametrize('first_val, second_val, result', [(1, 2, 3),
                                                           (-1, -2, -3),
                                                           ('1', 2, None),
                                                           ('a', 'b', None)])
def test_calculate(first_val, second_val, result, calculate):
    """
    In this test we are testing calculating with different values (Valid and Invalid)
    """

    assert calculate(first_val, second_val) == result


