from urlshort import create_app


def test_shorten(client):
    response = client.get("/")
    assert b"shortenz" in response.data
