from flask import Flask, jsonify, render_template, send_from_directory
import random, time, os

app = Flask(__name__, static_folder="static", template_folder="templates")

def sixg_latency():
    # simulate 0.1 - 1.0 ms latency
    return round(random.uniform(0.1, 1.0), 3)

def generate_patient_data():
    return {
        "patient_id": "P-1023",
        "heart_rate": random.randint(60, 110),
        "spo2": random.randint(90, 100),
        "blood_pressure_systolic": random.randint(110, 135),
        "blood_pressure_diastolic": random.randint(70, 90),
        "temperature_c": round(random.uniform(36.2, 37.8), 2),
        "ecg_alert_score": round(random.uniform(0, 100), 2),
        "latency_ms": sixg_latency(),
        "packet_loss_pct": round(random.uniform(0.0, 0.05), 4),
        "bandwidth_gbps": round(random.uniform(1.0, 10.0), 2)
    }

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/patient")
def api_patient():
    return jsonify(generate_patient_data())

@app.route("/api/surgery/<cmd>")
def api_surgery(cmd):
    latency = sixg_latency()
    # simulate processing delay (convert ms to seconds)
    time.sleep(latency/1000.0)
    return jsonify({
        "command_received": cmd,
        "robot_action": "Executed",
        "network_latency_ms": latency,
        "precision_accuracy": round(random.uniform(98.5, 100.0), 3)
    })

# Serve diagrams directory
@app.route("/diagrams/<path:filename>")
def diagrams(filename):
    return send_from_directory(os.path.join(app.root_path, "diagrams"), filename)

if __name__ == '__main__':
    # create directories if not present (helpful when running)
    os.makedirs("diagrams", exist_ok=True)
    os.makedirs(os.path.join("static","js"), exist_ok=True)
    os.makedirs(os.path.join("static","css"), exist_ok=True)
    os.makedirs("templates", exist_ok=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
