import sys
import os
from flask import Flask, jsonify, request

# Adicionar o diretório raiz ao path para importar o core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ai_engine.engine import AIEngine
from core.automation_module.automation import AutomationModule
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar os módulos do framework
ai_engine = AIEngine(api_key=app.config['OPENAI_API_KEY'])
automation = AutomationModule()

@app.route('/')
def index():
    return jsonify({
        "status": "online",
        "framework": "AI Framework Core",
        "version": "1.0.0"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Endpoint para interagir com o motor de IA.
    """
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt não fornecido"}), 400

    response = ai_engine.generate_response(prompt)
    return jsonify({"response": response})

@app.route('/api/automate', methods=['POST'])
def automate():
    """
    Endpoint para executar uma automação.
    """
    data = request.get_json()
    rule_name = data.get('rule_name')
    rule_data = data.get('data')

    if not rule_name:
        return jsonify({"error": "Nome da regra não fornecido"}), 400

    result = automation.execute_rule(rule_name, rule_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
