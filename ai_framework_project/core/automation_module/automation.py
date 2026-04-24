import requests
import json
import logging

class AutomationModule:
    """
    Módulo responsável por gerenciar automações, regras e chamadas de API.
    """

    def __init__(self, config=None):
        self.config = config or {}
        self.logger = logging.getLogger(__name__)

    def send_message(self, recipient, message, channel="web"):
        """
        Envia uma mensagem para um destinatário através de um canal específico.
        """
        self.logger.info(f"Enviando mensagem para {recipient} via {channel}: {message}")
        # Lógica de envio específica por canal seria implementada aqui
        return {"status": "success", "message": f"Mensagem enviada via {channel}"}

    def call_external_api(self, url, method="GET", headers=None, data=None):
        """
        Faz uma chamada a uma API externa.
        """
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data)
            else:
                return {"status": "error", "message": f"Método {method} não suportado"}

            response.raise_for_status()
            return {"status": "success", "data": response.json()}
        except Exception as e:
            return {"status": "error", "message": f"Erro ao chamar API externa: {str(e)}"}

    def execute_rule(self, rule_name, data):
        """
        Executa uma regra de automação pré-definida.
        """
        # Exemplo de regras simples
        if rule_name == "save_customer":
            return self.save_data("customers", data)
        elif rule_name == "trigger_notification":
            return self.send_message(data.get("email"), "Notificação importante!", channel="email")
        else:
            return {"status": "error", "message": f"Regra {rule_name} não encontrada"}

    def save_data(self, collection, data):
        """
        Salva dados em uma coleção específica (simulado).
        """
        self.logger.info(f"Salvando dados na coleção {collection}: {data}")
        # Integração com banco de dados seria implementada aqui
        return {"status": "success", "message": f"Dados salvos em {collection}"}
