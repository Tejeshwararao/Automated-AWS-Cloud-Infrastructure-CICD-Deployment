import logging
from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Home page requested")
    return "<h1>This is Teja DevOps Engineer!</h1><p>Deployed with Terraform, Docker and GitHub Actions.</p>"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)