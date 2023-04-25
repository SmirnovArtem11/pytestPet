import requests
from configuration import urlForCheck
from src.baseclasses.response import Response
from src.enums.global_enums import GlobalErrorMassages

from jsonschema import validate
# from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post
def test_geting_posts():
    r = requests.get(urlForCheck)
    response = Response(r)
    response.assert_status_code(200).validate(Post)
