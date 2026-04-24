import uuid
import datetime
import json
import os

def generate_id():
    """
    Gera um ID único.
    """
    return str(uuid.uuid4())

def get_timestamp():
    """
    Retorna o timestamp atual formatado.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_config(path):
    """
    Carrega um arquivo de configuração JSON.
    """
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return json.load(f)

def format_currency(value, currency="BRL"):
    """
    Formata um valor numérico para moeda.
    """
    return f"{currency} {value:,.2f}"

def validate_email(email):
    """
    Validação simples de e-mail.
    """
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
