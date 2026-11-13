import logging
import os
from flask import Flask, jsonify, request

LOG_DIR = os.environ.get("LOG_DIR", "/logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(LOG_DIR, "app.log")),
    ],
)

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Home page requested from %s", request.remote_addr)
    return "<h1>Hello from AWS - deployed by GitHub Actions!</h1><p>Deployed with Terraform, Docker and GitHub Actions.</p>"

@app.route("/health")
def health():
    app.logger.info("Health check requested")
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)