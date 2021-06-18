import pytest

import os
import sys
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from app import application

@pytest.fixture
def client():
    with application.test_client() as client:
        yield client

def test_some_data(client):
    r = client.get('/api/v1/somedata')
    assert b'{"some":"data"}\n' == r.data
def test_current_user(client):
    import json
    r = client.get('/api/v1/users/current')
    ans = {"meta": {"code": 200}, "response": {"data": {"user_id": None, "username": None, "email": None}}}
    assert ans == json.loads(r.data)

