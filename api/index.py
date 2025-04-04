from flask import Flask, request, jsonify
from models import save_beacon_event
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/beacon-event', methods=['POST'])
def beacon_event():
    data = request.get_json()

    mac = data.get('mac_address')
    lat = data.get('latitude')
    lon = data.get('longitude')
    phone = data.get('phone_number')
    event_type = data.get('event_type')

    if not mac or not event_type:
        return jsonify({'error': 'mac_address y event_type son requeridos'}), 400

    try:
        save_beacon_event(mac, lat, lon, phone, event_type)
        return jsonify({'message': 'Evento guardado exitosamente'}), 200
    except Exception as e:
        import traceback
        print("❌ Error al guardar el evento:")
        traceback.print_exc()  # 👈 Mostrará el error real en logs de Vercel
        return jsonify({'error': str(e)}), 500
    
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
