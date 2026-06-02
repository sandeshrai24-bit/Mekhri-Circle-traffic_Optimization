from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.get_json()
        
        # Swapped key assignments to map correctly with the newly assigned input elements
        traffic = {
            "Airport": int(data.get('airport', 0)),
            "Jayamahal": int(data.get('jayamahal', 0)),
            "Vidhana Soudha": int(data.get('vidhana_soudha', 0)),
            "Yeshwanthpur": int(data.get('yeshwanthpur', 0))
        }

        total_vehicles = sum(traffic.values())
        if total_vehicles == 0:
            return jsonify({
                "selected_lane": "None",
                "vehicles": 0,
                "signal_time": 0,
                "empty": True
            })

        selected_lane = max(traffic, key=traffic.get)
        vehicles = traffic[selected_lane]

        if vehicles >= 40:
            signal_time = 70
        elif vehicles >= 30:
            signal_time = 55
        elif vehicles >= 20:
            signal_time = 40
        elif vehicles >= 10:
            signal_time = 25
        else:
            signal_time = 10

        return jsonify({
            "selected_lane": selected_lane,
            "vehicles": vehicles,
            "signal_time": signal_time,
            "empty": False
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
