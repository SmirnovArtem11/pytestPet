import pytest
import requests
from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'
])
def test_something(status, get_number, make_number, get_player_generator):
    assert 1 == 1
    print(get_player_generator.set_status(status).build())
    print(make_number)


@pytest.mark.parametrize('delete_key', [
    'status',
    'balance',
    'avatar',
    'localize'
])
def test_something(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]

    print(object_to_send)


@pytest.mark.parametrize('localization,region',[
    ('fr', 'fr_FR')
]
)
def test_something(get_player_generator, localization, region):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localization], PlayerLocalization(region).build()
                                          ).build()
    print(object_to_send)