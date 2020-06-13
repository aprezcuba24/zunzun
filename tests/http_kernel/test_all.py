from zunzun import Router
from injector import Injector
from zunzun.testing import Client


injector = Injector()
router = injector.get(Router)


@router.get("/")
def action():
    return "action response"


def test_http_method():
    client = Client.create(injector)
    response = client.get("/")
    assert response.status_code == 200
    assert str(response.data) == "b'action response'"
