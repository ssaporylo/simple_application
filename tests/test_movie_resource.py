from asynctest.mock import patch
from asynctest import CoroutineMock
from tests.fixtures import people, films


@patch("asyncio.gather", CoroutineMock(return_value=(people, films)))
async def test_claims_task_list(test_client):
    resp = await test_client.get('/movies')
    data = await resp.json()
    assert resp.status == 200
    assert len(data) == 2
