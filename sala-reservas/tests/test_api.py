from app.api import app

# Test to verify successful reservation
def test_reserva_exitosa():
    cliente = app.test_client()
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 201

# Test to verify duplicate reservation handling
def test_reserva_duplicada():
    cliente = app.test_client()
    cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 409
