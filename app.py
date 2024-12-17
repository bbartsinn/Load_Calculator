# app.py

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import routes after initializing Flask to avoid circular imports
import routes  # Ensure you have a routes.py with your Flask routes

# Register the Blueprint
app.register_blueprint(routes.api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)