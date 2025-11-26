# scaling-octo-carnival
# Healthcare IoT on 6G -  Package

Contents:
- app.py                 : Flask-based working simulation dashboard + API
- static/                : static assets (js/css)
  - js/dashboard.js
  - css/style.css
- templates/
  - dashboard.html       : Mobile-friendly UI mockup and live dashboard
- diagrams/
  - architecture.svg     : System architecture diagram (SVG)
  - flowchart.svg        : Flowchart of system processes (SVG)
  - uml.svg              : Simple UML class diagram (SVG)
- requirements.txt
- LICENSE

How to run
----------
1. Create a Python environment (optional):
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows PowerShell

2. Install requirements:
   pip install -r requirements.txt

3. Run the Flask app:
   python app.py

4. Open the dashboard in your browser:
   http://localhost:8080

What this demo does
-------------------
- Simulates real-time patient vitals (/api/patient)
- Simulates robotic command execution (/api/surgery/<cmd>)
- Provides a responsive dashboard showing live vitals and latency
- Includes SVG diagrams: architecture, flowchart, UML
