import requests
from testcontainers.core.container import DockerContainer

def test_get_users():
    # Send a GET request to the API
    container = DockerContainer("server:1.0")
   # port = container.get_exposed_port(80)
    response = requests.get(f"http://localhost/#/store/getInventory")
        
    # Assert the response status code is 200 (OK)
    assert response.status_code == 200