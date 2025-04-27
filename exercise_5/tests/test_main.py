import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture
def created_vehicle():
    payload = {
        "veiculo": "Civic",
        "marca": "Honda",
        "ano": 2020,
        "descricao": "Sedan para teste",
        "vendido": False,
        "cor": "Preto"
    }
    response = client.post("/veiculos/", json=payload)
    assert response.status_code == 200
    vehicle = response.json()
    yield vehicle

    client.delete(f"/veiculos/{vehicle['id']}")


class TestVehicleAPI:

    def test_create_vehicle_success(self):
        payload = {
            "veiculo": "Corolla",
            "marca": "Toyota",
            "ano": 2021,
            "descricao": "Sedan médio",
            "vendido": False,
            "cor": "Branco"
        }
        response = client.post("/veiculos/", json=payload)
        assert response.status_code == 200
        assert response.json()["marca"] == "Toyota"

    def test_create_vehicle_invalid_brand(self):
        payload = {
            "veiculo": "Onix",
            "marca": "Xevrolé",
            "ano": 2020,
            "descricao": "Popular",
            "vendido": False,
            "cor": "Branco"
        }
        response = client.post("/veiculos/", json=payload)
        assert response.status_code == 400
        assert "Marca inválida" in response.json()["detail"]

    def test_list_vehicles(self):
        response = client.get("/veiculos/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_list_vehicles_with_filters(self, created_vehicle):
        response = client.get("/veiculos/", params={"marca": created_vehicle["marca"]})
        assert response.status_code == 200
        vehicles = response.json()
        assert any(v["marca"] == created_vehicle["marca"] for v in vehicles)

        response = client.get("/veiculos/", params={"cor": created_vehicle["cor"]})
        assert response.status_code == 200
        vehicles = response.json()
        assert any(v["cor"] == created_vehicle["cor"] for v in vehicles)

        response = client.get("/veiculos/", params={"ano": created_vehicle["ano"]})
        assert response.status_code == 200
        vehicles = response.json()
        assert any(v["ano"] == created_vehicle["ano"] for v in vehicles)

    def test_get_vehicle_success(self, created_vehicle):
        response = client.get(f"/veiculos/{created_vehicle['id']}")
        assert response.status_code == 200
        assert response.json()["id"] == created_vehicle["id"]

    def test_get_vehicle_not_found(self):
        response = client.get("/veiculos/99999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Veículo não encontrado"

    def test_update_vehicle_partial(self, created_vehicle):
        payload = {
            "descricao": "Sedan atualizado parcialmente"
        }
        response = client.patch(f"/veiculos/{created_vehicle['id']}", json=payload)
        assert response.status_code == 200
        assert response.json()["descricao"] == "Sedan atualizado parcialmente"

    def test_update_vehicle_full_success(self, created_vehicle):
        payload = {
            "veiculo": "HR-V",
            "marca": "Honda",
            "ano": 2022,
            "descricao": "SUV atualizado totalmente",
            "vendido": True,
            "cor": "Preto"
        }
        response = client.put(f"/veiculos/{created_vehicle['id']}", json=payload)
        assert response.status_code == 200
        assert response.json()["veiculo"] == "HR-V"
        assert response.json()["vendido"] is True

    def test_update_vehicle_full_missing_field(self, created_vehicle):
        payload = {
            "veiculo": "Fit"
        }
        response = client.put(f"/veiculos/{created_vehicle['id']}", json=payload)
        assert response.status_code == 422
        assert "errors" in response.json() or "detail" in response.json()

    def test_delete_vehicle_success(self):
        payload = {
            "veiculo": "Focus",
            "marca": "Ford",
            "ano": 2018,
            "descricao": "Hatch para deletar",
            "vendido": False,
            "cor": "Cinza"
        }
        response_create = client.post("/veiculos/", json=payload)
        assert response_create.status_code == 200
        vehicle_id = response_create.json()["id"]

        response_delete = client.delete(f"/veiculos/{vehicle_id}")
        assert response_delete.status_code == 200
        assert response_delete.json()["id"] == vehicle_id

        response_get = client.get(f"/veiculos/{vehicle_id}")
        assert response_get.status_code == 404

    def test_statistics_endpoint(self):
        response = client.get("/estatisticas/")
        assert response.status_code == 200
        data = response.json()
        assert "total_not_sold" in data
        assert "vehicles_by_decade" in data
        assert "vehicles_by_brand" in data
        assert "vehicles_created_last_week" in data

    def test_update_vehicle_partial_invalid_brand(self, created_vehicle):
        payload = {
            "marca": "Xevrolé"  # Marca inválida para validar no patch
        }
        response = client.patch(f"/veiculos/{created_vehicle['id']}", json=payload)
        assert response.status_code == 400
        assert "Marca inválida" in response.json()["detail"]

    def test_update_vehicle_partial_not_found(self):
        payload = {
            "descricao": "Tentativa de update parcial em veículo inexistente"
        }
        response = client.patch("/veiculos/99999", json=payload)
        assert response.status_code == 404
        assert response.json()["detail"] == "Veículo não encontrado"

    def test_update_vehicle_full_not_found(self):
        payload = {
            "veiculo": "FakeCar",
            "marca": "Honda",
            "ano": 2030,
            "descricao": "Fake update full",
            "vendido": False,
            "cor": "Azul"
        }
        response = client.put("/veiculos/99999", json=payload)
        assert response.status_code == 404
        assert response.json()["detail"] == "Veículo não encontrado"

    def test_delete_vehicle_not_found_direct(self):
        response = client.delete("/veiculos/99999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Veículo não encontrado"

    def test_database_initialization(self):
        from app.models import init_db
        init_db()
        assert True
