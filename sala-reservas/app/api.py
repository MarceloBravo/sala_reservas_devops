from flask import Flask, request, jsonify
from app.reservas import verificar_disponibilidad

app = Flask(__name__)
reservas = []

@app.route('/reservar', methods=['POST'])
def reservar():
    # Extraer datos JSON de la solicitud
    data = request.get_json()
    # Verificar si la sala está disponible para la reserva
    disponible = verificar_disponibilidad(reservas, data)
    if disponible:
        # Agregar la reserva a la lista si está disponible
        reservas.append(data)
        return jsonify({"mensaje": "Reservada con éxito"}), 201
    else:
        # Devolver una respuesta de conflicto si la sala no está disponible
        return jsonify({"mensaje": "Sala no disponible"}), 409