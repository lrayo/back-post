from flask import Flask, request, jsonify
from flask_cors import CORS
from .models import save_beacon_event


app = Flask(__name__)
CORS(app)

@app.route("/api/beacon-event", methods=["POST"])
def beacon_event():
    try:
        data = request.get_json()
        mac = data.get("mac_address")
        lat = data.get("latitude")
        lon = data.get("longitude")
        phone = data.get("phone_number")
        event_type = data.get("event_type")

        if not mac or not event_type:
            return jsonify({"error": "Faltan campos requeridos"}), 400

        save_beacon_event(mac, lat, lon, phone, event_type)
        return jsonify({"message": "✅ Evento guardado exitosamente"}), 200
    except Exception as e:
        print("🔥 ERROR:", str(e))  # Esto se verá en los logs de Vercel
        return jsonify({"error": str(e)}), 500


