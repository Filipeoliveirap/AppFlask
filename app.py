from flask import Flask, jsonify
from controllers.usuarios_controller import usuarios_bp
from controllers.instituicoes_controller import instituicoes_bp

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"versao": "2.0.0"}), 200

# blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(instituicoes_bp)

if __name__ == "__main__":
    app.run(debug=True)
